# Performance Sheet — Luna Tanaka「dance_clone_r1」(Method B)

**Date:** 2026-08-06
**Prepared by:** Performance Director
**Pipeline:** `DANCE_CLONE_SOP.md` Step 3 (motion-driven clone)
**Driver source:** Instagram Reel `DPWE2eqEVJ-` — off-shoulder ruffled crop top + high-waisted bottom, hotel-lounge setting, single continuous handheld/fixed shot, no cuts, ~15s, ~129 BPM (per `generation_notes.md` 2026-08-06 entry)
**KOL start frame (already generated, approved):** `kols/luna-tanaka/images/dance_clone_r1/start_frame.png` — oversized cream knit cardigan slipping off the shoulder(s) over a cream camisole + cream high-waisted shorts, Kyoto tatami apartment, low wooden table + old wooden window frame behind her. `scene_control="image"` will keep this wardrobe/background and borrow only the driver's body motion.
**Upstream standards:** `Buildup_KOL/docs/07` (R1–R5 realism mechanisms), `docs/05` §C.a/§D (section structure, taste rubric), `docs/04` (dance/lighting archetypes), this studio's `DANCE_METHOD_COMPARISON.md` (word-choice/NSFW note), `.claude/agents/performance-director.md` (local mandate incl. §3 framing-vs-torso)

> **Working caveat, read first:** everything below is built from a **text description sampled at 1.5s intervals** (~3.2 beats apart at 129 BPM), not frame-level video. Text at this resolution cannot confirm freeze points, exact hand paths, or whether the driver's own ruffle sleeves are genuinely desynchronised (vs. rigid). **Before Step 5, run the §7 "+5 frame" check on the actual `driver_cropped.mp4`.** Anything below marked "assumed" needs that confirmation.

---

## 0. Format anchor

| Item | Value |
|---|---|
| Duration | ~15.0s (last sampled beat at 13.5s + settle) |
| BPM | 129 → 1 beat = 60/129s = **0.465s** (≈11 frames @24fps / ≈14 frames @30fps) |
| Beats in clip | ~32 |
| FPS assumption | 24fps (this studio's typical Kling output per `DANCE_METHOD_COMPARISON.md`); rescale delay values ×1.25 if Step 5 outputs 30fps |
| Sampled-beat → beat-number map | 0.0s=beat 0 · 1.5s=b3.2 · 3.0s=b6.5 · 4.5s=b9.7 · 6.0s=b12.9 · 7.5s=b16.1 · 9.0s=b19.4 · 10.5s=b22.6 · 12.0s=b25.8 · 13.5s=b29.0 |

---

## 1. Movement quality

**Force (sharp vs. smooth):** the described choreography is mostly continuous/flowing (rotate, reach, spread, cross) rather than discrete hits. At 129 BPM — near the top of `docs/05`'s 100–130 BPM sweet spot — trying to land a sharp accent on every beat increases Kling's known motion-blur/limb-deformation risk. **Recommend 70% smooth / 30% sharp**, with the sharp fraction confined to the chorus block (6.0–9.0s): the top of the arm-spread (6.0s) and the diagonal point (7.5s) get a brief (~2–3 frame) hold at full extension; everything else stays smooth ease-in/ease-out.

**Weight / centre of gravity:** the sequence already gives natural weight shifts — hip-weighted stance at 0.0s, "weight shifts" at 7.5s, bounce at 9.0s. Keep these as the only weight-transfer moments; do **not** add a metronomic weight-shift on every beat, which reads as marching rather than dancing.

**Bounce amplitude:** 9.0s is explicitly called out as "more energetic bounce" — this is the clip's peak-energy beat and the only one with sustained vertical bounce. Keep it **moderate, not maximal** (restraint over amplitude is the standing principle): shoulders/torso lift with the beat, soft tissue settles in a single natural motion after each lift with no repeated secondary bounce, no framing or slow-motion choice that emphasises it. This satisfies both the taste standard (`docs/05` §D elegance axis) and this studio's content-filter word-choice rule — describe it in prompts as "torso lifts and settles naturally on the beat," never with body-part-specific dynamic phrasing.

---

## 2. Secondary motion (R1) — outfit verdict and per-beat substitution

**Wardrobe verdict: PASS, no wardrobe change required.** The oversized cream knit cardigan in the approved start frame is a valid R1 carrier — visibly loose, already draping past the wrists at rest, already slipping off the shoulder(s). This is good news relative to the default risk this role is supposed to flag (outfit with zero swaying element); that is **not** the case here.

**One correction to flag:** the brief describes the cardigan as "slipping off *one* shoulder," but the actual approved `start_frame.png` shows it already **off both shoulders** at rest (both hands on hips holding it open). This changes the substitution logic slightly — see below.

### 2.1 Fabric-physics substitution logic

The driver's ruffle sleeves are light chiffon-weight with structured frills: they produce **fast onset, multiple small ripples, quick settle** — a high-frequency flutter. Luna's cardigan is heavy oversized knit: it will produce **slower onset, a single large pendulum swing, slower settle** — a low-frequency drape. This is not a downgrade, it's a different (arguably more legible) physical signature, and it should be treated as its own carrier rather than an attempt to mimic ruffle-flutter timing.

| Element | Onset delay after the driving motion starts | Continues after motion stops | Full settle | Amplitude / character |
|---|---|---|---|---|
| **Cardigan sleeve** (oversized, past-wrist) | ~150–200ms (~0.35–0.45 beat) | 250–350ms, **single slow decay swing** (not multi-ripple like the ruffle original) | ~450–600ms after body stops | tip swings up to ~1.3× the wrist's own displacement |
| **Cardigan front/hem** (open, torso-length) | ~180–220ms | 300–400ms, drifts briefly opposite the torso's direction | ~500–650ms | moderate lateral drift, ≤ a hand's width |
| **Off-shoulder neckline** | ~200ms after a shoulder lifts/rotates | ~300ms after the shoulder returns | ~500ms | **subtle** — since it's already off both shoulders at rest, don't force a bigger "slip" event than the fabric would naturally do; an exaggerated slip beyond what's already established reads as artificial and risks pushing past the taste threshold |
| **Camisole strap** | ~80–100ms | ~150ms | minor, visible mainly in close crop | small |
| **Hair** (chin-length bob) | ~90–120ms (lighter/shorter = faster onset, smaller travel) | ~200–250ms | short | ends sway ≤15–20°, a **much smaller arc** than the driver's loose ponytail — see flag below |

**Flag — hair carrier diminished:** the driver's hair "swings with the motion" because it's a loose ponytail; Luna's chin-length bob physically cannot produce that arc. This is not blocking (the cardigan is the primary carrier and is sufficient on its own), but it reduces redundancy. Optional, non-required mitigation for a future regeneration: add one small piece of jewellery (drop earring or thin necklace) to the start frame as a second carrier.

### 2.2 Per-beat mapping (secondary motion at each described gesture)

| Beat | Gesture | Secondary-motion read |
|---|---|---|
| 0.0s | 3/4 stance, hand at waistband | static baseline — cardigan hangs at rest, nothing to time yet |
| 1.5s | Rotates to camera | cardigan hem/front swing opposite the rotation, catch up ~200ms after the turn completes |
| 3.0s | Peace sign near face | minimal — only the raised arm's sleeve responds, small and quick |
| 4.5s | Arm reaches forward/up, torso leans in | sleeve on the reaching arm streams back then follows the arm up; the off-shoulder edge on that side shifts slightly with the shoulder lift |
| 6.0s | **Both arms spread wide** | both sleeves swing outward/up, hair ends flick out (small arc), cardigan front panels fall open wider and swing — **this is the best available R1 verification window if there's any hold at full extension** |
| 7.5s | One arm diagonal, other forward | asymmetric sleeve response, left/right delay differing by ~50–80ms — this reinforces R3 (asymmetry) for free |
| 9.0s | **Arms cross at chest + bounce** | cardigan panels/sleeves converge toward centre; soft tissue settles once, per §1 wording discipline — **see §6 blocking flag: this beat's literal arm-crossing is a known Kling risk, independent of R1** |
| 10.5s | Hands clasp near chin/chest | arms are largely static here — sleeves drape down along forearms, main visible carrier is the cardigan hem still settling from beat 9.0s, plus hair settling |
| 12.0s | Hand near cheek, eyes closed | quiet beat, minimal secondary motion — good contrast beat, don't force movement here |
| 13.5s | Settling closing pose | cardigan hem/sleeve and hair must still be finishing their settle from the 10.5–12.0s beats into and past this pose — **the final frame of the whole clip must not show body, cardigan, and hair all stopped at once** |

---

## 3. Framing vs. torso trade-off — flagged, needs resolution before Step 5

I looked at the approved `start_frame.png` directly. It is framed **wider than the SOP's mid-thigh-up default** — the crop runs down to roughly the ankles/near-feet, and the **low wooden table sits directly in the foreground at hip height**, close enough that she is nearly leaning against it in the reference pose. `generation_notes.md` already flagged this composition deviation and deferred it to "check during Step 5," which I'm now escalating:

- **Physical collision risk:** this choreography has real weight-shift and lean moments (4.5s lean-in, 7.5s weight shift, 9.0s bounce). With the table this close in a full-body-to-feet frame, any body drift the motion transfer introduces risks reading as her clipping into/through the table.
- **Face-size cost:** the wider crop is *good* for R1 (full torso stays in frame, so cardigan-hem and weight-shift sway are all visible) but shrinks the face well below the ~12% "mid-thigh" target this studio's own comparison doc calls out as the dance-clip standard — worse for reading the coy/eyes-closed beats (10.5s, 12.0s) that depend on visible expression.
- Because this is a **single continuous shot with no cuts** (stated constraint), we cannot solve this the way the local agent spec's §3 suggests (cut between two framings per section) — there is only one framing for the whole clip.

**Recommendation:** re-crop or regenerate the start frame to **mid-thigh-up** (the SOP default), which simultaneously (a) removes the table from frame — solving the collision risk, and (b) brings the face proportion up to spec without sacrificing the torso sway R1 depends on. This is the single highest-leverage fix available before Step 5.

---

## 4. Breathing and pauses

| Beat | Event |
|---|---|
| 0.0–1.5s | **Inhale.** The calm neutral stance before she rotates and begins speaking/lip-syncing is the natural held-breath opening — don't have her already moving before this settles. |
| ~6.0s (top of arm-spread) | **Candidate freeze #1** — recommend confirming in the actual driver footage whether there's a hold at full extension. Not confirmed from the text description alone (see caveat, §0). |
| ~9.0s→10.5s transition | **Candidate freeze #2** — the shift from energetic bounce/cross into the quieter clasped-hands coy gesture is a natural place for a brief settle before the next beat starts. Confirm against actual footage. |
| 12.0s | **Exhale begins.** Eyes briefly closed, soft coy smile — shoulders should be visibly lower here than at the 9.0s peak. |
| 13.5s→end | **Release.** Head tilts back/up, closed-mouth smile, hand rests on hip — this is the full exhale and matches Luna's default quiet register well. Cardigan/hair must still be completing their settle here (see §2.2, last row). |

**Note on freezes:** the sampled description gives no explicit freeze/hold moment — the org's own SOP (§ "D7" in `docs/07`, and this studio's checklist) wants **≥2 genuine freezes ≥8 frames** as the R1 verification window. Without a confirmed freeze, the arm-direction-reversal moments (6.0s→7.5s, 9.0s→10.5s) are the fallback verification points, but they're weaker evidence than a true freeze. **Confirm this against the real driver clip before finalizing.**

---

## 5. Camera relationship (R5)

**Shot type:** single continuous handheld/fixed shot, no cuts (given constraint) — consistent with `content_style.md`'s brand voice: *"鏡頭穩定：非常穩，像她的性格一樣不急不晃"* (camera very stable, unhurried, matching her personality). This creates a real tension with the general realism mandate that a perfectly-still tripod shot is itself an AI tell (R5 requires *some* life in the camera). Resolution: keep handheld sway **present but small** — steadier than a typical energetic-KOL dance clip, but not mathematically zero. Recommend the low end of this studio's own established sway ranges (sub-1% frame-width drift, non-periodic, never locked to the beat grid) rather than omitting sway entirely.

**Subject distance:** tie to §3 — recommend locking to **mid-thigh-up** once the start frame is re-cropped. This is also this SOP's own stated default for dance content.

**Eye-level:** the approved start frame already sits at roughly chest/eye height on a 155cm subject — hold that height for the whole clip. No low-angle, no crotch-level framing (both would fail the taste standard regardless of how tame the choreography is).

**Lean-in moment:** 4.5s (arm reaches toward camera, torso leans in) is the one explicit, camera-directed moment in this sequence — this is the R5 highlight and should read clearly as her deciding to close distance with the lens, not the lens pushing in. Keep it inside the taste-standard bounds already satisfied by a mid-thigh (not tighter) crop.

**Open technical question to confirm at Step 5:** does `motion_control` with `scene_control="image"` also inherit the *driver's own camera path* (its handheld motion), or does it generate a fresh camera relative to Luna's reference image? If the former, the driver's actual handheld character (unknown — could be shakier "casual reel" handheld) may need reconciling with the stable-camera brand voice above; verify empirically before treating this section as final.

---

## 6. Section structure

| Section | Time | Content | Notes |
|---|---|---|---|
| **Entrance pose** | 0.0–1.5s | 3/4 stance, hand at waistband, weight on hip, calm neutral | On-brand — matches Luna's default quiet register well |
| **Verse groove** | 1.5–4.5s | Rotate to camera → peace sign near face → arm reach + lean-in toward camera | Peace sign is flagged below (persona tension, not a physics/taste issue); the 4.5s lean-in is the R5 highlight of the whole clip |
| **Chorus signature move** | 6.0–9.0s | Both arms spread wide → one-arm diagonal point (candidate hook/memory-point per `docs/05` §C.a) → arms cross at chest + energetic bounce | Highest-energy block; 7.5s's diagonal point is the best candidate for a repeatable, memorable "point" move if the actual footage loops it. **9.0s carries the hand-crossing flag, §7.** |
| **Bridge / cooldown** | 10.5–12.0s | Hands clasp near chin/chest with pursed-lips gesture → hand near cheek, eyes briefly closed | 10.5s flagged below (persona tension); 12.0s is strongly on-brand |
| **Closing pose** | 13.5s–end | Head tilts back/up, closed-mouth soft smile, hand rests on hip, settle | On-brand, clean close — ensure secondary motion is still resolving in the final frames (§2.2) |

---

## 7. Driver clip criteria (`DANCE_CLONE_SOP.md` Step 2/3 + `docs/07` §6)

Evaluated against what's confirmable from the text description alone. **PASS/FAIL** marked only where the description gives direct evidence; everything else is **UNKNOWN — verify on actual footage**.

| # | Criterion | Status | Basis |
|---|---|---|---|
| Single continuous shot, no cuts | ✅ PASS | Explicitly stated |
| Driver already has a swaying wardrobe element | ✅ PASS | Ruffle sleeves explicitly flutter on every arm movement |
| Hands stay off the body midline | ❌ **FAIL** | 9.0s: "arms come forward/crossing gesture at chest height" — explicit cross-body motion, a known Kling hand/finger-deformation risk this studio's own docs call out |
| ≥2 genuine freezes ≥8 frames | ⚠️ UNKNOWN | No freeze explicitly described at 1.5s sampling resolution (see §4) |
| Crop width — mid-thigh (preserves torso R1) vs. waist-up (kills it) | ⚠️ Needs decision | Original driver framing not described; when cropping the driver to single-person-centre 9:16 (Step 2), crop to **mid-thigh**, matching the KOL-side framing fix in §3 |
| Native fps, no slow-motion ramps | ⚠️ UNKNOWN | Not stated — check file metadata after download |
| Single person in frame throughout | ⚠️ Assumed (solo dance-reel format) | Verify no second person/mirror reflection |
| Eye contact with camera ≥60% of runtime | ⚠️ Likely, not confirmed | Multiple beats describe camera-directed smiles/gestures (1.5s, 3.0s, 4.5s, 6.0s, 7.5s) |
| No busy prints / plaid (moiré risk) | ⚠️ UNKNOWN | Ruffled top described plainly, no pattern mentioned — verify visually |
| No captions/logos over the body | ⚠️ UNKNOWN | Not stated |

**Mandatory pre-Step-5 action:** once `driver_cropped.mp4` exists, run the standard check — pause on any frame where the body fully stops, step forward 5 frames, and confirm the ruffle sleeves/hair have moved. If they haven't, this driver is rigid at its source and no amount of downstream work will add real R1 — it would need to be swapped for a different clip.

**Licensing note (Step 7, flagged for completeness, outside my core mandate):** this is a third-party Instagram Reel — internal validation use is fine per SOP, but external publish requires the Step 7 authorization check (own/licensed audio, motion altered enough to be non-identifiable or a proper reference).

---

## 8. Flags summary

**Blocking-adjacent — resolve before/at Step 5:**
1. **9.0s hand-crossing gesture** — explicit cross-body arm motion at the chorus peak, a known Kling failure mode. Either confirm the actual driver clip's crossing motion is mild enough to risk it (budget a mandatory hand-restoration pass on that segment), or treat it as a candidate trim point if the driver clip allows.
2. **Start-frame framing** — currently wider than mid-thigh-up, with the low wooden table intruding into the foreground at hip height right where this choreography's weight-shift/lean moments happen. Recommend re-crop/regenerate to mid-thigh before Step 5.
3. **No confirmed freeze** in the sampled description — need ≥2 genuine freezes in the real footage for a clean R1 verification window; confirm on actual video.

**Not blocking — outside my core mandate (R1/R5/shared-R3), flagged for Emotion Director / creative sign-off:**
- The peace sign (3.0s), the pursed-lips/blow-kiss-adjacent gesture (10.5s), and the big open-mouth smile with both arms spread wide (6.0s) sit outside Luna's default restrained, quiet emotional register — her own character bible lists exactly these (exaggerated cute gestures, kiss/heart poses, wide open-arm gestures) as atypical-but-not-forbidden. Nothing here is vulgar or a taste-standard violation (no crotch focus, no exaggerated jiggle, framing stays modest) — this is a **persona-fit** question, not a physics or taste-standard block. Recommend explicit sign-off that this clip intentionally plays in her rare "playful" register rather than this being an unreviewed default.

**Cleared, no action needed:**
- Wardrobe secondary-motion carrier (cardigan) — sufficient, no wardrobe change required.
- Taste standard (eye-level framing, no crotch-focus, no exaggerated jiggle) — nothing in the described choreography or the approved start frame violates this, provided the bounce/soft-tissue wording discipline in §1 is followed in the actual generation prompt.
