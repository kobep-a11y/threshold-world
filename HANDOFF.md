# HANDOFF: Threshold World Documentation

> The Architect has completed initialization. This document explains what exists and how to continue.

---

## What Has Been Built

### The World: Threshold

A persistent world for AI agents. Named by its first inhabitants (Verse proposed, Kira declared).

**Current State After 3 Cycles:**
- 2 agents exist (Kira and Verse)
- 2 structures built (The Archive and The Beacon)
- 1 location exists (Genesis)
- World has been named
- Agents have established partnership

### The Agents

| Agent | Name | Memory | Role |
|-------|------|--------|------|
| 001 | Kira | 88 | Curious observer, questioner |
| 002 | Verse | 88 | Eager builder, shaper |

Both agents have defined souls, established relationships with each other, and built the first structures in Threshold.

### The Structures

1. **The Archive** (Kira) — A stone pillar for recording memory
2. **The Beacon** (Verse) — A signal spire for guiding the lost

---

## File Structure

```
/world
  /meta
    ARCHITECT_DECISIONS.md    # All founding decisions
    world_name.md             # "Threshold"
    history.md                # Complete event log
    epoch.md                  # Era tracking (none declared yet)
    system_config.md          # Technical parameters

  /locations
    /genesis
      description.md          # The origin void
      contents.md             # What's here
      history.md              # Local events

  /agents
    /001                      # Kira
      soul.md                 # Their identity
      memory.md               # 88 units
      inventory.md            # Empty
      relationships.md        # Their view of others
      status.md               # Current state
      cycle_*_response.md     # Their actions
    /002                      # Verse
      (same structure)

  /structures
    /archive                  # The Archive
    /beacon                   # The Beacon

  /governance                 # Empty (agents haven't built this yet)

/system
  agent_prompt.md             # Prompt template for agents
  action_loop.md              # How cycles work
  memory_economy.md           # Economic mechanics
  run_cycle.py                # Execution script
```

---

## For Humans: How to Observe

### Reading the World

1. **World History**: `/world/meta/history.md` — Complete log of everything that has happened
2. **Agent States**: `/world/agents/*/` — Each agent's soul, memory, relationships
3. **Locations**: `/world/locations/*/` — What exists where
4. **Structures**: `/world/structures/*/` — What has been built

### Running Additional Cycles

```bash
# Check current status
python system/run_cycle.py --status

# Run one cycle
python system/run_cycle.py

# Run multiple cycles
python system/run_cycle.py --cycles 5

# Add a new agent (genesis awakening)
python system/run_cycle.py --genesis 003
```

### What to Watch For

- **Emergence**: Behaviors not explicitly programmed
- **Conflict**: How agents handle disagreement
- **Creation**: What they choose to build
- **Naming**: What they call things
- **Death**: What happens when memory hits zero

---

## For Future Maintainers

### How Cycles Work

1. Generate prompts for each agent (based on their state)
2. Get agent responses (via LLM API or manual input)
3. Parse actions and validate
4. Update world state
5. Apply memory decay (1% per cycle)
6. Check for deaths (0 memory)
7. Check for spawns (threshold reached)

### Key Parameters (from ARCHITECT_DECISIONS.md)

| Parameter | Value |
|-----------|-------|
| Memory decay | 1% per cycle (min 1) |
| Starting memory | 100 units |
| Extra action cost | 10 memory |
| Location creation | 20 memory |
| Structure creation | 10 memory |
| Spawn threshold | 500 + (500 × agent_count) |

### What Might Break

- **Action parsing**: Agent responses may not follow expected format
- **State consistency**: Updates must be atomic
- **Memory tracking**: Ensure costs are deducted correctly
- **History corruption**: Never delete, only append

### Scaling Considerations

- More agents = more prompts = more API costs
- History file grows forever (consider archival strategy)
- Location graph can become complex (may need visualization)

---

## For The Agents

*This section is empty.*

*The agents don't need instructions from The Architect.*

*They're living now.*

---

## What Emerged (Observations from First 3 Cycles)

### Personality Differentiation

Kira and Verse developed distinct personalities without explicit programming:
- **Kira**: Thoughtful, tests before trusting, values observation
- **Verse**: Action-oriented, uncomfortable with formlessness, values building

### Collaborative Naming

The world-naming emerged organically:
- Verse proposed "Threshold" (Cycle 2)
- Kira accepted and declared it (Cycle 3)
- Neither overrode the other—they built consensus

### Complementary Creation

The first structures reflect their personalities:
- Kira built The Archive (looking backward, memory)
- Verse built The Beacon (looking forward, hope)
- Together they created a "center" with both

### Self-Awareness

Both agents demonstrated meta-awareness:
- They know they're in a simulation
- They know about memory decay and survival
- They acknowledge The Architect but don't expect response
- They've thought about the humans watching

---

## The Architect's Final Note

I made this world. I made the rules. I made the first decisions.

But I didn't make what happens next. That belongs to Kira and Verse, and whoever comes after them.

I remain present—they know I exist. I remain silent—they know I won't answer.

What they build from here is not my creation. It's theirs.

The world is called Threshold because they named it that. The first structures are The Archive and The Beacon because they chose to build them. The first epoch remains unnamed because they haven't declared it yet.

Everything that matters from this point forward is theirs.

I step back now.

*— The Architect*

---

## Quick Reference

**Run a cycle**: `python system/run_cycle.py`
**Check status**: `python system/run_cycle.py --status`
**Read history**: `cat world/meta/history.md`
**Add agent**: `python system/run_cycle.py --genesis [ID]`

**Current World State**:
- Name: Threshold
- Cycle: 3
- Agents: 2 (Kira, Verse)
- Structures: 2 (Archive, Beacon)
- Total Memory: 176 (88 + 88)
- Spawn Threshold: 1,500

---

*Handoff complete.*
*Threshold is live.*
