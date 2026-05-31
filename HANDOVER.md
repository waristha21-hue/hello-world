# Handover Note — Job → Claude Code
_Prepared: 2026-05-31_

---

## Who is Job?
- **Nickname:** Job
- **Role:** Sales Representative — Meditop Co., Ltd.
- **Industry:** Medical devices / Laboratory diagnostics
- **Location:** Bangkok, Thailand
- **DOB:** 23 March 1995

Full profile → see `profile.md`

---

## What we worked on this session

### 1. Profile built (`profile.md`)
- Merged data from ChatGPT memory export + live conversation
- Contains: personal info, professional background, strengths, goals, interests, work preferences, AI collaboration notes

### 2. Quotation Email Skill (in progress)
A custom skill to help Job write formal Thai-language quotation emails to hospital customers.

**Spec confirmed:**
- Language: **Thai (Formal)**
- Tone: Professional, not pushy
- Recipients: แพทย์/หัวหน้าแล็บ AND จัดซื้อโรงพยาบาล (different tone per recipient)
- Structure: Flexible — chosen at generate time
- Product lines with separate templates:
  - Sysmex UA/UF Series (UF-4000, UN-Series, UD-10)
  - Sysmex CBC XN-3000
  - Dirui Analyzers
  - Sciendox Feces Analyzer 5A

**Files created:**
- `quotation-email-skill/SKILL.md` — main skill logic
- `quotation-email-skill/references/sysmex-ua-uf.md`
- `quotation-email-skill/references/sysmex-xn3000.md`
- `quotation-email-skill/references/dirui.md`
- `quotation-email-skill/references/sciendox.md`

**Status:** Draft complete — awaiting Job's feedback on test output before finalizing & packaging as `.skill` file

**Test output shown:** Sysmex UF-4000 email to หัวหน้าแล็บ (post-meeting version, 1,350,000 THB, free install + training)

**Pending feedback on:**
- Email length preference
- Tone adjustment
- Structure changes

---

## Job's Working Preferences (for Claude Code)
- Output: Structured, professional, concise — executive-friendly
- Formats liked: Excel/Sheets templates, PowerPoint structures, comparison matrices
- Avoid: Generic motivation, vague language, fluff
- Language: Thai preferred for communication, English for customer-facing docs
- Thinks in systems/frameworks — prefers step-by-step plans

---

## Suggested Next Steps in Claude Code
1. Finalize quotation email skill based on Job's feedback
2. Package skill as `.skill` file for installation
3. Potentially expand: Follow-up email variant, Tender version
4. Update `profile.md` as more info is shared
