export const meta = {
  name: 'kol-content-qa-pipeline',
  description: 'Review-generate-critique pipeline for KOL AI image/video batches, enforcing the anti-"AI look" checklist before and after generation, flagging video for manual editing, and archiving approved assets to Google Drive',
  whenToUse: 'Run when actually generating AI images or videos for a KOL persona batch (pulled from that persona\'s generation_notes.md or a weekly_content_planner output). Reviews each prompt against the studio\'s 5-point anti-"AI look" checklist (see SEXY_SCENE_LIBRARY.md), generates the asset, and either: (a) for images/no-edit-needed video, critiques for AI-look tells and retries with a targeted fix up to maxRetries, or (b) for video marked needs_manual_video_edit, generates the raw asset and routes it straight to human post-production (per DAILY_VIDEO_SOP.md/DANCE_VIDEO_SOP.md — BGM/editing is a known manual step) instead of looping on auto-critique. Approved assets get uploaded to Google Drive and generation_notes.md is updated with real results.',
  phases: [
    { title: 'Prompt Review', detail: 'Check each draft prompt against the 5-point checklist and fix gaps before spending generation credits' },
    { title: 'Generate', detail: 'Call the Higgsfield image/video generation tool with the reviewed prompt' },
    { title: 'Quality Critique', detail: 'Vision review for AI-look tells (images / no-edit video only); video needing manual edit skips straight to that status' },
    { title: 'Finalize', detail: "Upload approved assets to Google Drive and update the persona's generation_notes.md with the real results" },
  ],
}

// args shape:
// {
//   koId: 'vicky-lin',
//   batches: [
//     { id: 'batch5', scene: '晨間鏡前綁頭髮', prompt: '...', format: 'image' },
//     { id: 'batch6', scene: '週三熱梗舞', prompt: '...', format: 'video', needs_manual_video_edit: true },
//   ],
//   maxRetries: 2,          // optional, defaults to 2
//   runTimestamp: '2026-07-24', // optional, stamp to record in generation_notes.md — pass in, don't invent one
//   driveFolderId: '...',   // optional Google Drive folder id to upload approved assets into — if omitted, agent picks/creates a per-KOL folder and reports its id
// }

const koId = args && args.koId
const batches = (args && args.batches) || []
const maxRetries = args && args.maxRetries != null ? args.maxRetries : 2

const PROMPT_REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    passed: { type: 'boolean' },
    finalPrompt: { type: 'string' },
    fixesApplied: { type: 'array', items: { type: 'string' } },
  },
  required: ['passed', 'finalPrompt', 'fixesApplied'],
}

const GENERATION_RESULT_SCHEMA = {
  type: 'object',
  properties: {
    success: { type: 'boolean' },
    imagePath: { type: 'string' },
    jobId: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['success', 'imagePath', 'notes'],
}

const CRITIQUE_SCHEMA = {
  type: 'object',
  properties: {
    approved: { type: 'boolean' },
    aiLookIssues: { type: 'array', items: { type: 'string' } },
    fixInstruction: { type: 'string' },
  },
  required: ['approved', 'aiLookIssues', 'fixInstruction'],
}

const CHECKLIST_TEXT = `1. 皮膚質感關鍵字（毛孔、自然紋理、不打磨、不 airbrushed）
2. 具體拍攝裝置/鏡頭規格（不只是「shot on iPhone」，要有裝置特有的破綻描述：對焦、過曝、動態模糊、壓縮痕跡）
3. 混合/不均勻光源配方（不是乾淨棚拍光，要有色溫混合、不均勻衰減）
4. 具體生活雜物背景細節（不是只寫地點名稱，要有具體雜物）
5. 服裝完整明確寫出（不留給模型自己猜）`

if (!koId) {
  log('未提供 koId，跳過執行（這是安全的空跑，用於驗證流程結構）')
}

const results = await pipeline(
  batches,
  async (batch) => {
    const review = await agent(
      `你在審核一個要送進 AI 圖片生成的 prompt，目的是避免浪費生成資源在品質不合格的 prompt 上。
角色：${koId}。場景：${batch.scene || batch.id}。
原始 prompt：
"""${batch.prompt}"""

請對照這 5 項檢查清單（出自 SEXY_SCENE_LIBRARY.md「降低 AI 感的技術要點」）：
${CHECKLIST_TEXT}

如果有缺漏，直接重寫 prompt 補上缺漏的部分——不要只是說明缺什麼，要給出可以直接使用的完整修正版 prompt。回傳最終可用的 prompt、原本是否就通過、以及做了哪些修正。`,
      { phase: 'Prompt Review', label: `review:${koId}:${batch.id || batch.scene}`, schema: PROMPT_REVIEW_SCHEMA }
    )
    return { ...batch, reviewedPrompt: review.finalPrompt, reviewPassed: review.passed, fixesApplied: review.fixesApplied }
  },
  async (reviewedBatch) => {
    const isVideo = reviewedBatch.format === 'video'
    const generation = await agent(
      `用可用的 Higgsfield ${isVideo ? '影片' : '圖片'}生成工具（用 ToolSearch 找 mcp__higgs__generate_${isVideo ? 'video' : 'image'} 或同等工具）生成${isVideo ? '一支影片' : '一張圖片'}，prompt 如下：
"""${reviewedBatch.reviewedPrompt}"""
角色：${koId}，場景：${reviewedBatch.scene || reviewedBatch.id}。
如果這個角色在 kols/${koId}/profile.json 裡已經有 soul_id（identity.appearance.ai_generation 或類似欄位），優先使用該 soul_id 生成以維持角色一致性；如果還沒有 soul_id，就用純文字 prompt 生成，並在 notes 裡註明「無 soul_id，僅文字生成」。
${isVideo ? '影片生成請參考 DAILY_VIDEO_SOP.md / DANCE_VIDEO_SOP.md 裡記錄的已知限制（例如 generate_audio 設定、multi_shot_mode 等），照那邊的規則設定參數。' : ''}
生成完成後，把${isVideo ? '影片' : '圖片'}下載/儲存到本機 kols/${koId}/${isVideo ? 'videos' : 'images'}/ 對應子資料夾（檔名清楚標示場景，不要用時間戳當檔名，時間戳交給後續 Finalize 階段記錄），回傳實際存檔路徑、job ID、以及是否成功。`,
      { phase: 'Generate', label: `generate:${koId}:${reviewedBatch.id || reviewedBatch.scene}`, schema: GENERATION_RESULT_SCHEMA }
    )
    return { ...reviewedBatch, generation }
  },
  async (generatedBatch) => {
    let current = generatedBatch
    if (!current.generation.success) {
      return { ...current, finalStatus: 'generation_failed' }
    }
    // Video needing manual post-production (BGM/editing) skips auto-critique entirely —
    // per DAILY_VIDEO_SOP.md/DANCE_VIDEO_SOP.md, that step is a known non-automatable gap,
    // not something to loop on or pretend to approve.
    if (current.format === 'video' && current.needs_manual_video_edit) {
      return { ...current, finalStatus: 'needs_manual_edit' }
    }
    let tries = 0
    while (tries <= maxRetries) {
      const critique = await agent(
        `請用 Read 工具開啟這個素材檔案來看內容：${current.generation.imagePath}
這是虛擬角色「${koId}」的生成素材，場景設定：${current.scene || current.id}。
請檢查有沒有明顯的「AI 感」破綻：皮膚過度平滑/塑膠感、手指或肢體變形、臉部與背景光源不一致、構圖過於對稱工整、背景太乾淨沒有生活感。
回傳是否通過（approved）、發現的問題清單、以及如果不通過，給出具體要怎麼修正 prompt 的建議（用於下一輪重新生成）。`,
        { phase: 'Quality Critique', label: `critique:${koId}:${current.id || current.scene}:try${tries}`, schema: CRITIQUE_SCHEMA }
      )
      if (critique.approved) {
        return { ...current, critique, finalStatus: 'approved' }
      }
      tries++
      if (tries > maxRetries) {
        return { ...current, critique, finalStatus: 'needs_human_review' }
      }
      log(`${koId} / ${current.scene || current.id}：第 ${tries} 次重試，修正方向：${critique.fixInstruction}`)
      const regen = await agent(
        `重新生成，套用這個修正：${critique.fixInstruction}
原本的 prompt：
"""${current.reviewedPrompt}"""
角色：${koId}，場景：${current.scene || current.id}。用可用的 Higgsfield 生成工具生成，下載存檔後回傳路徑、job ID、是否成功。`,
        { phase: 'Generate', label: `regenerate:${koId}:${current.id || current.scene}:try${tries}`, schema: GENERATION_RESULT_SCHEMA }
      )
      current = { ...current, generation: regen }
    }
    return current
  }
)

const approved = results.filter(Boolean).filter(r => r.finalStatus === 'approved')
const needsManualEdit = results.filter(Boolean).filter(r => r.finalStatus === 'needs_manual_edit')
const needsReview = results.filter(Boolean).filter(r => r.finalStatus === 'needs_human_review')
const failed = results.filter(Boolean).filter(r => r.finalStatus === 'generation_failed')

log(`完成：${approved.length} 個通過，${needsManualEdit.length} 個需人工後製，${needsReview.length} 個需要人工複查，${failed.length} 個生成失敗`)

// Approved (ready-to-post) AND needs_manual_edit (raw footage a human still has to cut) both get
// archived to Drive — the manual-edit ones just get a clear marker so nobody mistakes raw footage
// for a finished post.
const toArchive = [...approved, ...needsManualEdit]

if (toArchive.length > 0 && koId) {
  const uploadResult = await agent(
    `請把這些生成完成的素材上傳到 Google Drive（用 ToolSearch 找 mcp__Google_Drive__* 工具）。
${args && args.driveFolderId ? `目標資料夾 id：${args.driveFolderId}` : `沒有指定資料夾 id——請先搜尋/確認是否已有名為「${koId}」的資料夾，沒有就建立一個，並回報你用的資料夾 id。`}
需要上傳的素材：
${JSON.stringify(toArchive.map(r => ({ scene: r.scene || r.id, path: r.generation.imagePath, status: r.finalStatus })), null, 2)}
對於 status 是 needs_manual_edit 的素材，上傳時檔名或說明請清楚標註「待後製」，不要跟已核准可直接發布的素材混在一起看不出差別。
回傳每個素材實際上傳後的 Drive 檔案連結/id，以及最終使用的資料夾 id。`,
    { phase: 'Finalize', label: `drive-upload:${koId}` }
  )
  log(`${koId}：已上傳 ${toArchive.length} 個素材到 Google Drive`)

  if (approved.length > 0) {
    await agent(
      `請把這些已核准的生成結果，更新進 kols/${koId}/generation_notes.md 對應的批次紀錄裡（把該批次從 PENDING 改成實際結果，記錄真實的 job ID、素材路徑、Google Drive 連結；時間戳請用下面提供的 runTimestamp，不要自己猜測或編造日期，若沒提供就寫「時間戳待補」）。
已核准批次資料：
${JSON.stringify(approved.map(r => ({ scene: r.scene || r.id, prompt: r.reviewedPrompt, path: r.generation.imagePath, jobId: r.generation.jobId })), null, 2)}
Google Drive 上傳結果：${JSON.stringify(uploadResult)}
runTimestamp: ${args && args.runTimestamp ? args.runTimestamp : '(未提供，請在檔案中標註「時間戳待補」)'}
只更新這些批次對應的內容，不要動到檔案裡其他章節或其他批次。`,
      { phase: 'Finalize', label: `finalize:${koId}` }
    )
  }
}

return {
  koId,
  approvedCount: approved.length,
  needsManualEditCount: needsManualEdit.length,
  needsReviewCount: needsReview.length,
  failedCount: failed.length,
  results,
}
