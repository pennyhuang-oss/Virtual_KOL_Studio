#!/usr/bin/env python3
"""
舞蹈影片素材庫 — 核准清單 → KOL 分配

用法：
    python3 assign_dance_batch.py approved.csv --seed 2026-08-05 > assignment.csv

輸入 approved.csv 欄位需含：ID, 連結 URL（其餘欄位忽略）。
只放「核准=TRUE」且尚未分配過的列（已分配過的歷史紀錄不要放進來，避免重複指定同一支影片）。

分配規則：
- 每支影片只分配給一位 KOL（不重複）
- 12 位 KOL 平均分配：影片數 // 12 每人至少幾支，餘數依洗牌後的順序多分配 1 支
- 同一輪批次內，同一位 KOL 不會拿到兩支不同影片以外的重複——本邏輯本身即保證這件事
  （每支影片對應唯一一位 KOL，KOL 之間互不重疊）
- --seed 用於重現同一次分配結果（同 seed + 同輸入 = 同輸出），不是用來混淆，只是讓「洗牌」
  可重現而不是每次執行都不一樣
"""
import argparse
import csv
import json
import random
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KOL_INDEX = REPO_ROOT / "kols" / "index.json"


def load_kol_ids():
    data = json.loads(KOL_INDEX.read_text(encoding="utf-8"))
    return [k["id"] for k in data["kols"] if k.get("status") == "active"]


def load_approved(csv_path):
    rows = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("連結 URL", "").strip():
                continue
            rows.append(row)
    return rows


def assign(rows, kol_ids, seed):
    rng = random.Random(seed)
    kols = kol_ids[:]
    rng.shuffle(kols)
    videos = rows[:]
    rng.shuffle(videos)

    n_kols = len(kols)
    assignments = []
    for i, video in enumerate(videos):
        kol = kols[i % n_kols]
        assignments.append({**video, "分配 KOL": kol})

    # 平均分配檢查：回報每位 KOL 拿到幾支，供人工核對「平均」是否成立
    counts = {k: 0 for k in kol_ids}
    for a in assignments:
        counts[a["分配 KOL"]] += 1
    return assignments, counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="已核准（核准=TRUE）的候選清單 CSV")
    parser.add_argument("--seed", required=True, help="重現用的 seed，建議用當次執行日期字串，例如 2026-08-05")
    args = parser.parse_args()

    kol_ids = load_kol_ids()
    rows = load_approved(args.csv_path)

    if not rows:
        print("沒有讀到任何已核准的影片列（連結 URL 為空的列會被忽略）", file=sys.stderr)
        sys.exit(1)

    if len(rows) > len(kol_ids):
        print(
            f"⚠️ 核准影片數（{len(rows)}）多於 KOL 數（{len(kol_ids)}），"
            f"部分 KOL 會拿到超過 1 支——若不想這樣，先分批執行或增加 KOL 名單",
            file=sys.stderr,
        )

    assignments, counts = assign(rows, kol_ids, args.seed)

    writer = csv.DictWriter(sys.stdout, fieldnames=list(assignments[0].keys()))
    writer.writeheader()
    writer.writerows(assignments)

    print("\n--- 分配統計（人工核對用，非 CSV 內容）---", file=sys.stderr)
    for k, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{k}: {c} 支", file=sys.stderr)


if __name__ == "__main__":
    main()
