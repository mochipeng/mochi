# Spotify "In Rotation" — Research Synthesis

## Research Overview

**Timeline:** 3-day explorative sprint  
**Methods:** Semi-structured interviews, contextual inquiry  
**Sample Size:** 5 participants  
**Recruitment:** Convenience sampling (musicians, casual listeners, Spotify users)

---

## Participant Profiles

| ID | Role | Context | Key Insight |
|----|------|---------|-------------|
| P1 | Independent Artist | Makes music, 2K followers | "I don't have time to curate playlists" |
| P2 | Music Enthusiast | Casual listener, follows artists | "I want to know what real artists listen to, not what labels want them to like" |
| P3 | Content Creator | TikTok creator using Spotify API | "Anything that adds friction, artists won't adopt" |
| P4 | Artist Manager | Manages 3 mid-tier artists | "Our artists get 50+ playlist requests a week—they're not adding another task" |
| P5 | Devoted Fan | Follows 15+ artists closely | "I'd pay to see what [artist] actually listens to" |

---

## Research Questions & Findings

### RQ1: How do artists currently share what they're listening to?

**Finding:** Artists don't systematically share listening habits.

**Evidence:**
- P1: *"I share music in Discord with close friends, but not on a platform"*
- P3: *"Most artists I work with use Instagram Stories if they share anything at all"*
- P4: *"We've tried artist playlists before—they got neglected after 3 weeks"*

**Implication:** Passive/automatic sharing > active curation.

---

### RQ2: What prevents artists from curating public playlists?

**Finding:** Curation carries hidden costs: effort, perfectionism, maintenance burden.

**Evidence:**
- P1: *"I don't want to maintain another playlist. I barely update my bio."* (effort)
- P4: *"Artists worry every playlist choice is judged. It's anxiety."* (perfectionism)
- P3: *"If a playlist isn't updated regularly, it signals abandonment. Nobody wants that."* (maintenance burden)

**Implication:** Features requiring ongoing effort will have <20% adoption. Design for automation.

---

### RQ3: What do fans actually want from artists' taste signals?

**Finding:** Authenticity > polish. Fans want a window into real listening, not curated PR.

**Evidence:**
- P2: *"I'd rather see their actual Spotify Wrapped than a cute playlist they made for photo ops"*
- P5: *"Is this really what they listen to, or is their label telling them to promote this?"*
- P2: *"The most interesting artists are the ones who share random taste—shows their depth"*

**Implication:** Algorithm-selected (from real listening history) > manually curated (feels manufactured).

---

### RQ4: What's the minimal viable context for taste sharing?

**Finding:** Optional context is better than required. Less is more.

**Evidence:**
- P1: *"If I have to write liner notes, I'm not doing it. A one-liner? Maybe."*
- P2: *"I don't need explanations. Let me discover the music."*
- P5: *"Honestly, just show me the tracks. If it's good, I'll listen."*

**Implication:** Optional single-line context. Better to have none than force anything.

---

### RQ5: Would artists use a feature that auto-generates their taste?

**Finding:** Yes, with strong caveats about control and visibility.

**Evidence:**
- P1: *"If it's automatic and I can delete stuff that makes me look bad, yeah"*
- P3: *"Artist adoption would jump 80% if it was default-on with blacklist"*
- P4: *"Artists would use this if they feel they own it — can turn off, pause, whatever"*

**Implication:** Design for artist autonomy. Blacklist > no control. Toggle on/off > required participation.

---

### RQ6: What operational risks concern you?

**Finding:** Without safeguards, community features lead to moderation nightmares.

**Evidence:**
- P4: *"Comments or likes on a playlist? We'd need a whole moderation team."*
- P3: *"Fan wars around music taste get toxic fast. Spotify has a trust problem there."*
- P2: *"I've seen artists get roasted for their taste — they deserve privacy"*

**Implication:** Avoid community features. No comments, ratings, or public discourse. Self-contained.

---

## Synthesis: Core User Needs

### For Artists:
1. **Low effort** — Can't require manual work
2. **Autonomy** — Control when/what/if shown
3. **Authenticity** — Reflects real listening, not performed taste
4. **Safety** — No harassment or public judgment

### For Fans:
1. **Authentic signals** — Real listening, not marketing
2. **Discoverability** — Find new music through trusted sources
3. **Connection** — Feel closer to artists
4. **Simplicity** — Easy to understand and use

---

## Key Contradictions Resolved

| Tension | Resolution | Why |
|---------|-----------|-----|
| Artists want to share but don't want to work | Auto-generation + optional customization | Removes friction, keeps agency |
| Fans want transparency but artists guard privacy | Show listening, not personal details | Safe disclosure for both |
| Need fresh content but avoid maintenance burden | Weekly auto-refresh from 30-day history | Automatic + predictable |
| Want community but avoid moderation complexity | No comments/ratings, music-only | Eliminates toxicity vectors |

---

## Recommendations for Design

### ✅ DO:
- Auto-generate from listening history
- Make opt-in, but default on after notification
- Allow blacklist + pause controls
- Show timestamp ("Updated 2 days ago")
- Keep it lightweight (3–5 tracks, no context required)
- Surface in non-intrusive locations (modal, mini-player)

### ❌ DON'T:
- Require manual curation
- Force required fields (comments, descriptions)
- Add community features (comments, likes, shares)
- Update too frequently (confusing) or too rarely (stale)
- Make it feel like promotional content
- Expose artists to public judgment

---

## Research Limitations & Future Work

**Limitations:**
- Small sample (N=5) — directional, not definitive
- Convenience sampling bias — participants self-selected interest
- No quantitative validation — findings are qualitative insights
- Hypothetical scenario — participants reacting to idea, not shipping product

**Future Research:**
- Validate with 20+ artists across genres/follower count
- Test different refresh frequencies (weekly vs. bi-weekly)
- Prototype fidelity study — does auto-generation feel authentic?
- Longitudinal study — do artists actually use this 6+ months in?
- Fan preference testing — would they engage with In Rotation?

---

## Quotes & Memorable Moments

> *"I don't want to maintain another playlist. I barely update my bio."*  
> — P1, Independent Artist

> *"If it's automatic and I can delete stuff that makes me look bad, yeah."*  
> — P1, when asked about auto-generation

> *"I'd rather see their actual Spotify Wrapped than a cute playlist they made for photo ops."*  
> — P2, Music Enthusiast

> *"Artist adoption would jump 80% if it was default-on with blacklist."*  
> — P3, Content Creator / API expert

> *"I'd pay to see what [artist] actually listens to."*  
> — P5, Devoted Fan (emotional validation)

---

## Next Steps

1. **Prototype validation** — Show interactive prototype to 5 new participants
2. **Operational assessment** — Model moderation/scaling concerns with Spotify ops team
3. **Technical feasibility** — Verify listening history API accessibility
4. **Measurement framework** — Define success metrics pre-launch
5. **Competitive analysis** — How are Apple Music, Amazon Music approaching this?
