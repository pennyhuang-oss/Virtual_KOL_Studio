#!/usr/bin/env python3
"""
把 assign_dance_batch.py 的分配結果，套進「舞蹈影片候選清單追蹤」Issue 的內文：
把剛分配的項目從「## 待篩選」移到「## 已分配」，並標註分配到哪位 KOL。

用法：
    python3 apply_dance_assignment_to_issue.py current_body.md assignment.csv > new_body.md

然後把 new_body.md 的內容整份傳給 mcp__github__issue_write(method='update', body=<內容>)。
GitHub 沒有「附加/局部更新」issue 內文的 API，每次都要整份 body 重新送出，這是預期行為。
"""
import csv
import re
import sys

LINE_RE = re.compile(r"^- \[([ xX])\] `([^`]+)` \| (.*)$")


def main():
    if len(sys.argv) != 3:
        print("用法：python3 apply_dance_assignment_to_issue.py <current_body.md> <assignment.csv>", file=sys.stderr)
        sys.exit(1)

    body_text = open(sys.argv[1], encoding="utf-8").read()
    with open(sys.argv[2], encoding="utf-8") as f:
        assignment = {row["ID"]: row for row in csv.DictReader(f)}

    lines = body_text.splitlines()
    out_lines = []
    pending_removed_lines = []
    section = None
    assigned_ids_seen = set()

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            section = stripped[3:]
            out_lines.append(line)
            continue

        if section == "待篩選":
            m = LINE_RE.match(stripped)
            if m:
                _, item_id, _ = m.groups()
                if item_id in assignment:
                    # 從待篩選移除，記錄下來稍後插入已分配區塊
                    row = assignment[item_id]
                    pending_removed_lines.append(
                        f"- [x] `{item_id}` | {row['連結 URL']} | {row['分配 KOL']} | 待生成"
                    )
                    assigned_ids_seen.add(item_id)
                    continue  # 不寫進 out_lines，等於從待篩選刪掉
            out_lines.append(line)
            continue

        if section == "已分配" and pending_removed_lines:
            # 在「已分配」標題後、第一個非空白/非註解行之前插入新項目
            if stripped and not stripped.startswith("<!--"):
                out_lines.extend(pending_removed_lines)
                pending_removed_lines = []
            out_lines.append(line)
            continue

        out_lines.append(line)

    # 如果「已分配」區塊全是空的（沒有既有項目可以插在後面），保險起見補在檔尾前
    if pending_removed_lines:
        out_lines.extend(pending_removed_lines)

    missing = set(assignment.keys()) - assigned_ids_seen
    if missing:
        print(f"⚠️ 這些 ID 在「待篩選」區塊找不到，未套用：{', '.join(sorted(missing))}", file=sys.stderr)

    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
