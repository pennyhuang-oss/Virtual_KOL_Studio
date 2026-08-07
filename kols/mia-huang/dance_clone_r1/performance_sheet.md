# Performance Sheet — Mia Huang, Dance Clone R1 (Method B)

**KOL:** Mia Huang (soul_id `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`)
**Driver:** IG Reel `DPWE2eqEVJ-`, 576×1024, fixed camera, single continuous shot, ~9.8s, ~96 BPM
**Outfit:** navy sailor-uniform playsuit + white sailor cap + grey over-knee socks + black mary-jane heels (cosplay-lite category)
**Stage:** pre-Step-4 consultation — start frame not yet generated
**Standards applied:** `docs/07-kol-performance-realism-standard.md` (R1–R5, §C.1–C.3), `docs/05` (dance archetypes/turntable-groove taxonomy), `DANCE_CLONE_SOP.md` (Method B pipeline, §C.0/H.2 framing rules)

---

## 0. Correction to the brief before we go further

Character.md / profile.json establish Mia's hair as **dyed ash-brown, worn LONG with a loose wave**, pink money-piece streak on one side — not short. This matters for R1: long hair worn down is a *better* secondary-motion carrier than short hair (more mass, more visible lag). Do not shorten it for this clip. The wardrobe/hair-wheel rule in `content_style.md` ("長微捲放下／粉色挑染固定不變") already selects this as one of five valid hairstyle slots — pick it deliberately for this dance, not a bun/ponytail/half-up, all of which would kill the one hair-based R1 carrier we have.

---

## 1. Movement quality

- **Force profile:** Predominantly **smooth/groove**, not sharp/hit-based. The driver has no karate-chop isolations — it's walk → open-arm poses → settle. Two moments read as near-hits and should be treated as the sharp accents: the **cap-adjust pop at 4.0s** (hands snap up, brief hold) and the **overhead reach at 7.0s** (arm extends and holds a beat before releasing). Keep the rest smooth so these two don't get drowned out — restraint elsewhere is what makes them read as intentional accents rather than random.
- **Weight/centre of gravity:** Starts grounded and forward-leaning (0.0s, weight into the supporting hand), shifts laterally step-to-step during the 2.0s walk, becomes more vertical/open through 4.0–7.0s, and settles onto **one hip** at 8.0s (classic weight-release close). This is a legible, real weight-transfer arc — don't flatten it into upright-the-whole-time, that's the single biggest "AI stiffness" tell for a walking beat.
- **Bounce amplitude:** Low–moderate. Nothing in the sampled frames suggests a vertical bounce/pulse on the beat (this isn't a bounce-heavy groove like `docs/04`'s Glam-sway archetype). **Do not add bounce that isn't in the driver** — per the realism standard's "restraint over amplitude" principle, amplifying beyond the source increases breakdown risk without adding believability.

## 2. Secondary motion (R1) — carrier analysis for this specific outfit

**Direct answer to Q1:** Hair is a real carrier; the outfit as literally described is not — but it very likely already contains one that's simply missing from the brief's wording.

| Candidate | Verdict | Why |
|---|---|---|
| **Long ash-brown hair + pink streak, worn down** | ✅ Usable R1 carrier | Character-canon length + loose wave gives real mass. Must be *visible outside the cap* (framed around the nape/sides, not fully tucked up) or it contributes nothing. Delay ~3–5 frames (≈0.1–0.17s) behind head-turn/stop moments; settles ~4–6 frames after the body stops at 8.0s→9.8s. |
| **Sailor collar ribbon/necktie** | ⚠️ Conditional — likely already exists, must be named explicitly | You noted the driver's "sailor collar ribbons swing a lot." Since Mia's playsuit is specified as *the same navy sailor-uniform playsuit... as in the driver clip*, the collar tie is almost certainly part of that same garment design — real sailor uniforms carry this by default. **The risk is losing it silently**: if the Step 4 image prompt only says "navy sailor-uniform playsuit + white sailor cap + grey over-knee socks + black mary-jane heels" without naming the collar ribbon, the image model may render a flat/fused collar with no loose tie. Write it into the prompt explicitly: *"sailor collar with a loosely knotted ribbon tie hanging free at the chest, ribbon ends not tucked or fused to the bodice."* This is a chest-height carrier, which is valuable because it's readable even in a tighter crop where hem-level movement (socks, playsuit leg opening) would be cropped out. |
| Sailor cap | ⚻ Minor/passive | The cap itself won't sway on its own, but the **cap-adjust gesture at 4.0s** gives it one moment of motion (hands touching brim, cap tilting slightly). If it has any small element (strap, small bow/badge), that can carry a beat of secondary lag right at that gesture. Not required, but free if included. |
| Grey over-knee socks, mary-jane heels | ❌ No motion contribution | Rigid/fitted, no fabric to sway. Fine as-is — they're not expected to carry R1, don't force it. |
| Playsuit hem itself | ❌ No motion contribution | A fitted playsuit has no loose hem or pleats. If you want a *second* torso/hip-level carrier beyond the collar ribbon (useful because hip weight-shift at 8.0s is a real driver beat with nothing currently set up to react to it), consider a small optional add: a short detachable pleated underskirt panel layered over the playsuit shorts — common in sailor cosplay-lite styling, stays within the established wardrobe category, and gives the hip-shift something visible to swing. **This is an enhancement, not a blocker** — the collar ribbon + hair combination is already sufficient to pass §C.3's R1 check. |

**Blocking condition (conditional, not unconditional):** This wardrobe only clears the R1 bar if **both** of the following are true in the actual Step 4 prompt and generation: (a) hair is worn down/visible past the cap, not tucked/bunned, and (b) the collar ribbon is explicitly named as a loose, untucked tie. If either is dropped, this outfit becomes exactly the "rigid, fully-synchronised" wardrobe the standard says to reject — treat losing both as a hard blocker requiring re-prompt before Step 5.

## 3. Breathing and pauses

- **0.0–1.0s (entrance):** Inhale held through the lean-forward, hand-resting pose — a "settled, about to move" stillness, not a frozen one (eyes/mouth still have micro-movement per R2, that's the emotion-director's lane, but the body should read as loaded, not dead).
- **~1.0–2.0s:** Soft exhale releases into the first step — weight leaves the resting hand.
- **~4.0s (cap adjust):** Small inhale/held-breath micro-beat exactly at the cap touch — this is the "hit" moment, comedic/cute in tone (matches Mia's chat-facing personality), release immediately after into the smile.
- **~5.0–6.0s (arms open → singing/laughing):** Exhale outward through the open-arm pose into the mouth-open beat — this is a chest-opening breath, not a gasp.
- **~7.0s (overhead reach):** Inhale as the arm lifts (expansion reads more natural on an inhale), controlled exhale through the pursed-lip hold.
- **~8.0s (weight to one hip, confident smile):** Full exhale/release — this is the emotional "landing" of the phrase, shoulders should visibly drop half an inch, not stay locked.
- **9.0–9.8s (settle):** Shallow, natural breathing resumes, no dramatic final inhale — a big breath here would read as a performance being wound down for camera rather than a person naturally settling, which undercuts the "caught mid-life, not posed" quality Mia's brand voice depends on.

## 4. Camera relationship (R5)

### Framing recommendation for the start frame (Q2)

This driver is fuller-body than a typical waist-up dance clip (0.0s is head-to-feet, 2.0s is a walking/stepping beat that needs legs, 5.0s is a wide symmetric arm-spread that wants room). Two competing pulls:

- `docs/07` §C.1 default is waist-up (60–75% frame fill) for R2/R5 legibility.
- `DANCE_CLONE_SOP.md` §H.2 says dance content specifically should default to **mid-thigh-up (three-quarter/三分身)** because waist-up crops away the torso sway that carries R1 — and that's *before* accounting for this driver's walking beat.

**Recommendation: mid-thigh-up (three-quarter), not full-body, and not tight waist-up.** Reasoning:
- Full body would shrink Mia's face too much for R2 micro-expression legibility (this driver has real expression variety across the timeline — cap-adjust smile, open-mouth singing, pursed lips, confident smile — worth preserving at readable size).
- Waist-up would crop the walking legs at 2.0s and the hip weight-shift at 8.0s, losing two of the driver's more legible weight-transfer beats.
- Mid-thigh-up keeps the collar-ribbon and hair (chest/upper-body carriers) fully visible, keeps hip-level movement legible, and crops out feet/ankle detail — which, per Q3 below, is actually a *risk-reduction* side effect, not just a framing compromise.
- Adapt the entrance pose's anchor gesture (0.0s hand resting on a bench) to an equivalent surface at the right height for a mid-thigh crop — e.g., hand resting on the top of the gaming chair's backrest, or on the desk edge — rather than trying to preserve "full body head-to-feet" for that one beat. Don't chase the driver's exact crop; adapt the *gesture*, not the literal framing, to this shot's crop.

### Handheld sway

The driver is a **fixed camera** — it will not contribute any camera-life to the final clip, because `scene_control="image"` means the camera behavior in the output comes from Mia's own generated scene, not from the driver. If you generate this with a dead-still locked-off camera, you lose R5 entirely regardless of how good the body performance is. **Explicitly prompt for subtle handheld drift** — small, slow, non-repeating sway, roughly 2–4% of frame width/height, no pans or zooms. This is an add, not a copy-from-driver instruction.

### Subject distance & lean-toward-camera moments

Default: mid-thigh-up per above. Two natural lean-toward-camera opportunities that also reinforce Mia's established "talks straight to the lens like it's chat" trait:
- **0.0–1.0s entrance:** the driver's forward lean can be read as a lean-in toward camera/monitor, playing as a conspiratorial "come here" address to chat — very on-brand.
- **8.0s close:** confident smile + weight on one hip is a natural second beat for a slight lean-in, closing the phrase on direct eye contact rather than a static stance.

### Staging & collision risk with the streaming room (Q4)

**Yes, there is a real collision risk, and it needs to be handled at Step 4, not fixed later.** The 2.0s beat is a walking/stepping motion with arms swinging out to the sides — that needs open lateral floor space to read cleanly. A gaming-den start frame with desk + monitors + chair packed tightly around the subject (which is exactly how Mia's established streaming-room scenes are usually composed — close, cluttered, intimate) will either:
- visually clip the subject's swinging arms through the monitor/desk edge, or
- make the walking motion look like she's stepping *into* furniture that doesn't move with her (since in `scene_control="image"`, the background environment is static/rendered from the reference image while only the body is driven — a moving body against a static tight-packed background is exactly where "walked into the desk" artifacts happen).

**Staging fix for the start frame composition:**
- Position her with clear open floor to at least one side (e.g., between the chair and the collectible shelf, with the desk kept to the rear/side rather than directly in her stepping path) rather than the tight desk-facing framing typical of her sitting content.
- Keep the gaming chair as a background/anchor element (good for the 0.0s hand-resting substitute gesture) but not directly in the lateral path implied by the 2.0s step.
- If in doubt, err toward slightly more negative space around her than a typical Mia streaming-room shot — this is a dance clip, not a reaction-face clip, and the room needs to serve the movement rather than the movement needing to dodge the room.
- **GG the cat:** recommend leaving him out of this particular start frame, or including him only as a static/sleeping background element. Motion Control drives the subject's body from the driver skeleton; a cat is not part of that skeleton and has no equivalent motion source, so an "active" cat in frame during a body-driven clip is asking the model to invent motion for it with nothing to anchor it — added AI-tell risk for a payoff (cuteness) that belongs better in a separate reaction-style clip where he can be the whole point of the shot.

## 5. Hand-crossing / Kling-risk moments (Q3)

| Time | Moment | Risk | Note |
|---|---|---|---|
| 2.0s | Feet crossing mid-stride | **High** — crossed/overlapping legs and feet are a classic merged-limb failure zone, worse at lower resolution | Mid-thigh-up framing (see §4) crops out the feet/ankle detail, which reduces — though doesn't eliminate — exposure to this specific failure mode. If a full-body cut is ever wanted for this beat, plan on a dedicated cut-in rather than forcing the whole clip wide. |
| 4.0s | Both hands raised behind head adjusting cap | **Medium-high** — hands overlapping hair + cap near the head is a common finger/occlusion failure zone | Keep this beat brief; don't let hands linger fused against the cap for multiple seconds. |
| 6.0–7.0s | One hand near face/cap while other arm reaches overhead | **Medium** — hand near face increases finger-distortion and mouth-occlusion risk | Watch this frame range specifically in QA; if fingers deform, it's usually here. |
| 8.0s | Hand grazes bench edge (→ desk/chair edge in Mia's version) | **Medium** — hand-to-surface contact points are a known deformation zone | Make sure the equivalent surface (desk edge/chair back) is positioned so the hand only lightly grazes it in the start frame, not gripping/wrapping around an edge, which is harder for the model to hold correctly across frames. |
| 5.0s | Arms spread wide, palms out, symmetric | **Low** deformation risk, but a **taste/R3 flag**: this pose is explicitly symmetric. Per R3 and the taste standard, don't let the generation render it as a perfectly mirrored pose — keep a slight head tilt and asymmetric weight (even 5–10% off-centre) so it doesn't read as the "too-symmetric = AI" tell despite the driver's pose being technically symmetric. |

Standard §C.3 discipline applies regardless: run the freeze-frame +5-frame comparison at each of these moments once generated, and check hand/finger count and shape specifically at 2.0s, 4.0s, and 8.0s before calling this clip done.

## 6. Section structure

| Section | Time | Content |
|---|---|---|
| **Entrance pose** | 0.0–1.5s | Forward lean, hand resting on chair-back/desk-edge equivalent, calm direct-to-camera gaze — reads as "caught mid-moment," on-brand for Mia's fourth-wall-breaking habit |
| **Verse groove** | 1.5–4.0s | Walking/stepping beat, arms swinging loosely — this is the only real locomotion in the clip, keep weight transfer legible |
| **Build** | 4.0–5.0s | Cap-adjust hit (sharp accent) → smile release → arms open wide (breath-release beat) |
| **Chorus signature move** | 5.0–7.0s | Asymmetric arm spread + open-mouth singing/laughing → one arm reaching overhead + pursed-lip cute expression. **Treat this window as the memorable hook** — if this clip ever gets a dedicated cut-in/close-up insert, this is the range to use it on. |
| **Closing pose** | 7.5–9.8s | Arms lower, weight settles onto one hip, confident smile, gentle exhale into a natural stillness (not a held "ta-da" pose) |

## 7. Driver clip criteria (per `docs/05`/Method B selection standard)

Evaluating this specific driver against the selection bar:

- ✅ **Single continuous shot, no cuts** — meets the standard's preference; no discontinuity risk from mid-clip cut points.
- ✅ **Expression density over dance quality** — the sampled frames show real variety (calm gaze → smile → symmetric open smile → laughing/singing → pursed-lip cute → confident close), not one held expression stretched across 9.8s. This is exactly the "select for expression density" criterion `docs/05`/`07` both call out, not "select for impressive choreography."
- ⚠️ **Fixed camera** — acceptable for motion transfer, but as noted in §4, contributes zero camera-life to the output; compensate explicitly in generation prompting, don't assume it'll come from the driver.
- ⚠️ **No native audio-sync guidance given here** — confirm before Step 5 whether this Reel has usable music and what its actual BPM/beat grid is (96 BPM noted, but the sampled-frame timestamps above don't line up to obviously clean beat marks — re-verify against the real beat grid before treating 4.0s/5.0s/7.0s as "on the one").
- **Before Step 5:** run the standard's freeze-frame +5-frame test on the driver itself (not just the eventual output) — pause at 4.0s and 7.0s specifically (the two "hit" moments) and confirm the driver's own hair/collar keep moving into the following frames rather than stopping dead with the pose. If the driver itself freezes cleanly on these hits, that's fine (a real hit does still cause a brief true stop) — just confirm the *release* into the next beat isn't instant/synchronous across every visible element.

---

## Flags summary

1. **Conditional blocking (wardrobe/R1):** Outfit as literally worded has no swaying element. Fix is cheap — it likely already exists in the driver's own garment design — but it must be **written into the Step 4 prompt explicitly**: (a) hair worn down and visible past the cap, (b) sailor collar ribbon named as a loose, untucked tie. If either is dropped, re-prompt before Step 5.
2. **Framing decision needed:** Recommend mid-thigh-up (three-quarter), not full-body and not tight waist-up — balances R2 (face size), R1 (collar/hair visibility), and Q3's foot-crossing risk (crops it out) against the driver's need for visible hip/leg weight transfer.
3. **Staging risk (streaming room vs. 2.0s walking beat):** Desk/monitor/chair clutter typical of Mia's usual streaming-room compositions creates real collision/clip risk against the walking + arm-swing beat. Compose the start frame with genuine open floor space in the stepping direction; don't default to her usual tight desk-facing crop.
4. **GG the cat:** recommend excluding from this start frame, or static/sleeping only — an actively "present" cat has no motion source in a body-driven Motion Control generation and adds AI-tell risk for no performance benefit in this particular clip.
5. **R3 reminder at 5.0s:** the driver's symmetric arm-spread pose needs a deliberate asymmetry override (head tilt, slight off-centre weight) in generation — don't let a source pose that happens to be symmetric produce a symmetric-read result.
6. **No fixable-later R5 gap:** camera is fixed in the driver; handheld micro-sway must be added explicitly in the KOL's own generation, it will not come through motion transfer.
7. **Taste/scope:** nothing in this timeline crosses the sexy-but-elegant line (no crotch-focus, no low-angle, no exaggerated jiggle implied by any of the sampled poses) — no Part D taste conflicts identified, contingent on eye-level framing being maintained as planned.
