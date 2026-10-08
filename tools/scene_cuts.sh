#!/usr/bin/env bash
# 量一支影片裡有幾個「真的切鏡」——用來驗證某個模型是否真的能在單次生成裡切鏡頭。
#
# 用法：tools/scene_cuts.sh <影片> [門檻，預設 0.30]
#
# ⚠️ 這個腳本踩過一個坑，寫在這裡免得下次再踩：
#     ffmpeg 的 showinfo 輸出走 stderr 的 info 層級，
#     如果加了 -v error，showinfo 會被整個吃掉 → 任何影片都回報「0 個切點」。
#     所以這裡改用 metadata=print，不依賴 log level。
#     校正方法：拿一支自己用 ffmpeg concat 硬切出來的片跑一次，必須要有切點。
set -euo pipefail
f="${1:?usage: scene_cuts.sh <video> [threshold]}"
th="${2:-0.30}"
ffmpeg -nostats -hide_banner -i "$f" \
  -vf "select='gt(scene,${th})',metadata=print:file=-" -an -f null - 2>/dev/null \
  | grep -o "pts_time:[0-9.]*" | sed 's/pts_time://'
