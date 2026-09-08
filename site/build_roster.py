#!/usr/bin/env python3
"""Generate site/public/data/roster.json.

Hard specs (height / measurements / hair / face / ethnicity / soul status) are
read straight from kols/<id>/profile.json so the site can never drift from the
persona library.

Talent is editorial and lives in the EDITORIAL table below. Talents are NOT
restricted to what a persona's profile already states. Per PERSONA_CANON.md
原則三 (styling is a *current* setting, never a permanent lock) and 原則四
(never write absolute prohibitions — "人是會變化的，不可能一個人設從一而終
走到底"), a persona can acquire a skill the same way she can change hair
colour. The requirements are that the skill stays compatible with her
established tone, and that it is written back into her profile.json once the
roster is signed off, so the library stays the single source of truth.

Every contestant carries two things:
  talent    — her individual showcase, what a voter remembers her for
  secondary — 唱／跳, the group-performance baseline, because the final three
              have to perform together as 897 女團
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# id, 才藝分類, 主打才藝, 才藝說明, 首波影片提案, 共同必修（唱／跳）
EDITORIAL = [
    ("jia-seo", "舞蹈", "K-pop 編舞（練習生級）",
     "「十四歲進練習生體系，待了四年沒能出道」「對音樂的反應快到不需要思考」「手機裡有三百支沒發出去的練習影片」",
     "練舞室鏡面一鏡到底編舞，甩頭時薄荷綠 inner color 閃出",
     "唱：練習生四年的聲樂訓練底子"),
    ("wanyin-jiang", "舞蹈", "中國古典舞（水袖・身段）",
     "「從小學古典舞，藝校畢業」「身段是童子功，站著就跟別人不一樣」——本業旗袍訂製，儀態就是她的產品",
     "蘇州園林・水袖獨舞，旗袍開衩在轉身時剛好露出",
     "唱：古典舞科班的氣息控制轉唱腔，走民族／古風路線"),
    ("rin-ayase", "歌唱", "日本歌謠／爵士（成熟嗓）",
     "「二十一歲進銀座，四年做到店裡固定有指名」「和服與禮服的切換全是專業」——高級店的歌唱待客是職業技能的一部分",
     "銀座風鋼琴酒吧・一首慢歌，禮服＋手持麥",
     "跳：禮服與和服的所作訓練，走慢板、控制型的舞台走位"),
    ("somi-oh", "歌唱", "트로트／韓系流行（元氣嗓）",
     "「釜山人，家裡在市場旁邊開店，從小就在攤子之間長大」「慶尚道腔很重，她不改」",
     "釜山市場收攤後的路邊攤自彈自唱／트로트",
     "跳：元氣型唱跳，市場長大的體力與外放度撐得住"),
    ("mia-huang", "歌唱", "直播歌回／動漫歌",
     "profile 原文：`Low-key proud of how good she's gotten at performing for a camera without it feeling like performing`——對鏡頭表演就是她的本業",
     "直播間歌回，耳機掛頸、聊天室字幕在旁",
     "跳：直播主標配的唱跳曲目，鏡頭前表演本來就是她的本業"),
    ("emma-kao", "口語", "播報口條／主持",
     "「晚間新聞主播，今年是第五年」「表達能力極強，說話有結構」「習慣性在句子前面停半秒」",
     "「897 女團選秀」開場播報，一次到位不吃字",
     "唱：主播的發聲與氣息訓練直接轉唱功"),
    ("tammy-chou", "口語", "直播口才 × 快速換裝秀",
     "「超級外向，直播四小時不會累」「晚上八點準時開播」「一件衣服會用三種角度拍」",
     "60 秒換 6 套的換裝 transition",
     "跳：直播四小時不累的體力，唱跳體能沒問題"),
    ("coco-wu", "口語", "鏡頭前的自然反應／綜藝感",
     "backstory 明載室友對她的評語：`妳鏡頭前面就是很自然很好笑欸`——帳號就是這樣被推著開起來的。"
     "「拍 vlog 拍到一半會突然開始講室友的八卦」「英文偶爾會蹦出可愛的破碎短句，自己講完會先笑場」。"
     "另有 4 支舞蹈 reel 已產出，舞蹈內容亦可低成本覆蓋",
     "宿舍 vlog 式的自我介紹，一鏡到底不剪，中途岔題講室友",
     "跳：已有 4 支舞蹈 reel 產出，全庫舞蹈素材最完整的一位"),
    ("kanon-komori", "手作", "Cosplay 自製戲服 × 角色扮演",
     "「手很巧，服裝全部自己做」「自己打版、自己縫、自己拍」「房間有一台縫紉機比床還重要」",
     "從縫紉機到成品的 Cosplay 變身縮時 ＋ 角色定格",
     "唱跳：女僕咖啡廳的現役偶像唱跳，本來就是她的職業技能"),
    ("luna-tanaka", "手作", "生け花（華道）× 底片攝影",
     "「外婆在伏見開一間小小的花藝教室，她繼承了構圖的眼光與等待的耐心」「為了等一朵雲移開等了 45 分鐘」",
     "生け花一鏡完成，底片機快門聲收尾",
     "跳：已有 2 支舞蹈 reel 產出，走安靜、細節型的舞感"),
    ("miu-shiraishi", "手作", "咖啡拉花",
     "「現在是店裡拉花最穩的人」「一天講不到十句話，但客人會為了看她做咖啡而排隊」"
     "「開店前一定先擦一次吧台，即使昨天擦過」「圍裙帶子綁在前面，不是後面」",
     "吧台俯角特寫：一杯拉花從注入到收尾，全程無台詞",
     "唱：氣音、低音量的日系唱法，與她寡言的調性一致"),
    ("rainie-hsu", "造型", "變裝 performance（一鏡完成）",
     "profile 原文：`Treats getting ready and going out as a performance art she has mastered`「Does her eyeliner first, every single time」；早年在西門町／東區 bartending and hosting 的控場底子",
     "眼線第一筆到出門那一步，鏡子前一鏡完成",
     "跳：高跟鞋 heels dance，早年夜店控場的舞台張力"),
    ("iris-chen", "造型", "鏡頭直覺／街拍",
     "profile 原文：`Always finds the best light in any room without thinking about it`、`Every photo looks candid even when it isn't`——鏡頭直覺是她的核心特質。她同時是本庫影片素材最完整的一位（3 支舞蹈 reel 與多支生活 reel 已產出），可立即投入首波內容",
     "台北街頭一鏡到底的街拍走位；亦可直接沿用既有 dance reel",
     "跳：已有 3 支舞蹈 reel 產出，可立即投入"),
    ("angeline-kwee", "造型", "造型改造 × 台步（171cm）",
     "「眼光很準，選的東西都賣得掉」「新貨到一定自己先用一週」「對品質有標準，對價格反而不在意」",
     "選物店改造企劃：素人穿搭 before／after ＋ 她自己的台步",
     "跳：171cm 的伸展台身體控制轉舞台走位"),
    ("yerin-han", "運動", "高爾夫（競技級揮桿）",
     "「大學打校隊，差一點轉職業，最後選擇當教練」「記得每個學生的握桿毛病」"
     "「室內練習場的固定打位不讓人」——她自己講得很清楚：球技讓人留下來，穿搭讓人進來",
     "室內練習場・慢動作揮桿與 trick shot，球帽後扣穿馬尾",
     "跳：競技運動底的核心與體能，學編舞快"),
]

VIDEOS = {
    # Smallest of her four dance reels — the others are 42-59MB each and the
    # site is served whole, so payload matters more than having all four.
    "coco-wu": [
        "kols/coco-wu/videos/dance_clone_r13/coco_dance_clone_r13_ig_reel.mp4",
    ],
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
    for kid, group, talent, evidence, video, secondary in EDITORIAL:
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
            "secondary": secondary,
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
