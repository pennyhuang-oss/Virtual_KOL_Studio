set -e
SP="$1"; R="$2"; FONT="$3"
cd "$SP/cut"
ffmpeg -v error -y \
 -i "$R/i2v_test01/rujiao_pour_test01.mp4" \
 -i "$R/shot2_speak/rujiao_shot2_speak_v1.mp4" \
 -i "$R/i2v_test02/rujiao_chickenpot_test02.mp4" \
 -loop 1 -t 5.4 -i "$R/start_frames/rujiao_shot4_sakura_9x16.png" \
 -filter_complex "\
[0:v]trim=0:2.2,setpts=PTS-STARTPTS,fps=30,scale=720:1280,setsar=1[v1];\
[1:v]trim=0:3.15,setpts=PTS-STARTPTS,fps=30,scale=720:1280,setsar=1[v2];\
[2:v]trim=0.6:4.6,setpts=PTS-STARTPTS,fps=30,scale=720:1280,setsar=1[v3];\
[3:v]scale=1440:2560,fps=30,zoompan=z='min(1.0+0.018*on/162\,1.018)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=720x1280:fps=30,trim=0:5.4,setpts=PTS-STARTPTS,setsar=1[v4];\
[v1][v2][v3][v4]concat=n=4:v=1:a=0[vc];\
[vc]drawbox=x=0:y=ih-330:w=iw:h=330:color=black@0.58:t=fill:enable='between(t,12.60,14.75)',\
drawtext=fontfile='$FONT':textfile=s1.txt:fontsize=52:fontcolor=white:borderw=3:bordercolor=black@0.75:x=(w-text_w)/2:y=h-300:enable='between(t,2.62,3.15)',\
drawtext=fontfile='$FONT':textfile=s2.txt:fontsize=52:fontcolor=white:borderw=3:bordercolor=black@0.75:x=(w-text_w)/2:y=h-300:enable='between(t,3.30,5.30)',\
drawtext=fontfile='$FONT':textfile=s3.txt:fontsize=52:fontcolor=white:borderw=3:bordercolor=black@0.75:x=(w-text_w)/2:y=h-300:enable='between(t,5.57,6.30)',\
drawtext=fontfile='$FONT':textfile=cta1.txt:fontsize=58:fontcolor=white:borderw=0:x=(w-text_w)/2:y=h-255:enable='between(t,12.75,14.75)',\
drawtext=fontfile='$FONT':textfile=cta2.txt:fontsize=40:fontcolor=white@0.9:borderw=0:x=(w-text_w)/2:y=h-160:enable='between(t,12.75,14.75)'[vout];\
[0:a]atrim=0:2.9,asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,afade=t=out:st=2.2:d=0.7[a1];\
[1:a]atrim=0:4.45,asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,adelay=2200|2200[a2];\
[2:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,asplit=2[p1][p2];\
[p1]atrim=0.6:5.0,asetpts=PTS-STARTPTS,volume=0.30,afade=t=out:st=3.6:d=0.8,adelay=5350|5350[a3];\
[p2]atrim=0.6:5.0,asetpts=PTS-STARTPTS,volume=0.16,afade=t=in:st=0:d=0.6,afade=t=out:st=3.6:d=0.8,adelay=9550|9550[a4];\
[a1][a2][a3][a4]amix=inputs=4:normalize=0:duration=longest,atrim=0:14.75,asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -r 30 -t 14.75 \
 -c:v libx264 -preset veryfast -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart \
 rujiao_cut_v1.mp4
