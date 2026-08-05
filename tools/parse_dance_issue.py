#!/usr/bin/env python3
"""
把「舞蹈影片候選清單追蹤」GitHub Issue 的內文，解析成 assign_dance_batch.py 吃得懂的 CSV。

用法：
    1. 用 mcp__github__issue_read(method='get', issue_number=<N>) 抓 issue 內文，存成 body.md
    2. python3 parse_dance_issue.py body.md > approved.csv
    3. python3 assign_dance_batch.py approved.csv --seed <日期> > assignment.csv
    4. 用 apply_dance_assignment_to_issue.py 把 assignment.csv 套回 issue 內文，再呼叫
       mcp__github__issue_write(method='update', body=<新內文>) 寫回去

只解析「## 待篩選」區塊裡「已勾選（- [x]）」的項目，「## 已分配」區塊會被忽略
（那些已經處理過，不該重複分配）。勾選但連結欄位是「(無...」開頭（代表還沒找到具體連結）的項目
會被跳過並印警告——這種項目不能直接送進分配流程，要先找到真正的連結再勾。
"""
import csv
import re
import sys

LINE_RE = re.compile(r"^- \[([ xX])\] `([^`]+)` \| (.*)$")


def parse(text):
    lines = text.splitlines()
    in_pending_section = False
    rows = []
    for line in lines:
        if line.strip().startswith("## "):
            in_pending_section = line.strip() == "## 待篩選"
            continue
        if not in_pending_section:
            continue
        m = LINE_RE.match(line.strip())
        if not m:
            continue
        checked, item_id, rest = m.groups()
        if checked.strip().lower() != "x":
            continue
        fields = [f.strip() for f in rest.split(" | ")]
        if len(fields) != 5:
            print(f"⚠️ 跳過格式不符的列（欄位數應為5，實際{len(fields)}）：{item_id}", file=sys.stderr)
            continue
        url, platform, source_type, note, found_date = fields
        if url.startswith("(") or not url.startswith("http"):
            print(f"⚠️ 跳過 {item_id}：已勾選但沒有具體連結（「{url}」），先找到真正的連結再勾選", file=sys.stderr)
            continue
        rows.append({
            "ID": item_id,
            "連結 URL": url,
            "平台": platform,
            "來源類型": source_type,
            "簡述": note,
            "發現日期": found_date,
            "核准(TRUE/FALSE)": "TRUE",
            "分配 KOL": "",
            "備註": "",
        })
    return rows


def main():
    if len(sys.argv) != 2:
        print("用法：python3 parse_dance_issue.py <issue_body.md>", file=sys.stderr)
        sys.exit(1)
    text = open(sys.argv[1], encoding="utf-8").read()
    rows = parse(text)
    if not rows:
        print("沒有解析到任何「已勾選 + 有具體連結」的項目", file=sys.stderr)
        sys.exit(1)
    writer = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
