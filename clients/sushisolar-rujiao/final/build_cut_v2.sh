set -e
SP="$1"; R="$2"; F="$3"
cd "$SP/cut2"
SUB="fontfile='$F':fontsize=52:fontcolor=white:borderw=3:bordercolor=black@0.75:x=(w-text_w)/2:y=h-300"
ffmpeg -v error -y \
 -i "$R/shot2_speak/rujiao_shot2_speak_v1.mp4" \
 -i "$R/i2v_test01/rujiao_pour_test01.mp4" \
 -i "$R/i2v_test02/rujiao_chickenpot_test02.mp4" \
 -loop 1 -t 3.30 -i "$R/start_frames/rujiao_shot4_sakura_9x16.png" \
 -filter_complex "\
[0:v]trim=0:3.15,setpts=PTS-STARTPTS,fps=30,scale=720:1280,setsar=1[v1];\
[1:v]split=2[b1][b2];\
[b1]trim=0:1.25,setpts=PTS-STARTPTS,fps=30,scale=720:1280,setsar=1[v2];\
[b2]trim=2.6:3.9,setpts=PTS-STARTPTS,fps=30,crop=460:818:260:460,scale=720:1280,unsharp=5:5:0.6,setsar=1[v3a];\
[2:v]split=3[c2][c3][c4];\
[c2]trim=0.6:1.9,setpts=PTS-STARTPTS,fps=30,crop=450:800:140:40,scale=720:1280,unsharp=5:5:0.6,setsar=1[v3b];\
[c3]trim=2.0:3.2,setpts=PTS-STARTPTS,fps=30,crop=450:800:60:460,scale=720:1280,unsharp=5:5:0.6,setsar=1[v3c];\
[c4]trim=0.6:4.1,setpts=PTS-STARTPTS,fps=30,scale=720:1280,setsar=1[v4];\
[3:v]scale=1440:2560,fps=30,zoompan=z='min(1.0+0.016*on/99\,1.016)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=720x1280:fps=30,trim=0:3.30,setpts=PTS-STARTPTS,setsar=1[v5];\
[v1][v2][v3a][v3b][v3c][v4][v5]concat=n=7:v=1:a=0[vc];\
[vc]drawbox=x=0:y=ih-330:w=iw:h=330:color=black@0.58:t=fill:enable='between(t,12.85,15.0)',\
drawtext=fontfile='$F':textfile=hook.txt:fontsize=46:fontcolor=white:borderw=3:bordercolor=black@0.7:x=(w-text_w)/2:y=170:enable='between(t,0.30,2.80)',\
drawtext=$SUB:textfile=s1.txt:enable='between(t,0.42,0.95)',\
drawtext=$SUB:textfile=s2.txt:enable='between(t,1.10,3.00)',\
drawtext=$SUB:textfile=s3.txt:enable='between(t,3.37,4.15)',\
drawtext=$SUB:textfile=vo1.txt:enable='between(t,4.50,6.75)',\
drawtext=$SUB:textfile=vo2.txt:enable='between(t,6.85,8.15)',\
drawtext=$SUB:textfile=vo3.txt:enable='between(t,8.40,9.90)',\
drawtext=$SUB:textfile=vo4.txt:enable='between(t,10.00,11.55)',\
drawtext=fontfile='$F':textfile=sign.txt:fontsize=40:fontcolor=white:borderw=3:bordercolor=black@0.7:x=(w-text_w)/2:y=h-330:enable='between(t,11.90,12.80)',\
drawtext=fontfile='$F':textfile=cta1.txt:fontsize=58:fontcolor=white:x=(w-text_w)/2:y=h-255:enable='between(t,13.00,15.0)',\
drawtext=fontfile='$F':textfile=cta2.txt:fontsize=40:fontcolor=white@0.9:x=(w-text_w)/2:y=h-160:enable='between(t,13.00,15.0)'[vout];\
[0:a]atrim=0:4.45,asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[a1];\
[1:a]atrim=0:1.6,asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,volume=0.45,afade=t=out:st=1.1:d=0.5,adelay=3150|3150[a2];\
[2:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,asplit=2[p1][p2];\
[p1]atrim=0.5:5.0,asetpts=PTS-STARTPTS,volume=0.35,afade=t=in:st=0:d=0.5,adelay=4300|4300[a3];\
[p2]atrim=0.5:5.0,asetpts=PTS-STARTPTS,volume=0.22,afade=t=out:st=3.5:d=1.0,adelay=8800|8800[a4];\
[a1][a2][a3][a4]amix=inputs=4:normalize=0:duration=longest,atrim=0:15.0,asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -r 30 -t 15.0 \
 -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart \
 rujiao_cut_v2_animatic.mp4
