export const meta = {
  name: 'weekly-content-planner',
  description: "Plans one KOL persona's next 7 days of content (pillar, scene, caption, draft prompt) and reviews it against her own recent posting history so it doesn't repeat itself",
  whenToUse: 'Run once per KOL per week to produce the coming week\'s content calendar. Reads the persona\'s content_style.md for pillar weights/posting rhythm, checks kols/{id}/content_history.json to avoid repeating recent themes, drafts image/video prompts that already satisfy the SEXY_SCENE_LIBRARY.md anti-"AI look" checklist, then has a second agent critique the week for repetition/pillar-balance/caption-sameness before finalizing.',
  phases: [
    { title: 'Plan', detail: "Draft a 7-day content calendar from the persona's pillars + posting rhythm + recent history" },
    { title: 'Review', detail: 'Critique the draft week for repetition vs history, pillar-weight drift, caption sameness, checklist gaps' },
    { title: 'Finalize', detail: 'Write the approved calendar to disk and append this week to content_history.json' },
  ],
}

// args shape:
// {
//   koId: 'vicky-lin',
//   weekStartDate: '2026-07-28',   // Monday of the week being planned — pass in, never invent one
//   maxRevisions: 1,               // optional, defaults to 1
// }

const koId = args && args.koId
const weekStartDate = args && args.weekStartDate
const maxRevisions = args && args.maxRevisions != null ? args.maxRevisions : 1

const WEEK_PLAN_SCHEMA = {
  type: 'object',
  properties: {
    days: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          day: { type: 'string' },
          platform: { type: 'string' },
          pillar: { type: 'string' },
          scene: { type: 'string' },
          format: { type: 'string' },
          caption: { type: 'string' },
          draft_prompt: { type: 'string' },
          needs_manual_video_edit: { type: 'boolean' },
        },
        required: ['day', 'platform', 'pillar', 'scene', 'format', 'caption', 'draft_prompt'],
      },
    },
  },
  required: ['days'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    approved: { type: 'boolean' },
    issues: { type: 'array', items: { type: 'string' } },
    revision_instructions: { type: 'string' },
  },
  required: ['approved', 'issues'],
}

if (!koId || !weekStartDate) {
  log('缺少 koId 或 weekStartDate，跳過執行（安全空跑，用於驗證流程結構）')
}

let plan = null
let reviewResult = null

if (koId && weekStartDate) {
  phase('Plan')
  plan = await agent(
    `你在幫虛擬 KOL「${koId}」規劃下一週（從 ${weekStartDate} 這個週一開始的 7 天）的社群內容企劃。

請依序做這些事：
0. 先讀 PERSONA_CANON.md（人設憲章）。它定義了反差公式、標誌性場景配額、造型可變性與「不寫絕對禁令」四條原則，優先於任何角色檔案裡相衝突的敘述。企劃必須符合這四條。
1. 讀 kols/${koId}/profile.json 的 content.pillars —— **支柱名稱與權重以此為單一真理來源**（不要從 content_style.md 推測，也不要沿用「居家」這種舊命名）。再讀 kols/${koId}/content_style.md 取得各平台發文節奏與 caption 語氣範例。
   規劃時注意：「私下 / 她自己的空間」是最大支柱，內容是她精心打理過、只給自己和特定的人看的樣子，不是鬆垮耍廢；標誌性場景（泳池、和服、直播間、健身房、五星飯店等）一週最多出現一次。
2. 讀 kols/${koId}/character.md 確認她的人設語氣、視覺美學。
3. 讀 kols/${koId}/generation_notes.md 裡已經寫好的批次 prompt，可以直接沿用或延伸其中的場景，不用每次都憑空生出全新場景。
4. 如果 kols/${koId}/content_history.json 存在，讀取裡面最近幾週用過的支柱/場景主題，這一週的規劃要避開跟最近重複的具體場景（支柱本身當然會重複出現，因為那是她的固定內容比例，但「具體場景」不要跟最近幾週一樣）。如果檔案不存在，就當作沒有歷史紀錄。

然後產出 7 天份的企劃，每天包含：day（星期幾）、platform（對照她 content_style.md 裡的發文節奏，這天應該發哪個平台）、pillar（對應到哪個內容支柱）、scene（具體場景/主題，不是只寫支柱名稱）、format（照片/影片/Reels等）、caption（一句符合她語氣的 caption 草稿）、draft_prompt（一段完整可直接使用的英文生成 prompt，必須套用 SEXY_SCENE_LIBRARY.md 裡「降低 AI 感的技術要點」checklist——皮膚質感、具體裝置/鏡頭規格、混合不均勻光源、具體背景雜物細節、完整服裝描述）、needs_manual_video_edit（如果 format 是影片且需要配樂等人工後製，標記 true，理由可參考 DAILY_VIDEO_SOP.md / DANCE_VIDEO_SOP.md 裡記錄的限制；純圖片或不需要後製的影片標記 false）。

每天的支柱分配要大致符合 content_style.md 裡寫的權重比例（一週 7 天，用權重比例去分配天數，四捨五入即可，不需要精確到小數點）。`,
    { phase: 'Plan', label: `plan:${koId}:${weekStartDate}`, schema: WEEK_PLAN_SCHEMA }
  )

  let revisions = 0
  while (revisions <= maxRevisions) {
    phase('Review')
    reviewResult = await agent(
      `請審核這份虛擬 KOL「${koId}」${weekStartDate} 那週的內容企劃草案，檢查以下項目：
1. 跟 kols/${koId}/content_history.json（如果存在）裡最近幾週的具體場景相比，是否有明顯重複
2. 支柱分配比例是否大致符合 content_style.md 裡的權重（不需要完全精確，但不能明顯失衡，例如某支柱應該只佔 10% 卻排了 4 天）
3. 一週 7 則 caption 之間是否太過雷同（句型、開頭方式重複）
4. 每個 draft_prompt 是否確實涵蓋了 SEXY_SCENE_LIBRARY.md 的 5 點檢查清單（皮膚質感/裝置規格/混合光源/背景雜物/完整服裝）

企劃草案：
${JSON.stringify(plan, null, 2)}

如果有問題，回傳 approved:false，列出具體問題（issues），並給出清楚的修正指示（revision_instructions）給下一輪重新規劃使用。如果沒問題，回傳 approved:true。`,
      { phase: 'Review', label: `review:${koId}:${weekStartDate}:r${revisions}`, schema: REVIEW_SCHEMA }
    )

    if (reviewResult.approved || revisions >= maxRevisions) break

    log(`${koId} ${weekStartDate}：第 ${revisions + 1} 輪審核未通過，重新規劃。問題：${reviewResult.issues.join('; ')}`)

    plan = await agent(
      `請根據以下審核意見，重新規劃虛擬 KOL「${koId}」${weekStartDate} 那週的內容企劃：
審核意見：${reviewResult.revision_instructions}
發現的問題：${reviewResult.issues.join('; ')}

原本的草案：
${JSON.stringify(plan, null, 2)}

請產出修正後的完整 7 天企劃，格式跟原本一樣（day/platform/pillar/scene/format/caption/draft_prompt/needs_manual_video_edit），確實解決上面提到的問題。`,
      { phase: 'Plan', label: `replan:${koId}:${weekStartDate}:r${revisions + 1}`, schema: WEEK_PLAN_SCHEMA }
    )
    revisions++
  }

  phase('Finalize')
  await agent(
    `請把這份已經審核通過的虛擬 KOL「${koId}」${weekStartDate} 那週內容企劃寫入檔案：

1. 寫一份人類可讀的 markdown 到 kols/${koId}/content_calendar/${weekStartDate}.md（如果資料夾不存在就建立），用表格列出 day/platform/pillar/scene/format/caption/是否需人工後製，並附上每天的完整 draft_prompt 供後續生成使用。
2. 寫一份結構化 JSON 到 kols/${koId}/content_calendar/${weekStartDate}.json，內容就是這份企劃資料本身，供之後其他自動化流程（例如生成或排程）讀取使用。
3. 更新（或建立）kols/${koId}/content_history.json——把這一週用過的 pillar 和 scene 主題追加進去（保留最近 8 週的紀錄即可，太舊的可以移除），供未來規劃時比對防止重複。

企劃內容：
${JSON.stringify(plan, null, 2)}`,
    { phase: 'Finalize', label: `finalize:${koId}:${weekStartDate}` }
  )

  log(`${koId} ${weekStartDate} 那週的企劃已完成並寫入檔案，經過 ${maxRevisions >= 1 ? '至多 ' + (maxRevisions + 1) + ' 輪' : '1 輪'}審核。`)
}

return { koId, weekStartDate, plan, reviewResult }
