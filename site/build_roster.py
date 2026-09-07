#!/usr/bin/env python3
"""Generate site/public/data/roster.json.

Hard specs (height / measurements / hair / face / ethnicity / soul status) are
read straight from kols/<id>/profile.json so the site can never drift from the
persona library. Editorial content (talent, evidence quote, first-wave video
proposal) lives in the EDITORIAL table below.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# id, 才藝分類, 主打才藝, 設定依據原文, 首波影片提案
EDITORIAL = [
    ("jia-seo", "舞蹈", "K-pop 編舞（練習生級）",
     "「十四歲進練習生體系，待了四年沒能出道」「對音樂的反應快到不需要思考」「手機裡有三百支沒發出去的練習影片」",
     "練舞室鏡面一鏡到底編舞，甩頭時薄荷綠 inner color 閃出"),
    ("wanyin-jiang", "舞蹈", "中國古典舞（水袖・身段）",
     "「從小學古典舞，藝校畢業」「身段是童子功，站著就跟別人不一樣」——本業旗袍訂製，儀態就是她的產品",
     "蘇州園林・水袖獨舞，旗袍開衩在轉身時剛好露出"),
    ("nanami-fujiwara", "舞蹈", "日本舞踊／和服所作",
     "「動作很輕，走路沒有聲音」「和服一天穿十小時，腰帶綁得很緊」——女將見習的所作訓練",
     "和室・扇子所作，赤足踏在榻榻米上無聲"),
    ("rin-ayase", "歌唱", "日本歌謠／爵士（成熟嗓）",
     "「二十一歲進銀座，四年做到店裡固定有指名」「和服與禮服的切換全是專業」——高級店的歌唱待客是職業技能的一部分",
     "銀座風鋼琴酒吧・一首慢歌，禮服＋手持麥"),
    ("somi-oh", "歌唱", "트로트／韓系流行（元氣嗓）",
     "「釜山人，家裡在市場旁邊開店，從小就在攤子之間長大」「慶尚道腔很重，她不改」",
     "釜山市場收攤後的路邊攤自彈自唱／트로트"),
    ("mia-huang", "歌唱", "直播歌回／動漫歌",
     "profile 原文：`Low-key proud of how good she's gotten at performing for a camera without it feeling like performing`——對鏡頭表演就是她的本業",
     "直播間歌回，耳機掛頸、聊天室字幕在旁"),
    ("emma-kao", "口語", "播報口條／主持",
     "「晚間新聞主播，今年是第五年」「表達能力極強，說話有結構」「習慣性在句子前面停半秒」",
     "「897 女團選秀」開場播報，一次到位不吃字"),
    ("tammy-chou", "口語", "直播口才 × 快速換裝秀",
     "「超級外向，直播四小時不會累」「晚上八點準時開播」「一件衣服會用三種角度拍」",
     "60 秒換 6 套的換裝 transition"),
    ("kanon-komori", "手作", "Cosplay 自製戲服 × 角色扮演",
     "「手很巧，服裝全部自己做」「自己打版、自己縫、自己拍」「房間有一台縫紉機比床還重要」",
     "從縫紉機到成品的 Cosplay 變身縮時 ＋ 角色定格"),
    ("wendy-yeo", "手作", "花式調酒 × 手鑿冰球",
     "「手藝是真的，得過獎」「首席調酒師」「冰球是自己切的，不用機器」「什麼時候該放什麼音樂」",
     "手鑿冰球特寫 → 一杯成品，全程幾乎無台詞"),
    ("luna-tanaka", "手作", "生け花（華道）× 底片攝影",
     "「外婆在伏見開一間小小的花藝教室，她繼承了構圖的眼光與等待的耐心」「為了等一朵雲移開等了 45 分鐘」",
     "生け花一鏡完成，底片機快門聲收尾"),
    ("rainie-hsu", "造型", "變裝 performance（一鏡完成）",
     "profile 原文：`Treats getting ready and going out as a performance art she has mastered`「Does her eyeliner first, every single time」；早年在西門町／東區 bartending and hosting 的控場底子",
     "眼線第一筆到出門那一步，鏡子前一鏡完成"),
    ("iris-chen", "造型", "鏡頭直覺／街拍",
     "profile 原文：`Always finds the best light in any room without thinking about it`、`Every photo looks candid even when it isn't`。**這是全 15 位裡設定依據最薄的一組才藝**——使用者以外形點選入列，才藝為合理延伸而非設定明載。實務上的補償：她是全庫影片素材最多的一位（3 支 dance reel＋多支 daily reel 已產出），首波成本最低",
     "台北街頭一鏡到底的街拍走位；亦可直接沿用既有 dance reel"),
    ("angeline-kwee", "造型", "造型改造 × 台步（171cm）",
     "「眼光很準，選的東西都賣得掉」「新貨到一定自己先用一週」「對品質有標準，對價格反而不在意」",
     "選物店改造企劃：素人穿搭 before／after ＋ 她自己的台步"),
    ("peggy-lee", "運動", "手排駕駛 × 車輛知識",
     "「自己開一台手排，從高中就跟著哥哥們跑車聚」「真的懂車，講得出規格」「對『花瓶』這個詞很敏感」",
     "夜衝・手排換檔特寫 ＋ 講得出規格的車輛介紹"),
]

VIDEOS = {
    "iris-chen": [
        "kols/iris-chen/videos/dance_v1/dance_v1_seedance_10s_black_crop_vietnam_drum.mp4",
        "kols/iris-chen/videos/dance_v1/dance_v3_seedance_15s_blue_dress_sugar_on_tongue.mp4",
        "kols/iris-chen/videos/daily_reel_music_r1/iris_daily_reel_r1.mp4",
    ],
    "luna-tanaka": [
        "kols/luna-tanaka/videos/dance_v1/luna_dance_v1.mp4",
        "kols/luna-tanaka/videos/daily_v1/luna_daily_v1.mp4",
    ],
}

ETH = {"台灣": "台灣", "日本": "日本", "韓國": "韓國", "中國": "中國",
       "Taiwanese": "台灣", "Japanese": "日本", "Korean": "韓國",
       "新加坡華裔（Chinese-Singaporean）": "新加坡華裔",
       "馬來西亞華裔（Chinese-Malaysian）": "馬來西亞華裔",
       "印尼華裔（Chinese-Indonesian）": "印尼華裔"}


def soul_status(p):
    """'已訓練' when a soul_id exists anywhere, else '建模圖已備齊・待送訓'."""
    found = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "soul_id" and v:
                    found.append(v)
                elif k == "status" and v == "deprecated":
                    pass
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(p)
    return "已訓練" if found else "待送訓"


def main():
    out = []
    for kid, group, talent, evidence, video in EDITORIAL:
        p = json.load(open(os.path.join(ROOT, "kols", kid, "profile.json")))
        i = p["identity"]
        a = i["appearance"]
        m = a.get("measurements", {})
        out.append({
            "id": kid,
            "name": i["name"],
            "native_name": i.get("native_name") or "",
            "handle": i.get("handle", ""),
            "age": i["age"],
            "ethnicity": ETH.get(i["ethnicity"], i["ethnicity"]),
            "location": i.get("current_location") or i.get("origin", ""),
            "group": group,
            "talent": talent,
            "evidence": evidence,
            "video_proposal": video,
            "archetype": p["persona"]["archetype"],
            "public_face": p["persona"].get("public_face") or "",
            "specs": {
                "height_cm": m.get("height_cm"),
                "bust_cm": m.get("bust_cm"),
                "waist_cm": m.get("waist_cm"),
                "hip_cm": m.get("hip_cm"),
                "cup": m.get("cup_size"),
                "whr": round(m["waist_cm"] / m["hip_cm"], 2) if m.get("hip_cm") else None,
                "leg_ratio": round(100 * m["leg_length_cm"] / m["height_cm"], 1)
                if m.get("leg_length_cm") and m.get("height_cm") else None,
            },
            "hair": a.get("hair", ""),
            "face": a.get("face_type") or "",
            "figure": a.get("figure") or "",
            "soul": soul_status(p),
        })

    roster = {"contestants": out, "videos": VIDEOS}
    dest = os.path.join(ROOT, "site/public/data/roster.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    json.dump(roster, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"{len(out)} contestants -> {dest}")
    for c in out:
        s = c["specs"]
        print(f"  {c['name']:18s} {c['ethnicity']:8s} {c['age']} "
              f"{s['height_cm']}cm {s['cup']} {s['bust_cm']}-{s['waist_cm']}-{s['hip_cm']} "
              f"WHR{s['whr']} leg{s['leg_ratio']}% [{c['group']}] {c['soul']}")


if __name__ == "__main__":
    main()
