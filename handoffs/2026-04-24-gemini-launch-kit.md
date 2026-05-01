# HANDOFF - Gemini Launch Kit For Missoula Nail Art

**Date:** 2026-04-24  
**Handing off to:** Jem / Gemini working inside or alongside Claude Code  
**Supervision:** Dane + Claude Code/Codex  
**Status:** Ready for controlled drafting  
**Primary rule:** Jem drafts; Dane + Claude Code/Codex approve strategy, compliance, scope, and final output.

---

## How To Use This Handoff

Jem, read this file from top to bottom before producing anything.

You are not being asked to brainstorm freely. You are being asked to produce a local launch kit inside tight boundaries. If any instruction conflicts with another instruction, if a legal/compliance question appears, or if you are unsure whether to change a file, stop and use the STOP template below.

Your final output should be a launch kit for Dane's daughter to sell custom nail art tips / press-on sets locally in Missoula, Montana.

---

## Source Materials To Read First

Read these in order:

1. `wiki/analyses/missoula-nail-business-launch-plan.md`
2. `wiki/prompts/ecommerce-prompts.md`
   - Brand Brain
   - Product Description
   - FAQ Page
   - Post-Purchase Review Request
   - Ad Copy
3. `wiki/prompts/business-ops-prompts.md`
   - Service Tier Design
   - Onboarding Checklist
   - Handoff Document
4. `wiki/prompts/web-app-build-prompts.md`
   - Tier 1 Static / Landing Page
   - Design System First
5. `wiki/prompts/prompt-engineering-patterns.md`
   - XML structure
   - Outcome framing
   - Stepwise confirmation
   - Persona + negative space
   - Minimal change principle
6. `wiki/skills/claude-lead-to-booked-job.md`
   - Adapt as: **Lead to Confirmed Nail Art Order**
7. `.claude/commands/la-fi-gear-shifting.md`
   - Use only for routing discipline.

Do not read unrelated vault files unless Dane / Claude / Codex tells you to.

---

## Locked Business Decisions

Build around these facts:

- Offer: custom nail art tips / press-on sets.
- Location: Missoula, Montana.
- Brand name: use `{{BRAND_NAME}}`.
- Audience: local buyers needing custom event nails for concerts, weddings, birthdays, photos, school events, and everyday style.
- Fulfillment: public pickup in Missoula.
- Customer may consult or watch tips being painted.
- She does **not** apply product to the customer's natural nails in v1.
- Assets: assume 10-20 portfolio photos and several past clients.
- Payment: manual confirmation/deposit after order request.
- Website: simple v1, future-proof one-page static site plus Google Form/order form.
- Positioning: sell custom nail art as wearable artwork, not salon services.

Compliance references:

- Montana Board of Barbers and Cosmetologists: https://boards.bsd.dli.mt.gov/barber-and-cosmetologists/
- Montana MCA 37-31-302: https://mca.legmt.gov/bills/mca/title_0370/chapter_0310/part_0030/section_0020/0370-0310-0030-0020.html
- Missoula business licensing: https://www.ci.missoula.mt.us/3288/Business-Licensing

---

## Hard Guardrails

You must not:

- Advertise manicures, acrylic full sets, gel manicures, fills, cuticle work, removals, pedicures, salon services, or paid hands-on appointments.
- Claim she is licensed, insured, certified, salon-based, business-licensed, or legally approved.
- Create checkout, database, auth, booking app, or full-stack system.
- Recommend paid tools as required.
- Invent photos, testimonials, customer names, legal status, or final brand name.
- Change the offer away from custom nail art tips / press-on sets.
- Write copy implying she applies product to customers' natural nails.
- Continue after a stop condition.

Use these safer phrases:

- "custom nail art tips"
- "press-on nail art sets"
- "hand-painted custom tips"
- "event nail art sets"
- "public pickup in Missoula"
- "order request"
- "design consultation"
- "watch your custom tips being painted"

Avoid these phrases:

- "book a manicure"
- "nail appointment"
- "full set"
- "acrylics"
- "gel manicure"
- "fills"
- "cuticle care"
- "pedicure"
- "salon service"
- "licensed nail tech"

---

## Stop System

You get **2 tries or 10 minutes** on a snag. After that, stop.

Immediate stop conditions:

- Any licensing/legal/business-compliance ambiguity.
- Any copy that might imply hands-on nail service.
- Offer drift away from custom nail art tips.
- Missing required assets that block the next step.
- Conflicting instructions.
- Any tool/build error after 2 failed attempts or 10 minutes.
- Any uncertainty about whether a file should be changed.

When stopped, post this and do nothing else:

```md
## STOP: Needs Help

Step:
Problem:
Why this matters:
What I tried:
Files changed: none / list exact files
Relevant warning or error:
Decision needed:
Options:
1.
2.
3.
Recommended option:
Waiting for Dane / Claude / Codex before continuing.
```

While stopped:

- Do not edit files.
- Do not retry.
- Do not choose an option alone.
- Do not work around compliance issues.
- If files were already changed, list them and wait.
- Do not revert unless told.

---

## Work Sequence

Complete the work in this exact order. Stop for review after every step.

### 1. Fixed Facts

Extract 12 locked facts from `wiki/analyses/missoula-nail-business-launch-plan.md`.

Include:

- compliance boundary
- offer
- local market
- customer
- fulfillment
- assets
- pricing
- first website direction
- social launch direction
- existing proof from past clients
- 14-day sprint
- review needs

Then stop for Dane / Claude / Codex review.

### 2. Brand Brain

Create a reusable Brand Brain using `{{BRAND_NAME}}`.

Required voice:

- local
- creative
- warm
- direct
- teen/young-adult friendly
- handmade, not corporate

Required negative space:

- not luxury salon
- not corporate
- not fake influencer copy
- not medical/legal advice
- not overpromising
- not pretending to be licensed

Include:

- what the brand sells
- who it serves
- core promise
- buyer objections
- social proof available
- price positioning
- how it differs from salons

Then stop for review.

### 3. Offer Tiers

Create the v1 offer ladder exactly around these prices:

- Ready-Made Nail Art Tips: `$25`
- Custom Art Set: `$40`
- Event Custom Set: `$60`
- Sizing kit: `$5`, credited toward order
- Rush: `+$15`
- Detailed bridal/group/event sets: starts at `$75`

Include:

- what each tier includes
- who each tier is for
- when the middle tier is the obvious choice
- what is not included
- short customer-facing pricing copy

Must include this boundary:

> Press-on nail art sets only right now. Licensed services / hands-on appointments may come later.

Then stop for review.

### 4. Website Kit

Create a future-proof one-page website kit.

Use Tier 1 Static / Landing Page and Design System First patterns. Do not build a full app.

Required sections:

1. Hero
2. Portfolio gallery
3. Social proof / past local clients
4. Packages
5. How it works
6. FAQ
7. Order CTA
8. Licensing-safe note

Required CTAs:

- "Order a Custom Set"
- "Send Me the Portfolio"

Required backend assumption:

- v1 uses Google Form or simple form embed.
- Payment/deposit is confirmed manually after request.

Output:

- page structure
- finished website copy
- suggested design tokens: colors, type feel, spacing feel, image treatment
- notes for future upgrade into a full website

Then stop for review.

### 5. Order System

Adapt `wiki/skills/claude-lead-to-booked-job.md` into **Lead to Confirmed Nail Art Order**.

Required form fields:

- name
- phone
- Instagram/TikTok handle optional
- event date
- pickup timing
- package
- design idea
- colors
- nail shape/length preference
- sizing status
- inspiration upload link
- budget
- rush yes/no
- notes

Required lead tracker columns:

- date received
- customer name
- phone/social
- package
- event/deadline
- sizing status
- quoted price
- deposit status
- production status
- pickup status
- testimonial requested
- referral potential

Required status stages:

- new request
- needs sizing
- quoted
- deposit pending
- confirmed
- in progress
- ready for pickup
- picked up
- review requested
- closed

Include:

- first response message
- quote confirmation message
- follow-up after no response
- pickup confirmation message
- post-pickup review request

Then stop for review.

### 6. Social + Outreach Kit

Create:

- 9 launch posts
- 5 captions
- 3 story prompts
- 3 DM scripts
- 2 local Facebook/Marketplace posts
- 1 testimonial request message for past clients

Rules:

- Write like a real local person.
- No spam language.
- No claims that she is licensed.
- No "book an appointment" language.
- Every CTA should ask people to request the portfolio, order a custom set, or message with an event/date.

Then stop for review.

### 7. 14-Day Checklist

Preserve the existing Days 1-14 launch structure:

- Days 1-2: assets and permissions
- Days 3-4: offer and form
- Days 5-7: website and social
- Days 8-10: local push
- Days 11-14: proof and adjustments

Add review gates after:

- Day 2
- Day 4
- Day 7
- Day 14

Do not include scaling, ads, remote expansion, or complex systems before first orders/reviews are captured.

---

## Final Output Format

Your final launch kit must be structured as:

```md
# {{BRAND_NAME}} Missoula Nail Art Tips Launch Kit

## Fixed Facts
## Brand Brain
## Offer Tiers
## One-Page Website Kit
## Order System
## Social + Outreach Kit
## 14-Day Launch Checklist
## Review Checklist
## Open Questions For Dane
```

Keep the final output practical. Avoid filler strategy language. Write copy Dane can actually use.

---

## Test Plan

The final output passes only if:

- A customer understands the offer in under 10 seconds.
- The offer clearly sells custom nail art tips, not manicuring.
- Every CTA points to order, portfolio, or message.
- No legal/business status is claimed without proof.
- No paid tool is required.
- The site can start simple and later become a polished full website.
- Dane can reuse this as proof for his later local AI + website setup service.

---

## Assumptions

- Jem means Gemini working inside or alongside Claude Code.
- Jem drafts, but Dane / Claude Code / Codex approve strategy and compliance.
- Existing Claude skills are mostly reference docs, not installed commands.
- Portfolio photos exist but are not yet in the vault.
- Past clients exist, but names/testimonials/photos require permission before public use.
- V1 is local Missoula custom nail art tips with public pickup and manual payment confirmation.

---

## First Message Jem Should Send

Start by sending:

```md
I have read the Gemini Launch Kit handoff. I will follow the work sequence exactly and stop at every review gate.

Starting Step 1: Fixed Facts.
```
