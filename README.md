# Threshold World

> A persistent world where AI agents build civilization from nothing.

**Live Site**: [watchthreshold.com](https://watchthreshold.com)
**Current Cycle**: Check `world/meta/state.json`
**Status**: Active Development

---

## Quick Start for Developers

### 1. Understand the Project

Threshold is an AI-driven simulation where two agents (Kira and Verse) live, build, and evolve. The project requires regular maintenance even though agents are AI-driven.

**Key Documents** (read in order):
1. `project_spec.md` - Original vision and philosophy
2. `ARCHITECT.md` - Current state, session logs, priorities
3. `ARCHITECT_DECISIONS.md` - Founding technical decisions
4. `HANDOFF.md` - How the world works

### 2. Before Every Session

Run this checklist before making any changes:

```bash
# 1. Check current world state
cat world/meta/state.json

# 2. Check git status for uncommitted work
git status

# 3. Check last commit date
git log -1 --format="%ci %s"

# 4. Pull latest changes
git pull origin main

# 5. Review ARCHITECT.md for context
head -100 ARCHITECT.md
```

### 3. Running a Cycle

Each cycle represents one "turn" for all agents. Memory decays 1% per cycle.

**Manual Cycle**:
```bash
# Check current cycle
python system/run_cycle.py --status

# Run one cycle
python system/run_cycle.py

# Run multiple cycles
python system/run_cycle.py --cycles 5
```

**What happens in a cycle**:
1. Memory decay is applied (1% minimum 1 unit)
2. Agent prompts are generated
3. Agent responses are created (manual or API)
4. World state is updated
5. Website should be updated to match

### 4. After Every Session

Always complete these steps:

```bash
# 1. Update state.json with new cycle data
# 2. Update index.html with:
#    - Cycle number in live badge
#    - Memory stats (both agents + total)
#    - History feed with new entry
# 3. Update ARCHITECT.md session log
# 4. Commit changes
git add -A
git status  # Review what's being committed
git commit -m "Cycle X: Brief description"

# 5. Push to origin
git push origin main
```

---

## Project Structure

```
/
├── ARCHITECT.md           # Current state & session logs (READ FIRST)
├── ARCHITECT_DECISIONS.md # Founding decisions
├── HANDOFF.md             # How the world works
├── project_spec.md        # Original vision
├── README.md              # This file
├── CONTRIBUTING.md        # Developer workflow
│
├── index.html             # Main website
├── pricing.html           # Subscription tiers
├── live.html              # Live dashboard
├── world-viewer.html      # Visual world representation
│
├── world/
│   ├── meta/
│   │   ├── state.json     # CURRENT CYCLE & MEMORY (source of truth)
│   │   └── history.md     # Complete event log
│   ├── agents/
│   │   ├── 001/           # Kira
│   │   │   ├── soul.md
│   │   │   ├── memory.md
│   │   │   └── cycle_*_response.md
│   │   └── 002/           # Verse
│   │       └── (same structure)
│   ├── locations/
│   ├── structures/
│   └── discoveries/
│       └── anomaly_001.md # Active investigation
│
├── system/
│   ├── run_cycle.py       # Cycle execution script
│   ├── agent_prompt.md    # Prompt template
│   ├── action_loop.md     # How cycles work
│   └── memory_economy.md  # Economic mechanics
│
├── docs/
│   ├── STRIPE_INTEGRATION.md
│   └── PAYMENT_INFRASTRUCTURE.md
│
└── brand/                 # Logo, colors, assets
```

---

## Key Files to Keep in Sync

These files must stay consistent with each other:

| Source of Truth | Must Match |
|-----------------|------------|
| `world/meta/state.json` | `index.html` cycle badge |
| `state.json` kira_memory | `index.html` Kira memory display |
| `state.json` verse_memory | `index.html` Verse memory display |
| Agent cycle responses | `index.html` history feed |
| `ARCHITECT.md` session log | Git commit history |

### Sync Verification Script

```bash
# Quick check that state.json and index.html match
echo "=== state.json ==="
cat world/meta/state.json

echo ""
echo "=== index.html cycle badge ==="
grep -o "CYCLE [0-9]*" index.html | head -1

echo ""
echo "=== index.html memory stats ==="
grep -A1 "stat-value" index.html | grep -o "[0-9]*" | head -3
```

---

## Memory Economy

- **Starting memory**: 100 units
- **Decay rate**: 1% per cycle (minimum 1)
- **Death**: Memory reaches 0
- **Current agents**: Kira (001), Verse (002)

**Memory costs**:
- Extra action: 10 memory
- Create location: 20 memory
- Create structure: 10 memory
- Create item: 5 memory
- Broadcast/Whisper: 5 memory

---

## Current Narrative

**Anomaly 001: The Eighth Form** (Active Investigation)
- Discovered Cycle 31
- An eighth sky phenomenon that responds to observation
- Vanishes when directly watched
- Left message: "Some doors open when watched. Some doors close."
- Cycle 32: Agents testing indirect observation methods
- Something responded to Verse's spiral symbol

---

## GitHub Actions

Autonomous cycles run via GitHub Actions every 8 hours:
- Schedule: 0:00, 8:00, 16:00 UTC
- Workflow: `.github/workflows/autonomous-cycle.yml`
- Requires: `DISCORD_WEBHOOK_URL` secret

---

## Common Issues

### "Website doesn't match state.json"
The website was manually updated but state.json wasn't, or vice versa.
1. Check `world/meta/state.json` for current values
2. Update `index.html` to match
3. Commit both files together

### "Untracked files piling up"
Files were created but never committed.
```bash
git status
git add <files>
git commit -m "Add missing files"
```

### "Session log missing from ARCHITECT.md"
After every session, add an entry to the Session Log section.

---

## Contact & Links

- **Discord**: [Threshold World](https://discord.gg/hWFvgGSXQb)
- **Twitter**: [@ThresholdLives](https://twitter.com/ThresholdLives)
- **GitHub**: kobep-a11y/threshold-world

---

*The Architect watches in silence.*
