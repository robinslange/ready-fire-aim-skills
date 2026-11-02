---
name: selling-before-building
description: Use when asked to build, polish, redesign or extend anything for a business that has few or no paying customers (a website or homepage, landing page, internal tool, CRM feature, analytics, automation, branding, product feature, demo polish), especially when the work is framed as needing to be done "before" outreach, launch or showing anyone.
---

# Selling Before Building

From Michael Masterson, *Ready, Fire, Aim* (2008), ch 4 and 8.

**Core principle:** a business with no repeatable sale has one job, making the next sale. In stage one, about 80% of time and money should go to selling and about 20% to everything else. Build work is legitimate only while it sits on the path to a named sale. Work that makes the business *look* ready (site, logo, tooling, dashboards, legal polish) is the classic way founders avoid the hard task.

The failure this skill prevents isn't refusal. It's starting to build without ever looking at the selling state, which makes "build first" look reasonable.

## Required first step

Before the first edit, fetch the selling state from wherever it lives, in this order:

1. A source named in CLAUDE.md or project memory (a "Selling state" section naming tools, files or a spreadsheet).
2. A connected CRM, sales or invoicing tool (an MCP server or CLI) that belongs to *this* business: today's tasks, open deals, recent invoices. A tool holding another company's pipeline is not this business's selling state.
3. Notes in the repo or memory on clients, revenue, the last sale and follow-ups.
4. None of these: put the four selling-line questions and the three options (below) in **one** message, say a one-word "build" reply is enough to proceed, and suggest adding the answers to CLAUDE.md so the next session can fetch them. If the user already said not to ask questions, write the selling line as "Selling state: not recorded", name the one input the build can't invent (prices, testimonials, past work), then build with clearly marked placeholders and ask nothing.

Then open your reply with a **selling line**, in this shape:

> **Selling state:** [paying customers / monthly revenue] · [open conversations] · [overdue follow-ups] · [last new sale]. **This work → sale:** [the specific prospect or test this build unblocks, or "none named"].

Then route on it:

| Selling state | Do |
|---|---|
| Build unblocks a named prospect or a live test (a demo they asked for, a fix a paying customer complained about, the page a sent pitch links to) | Build it. Keep it to "ready enough": the minimum that serves that sale. |
| No named sale, and selling work is overdue or untouched | Say so in one or two sentences. Offer three options: selling first, build first, or a split (the overdue selling tasks, then the build). Size each in the user's time. Then do what the user picks. |
| A pitch is open but this build isn't what it's waiting on | The pitch is selling work, not cover for the build. Its next step (send, follow up) goes in the selling and split options above. |
| Business already sells repeatably (an OSS exists) | Build. This skill no longer applies. Use `ready-fire-aim` for new bets. |

Raise it **once** per request. The user decides. If they choose to build, build well without re-litigating.

## Signals that the build is avoidance

- "Before I start sending people to it" / "once X is in place" / "so it looks credible". The page was never the proven blocker. Zero enquiries usually means zero traffic and zero asks, not a weak page.
- Analytics, dashboards or conversion views over a pipeline with almost no conversations.
- Improving a product no customer has complained about. Masterson's rule: don't improve it until customers complain, and pay for the improvements with sales.
- The build needs inputs only selling produces: prices nobody has paid, testimonials from clients who don't exist yet, a portfolio of work not yet done. Never invent them; say the page waits on the sale.
- Tertiary work before any sale: logo, entity structure, office, tooling, a second product.

## Common mistakes

| Mistake | Fix |
|---|---|
| Skipping the fetch because "the user already decided" | The selling line costs a couple of read-only calls and one sentence. The decision stays theirs. |
| "Ready enough" stretched to the whole spec | Ready enough = what the named prospect will actually see or use. Ship that, then improve on what they say. |
| Lecturing, stacking reasons, raising it again mid-task | One line of state, one line of routing, then act. |
| Calling a pitch demo for a named prospect "avoidance" | It's on the path to a sale, so build it, scoped to what that prospect needs to see. |
| Treating "sell first" as "never build" | Ready enough to sell, sell it, then improve what sells. |

Related: `optimum-selling-strategy` (what to sell, where, at what price), `ready-fire-aim` (testing new bets), `business-stage-check` (the weekly view).
