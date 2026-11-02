# ready-fire-aim-skills

Five [Claude Code](https://claude.com/claude-code) skills for founders who would rather build than sell. They're drawn from Michael Masterson's *Ready, Fire, Aim: Zero to $100 Million* (2008), and scaled down for one-person and small businesses.

The main one is `selling-before-building`. Ask Claude to redo your homepage, add a dashboard or polish a feature, and it first checks your selling state: paying customers, open deals, overdue follow-ups and your last sale. It opens with one line on that and names the sale the work leads to, if there is one. If none is named, it offers selling first, building first or a split. It raises this once, then does what you pick.

## Why it fetches instead of lecturing

Without the skill, an agent told "redo the homepage before I start sending people to it" just started building. Given the pipeline facts (one paying client, several overdue follow-ups), the same agent pushed back on its own. So the skill doesn't tell Claude to sell first. It makes Claude look at the pipeline before the first edit. Each skill was pressure-tested against subagents with and without it, and rewritten wherever they slipped.

## The skills

| Skill | Use it when |
|---|---|
| `selling-before-building` | You ask for build or polish work on a business with few or no paying customers |
| `ready-fire-aim` | You're starting something unproven, want to "spec it properly first", or must decide whether to keep going or kill it. Seven questions, a 24-hour proposal, a stop-loss set before you launch, the smallest test that asks for real money |
| `optimum-selling-strategy` | Nothing is selling yet, or you're choosing an offer, price, channel or pitch. Four keys in order of impact: where the buyers are, what you sell first, price, then copy |
| `business-stage-check` | Weekly review, "what should I focus on", or too many priorities. One problem, one challenge, one opportunity, three numbers |
| `selling-to-existing-customers` | Renewals, a customer asking for more, or deciding what to offer next |

## Install

As a plugin:

```
/plugin marketplace add robinslange/ready-fire-aim-skills
/plugin install ready-fire-aim@ready-fire-aim-skills
```

Or as plain skills, linked so `git pull` updates them:

```sh
git clone https://github.com/robinslange/ready-fire-aim-skills.git
cd ready-fire-aim-skills
./install.sh
```

## Tell it where your sales live

`selling-before-building` works best when it can fetch the facts instead of asking you. Add a section to your project's `CLAUDE.md`:

```markdown
## Selling state
Deals: the HubSpot MCP (open deals, tasks due). Invoices: Xero. Last sale and follow-ups: sales/pipeline.md.
```

A spreadsheet, a markdown file or a CRM MCP server all work. With nothing configured, Claude asks you four short questions once and suggests adding the answer here.

## Notes

- These skills paraphrase the book's frameworks; they don't replace it. Buy it, especially chapters 4-8 on finding the way you sell. Not affiliated with the author or publisher.
- His examples are mass-mail publishers with thousands of responses per test. For a business with a handful of buyers, the test unit is the conversation. The skills say so where it matters.
- `./test.sh` checks that every skill loads (name, description, cross-references) and that no private paths or client names are committed.

## License

MIT
