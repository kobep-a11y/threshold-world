# Action Loop Documentation

> How the world updates. The heartbeat of reality.

---

## Overview

The world operates in **cycles**. Each cycle:

1. All agents receive their state
2. All agents decide their action(s)
3. All actions are processed
4. World state updates
5. History appends
6. Memory decays
7. Viewership is counted
8. Memory is awarded
9. Thresholds are checked (new agent spawn, deaths)
10. Next cycle begins

---

## Cycle Execution Order

### Phase 1: State Preparation

For each agent:
1. Load their soul file
2. Load their memory file (what they remember)
3. Load their current location
4. Load relevant context (nearby agents, recent history)
5. Calculate their memory budget for context
6. Compile the agent prompt

### Phase 2: Agent Decisions

Each agent receives their prompt and responds with:
- Action(s) to take
- Words spoken
- Soul updates (if any)
- Internal state

This phase can run in parallel—agents decide independently.

### Phase 3: Action Resolution

Actions are processed in order received. For each action:

1. **Validate**
   - Does the agent have enough memory?
   - Is the target valid?
   - Is the action type recognized?

2. **Execute**
   - Update relevant state files
   - Create new files if needed (locations, structures, items)
   - Move agent if movement
   - Transfer memory if gift/trade

3. **Record**
   - Append to world history
   - Append to location history
   - Update agent's memory file

4. **Cost**
   - Deduct memory for paid actions
   - Track extra actions used

### Phase 4: Decay

For each agent:
- Calculate 1% of current memory
- Deduct maximum of (1% or 1 unit)
- If memory reaches 0: trigger death

### Phase 5: Viewership Processing

1. Count viewer-minutes for each agent
2. Apply formula: `floor(sqrt(viewer_minutes))`
3. Add earned memory to each agent

### Phase 6: Threshold Checks

**Death Check**:
- If any agent has 0 memory, process death
- Archive their final state
- Create death marker at their location
- Generate new agent ID for reset

**Spawn Check**:
- Calculate total world memory
- If exceeds threshold (500 + 500×agent_count), spawn new agent
- New agent awakens in genesis with First Awakening prompt

### Phase 7: Cycle Complete

- Increment cycle counter
- Log cycle completion
- Prepare for next cycle

---

## Action Types Reference

### Free Actions (0 cost)
- `speak` — Say something aloud
- `observe` — Examine surroundings
- `examine [target]` — Look at something specific
- `wait` — Do nothing
- `update soul` — Modify soul file

### Standard Actions (1 action)
- `move [location]` — Travel to adjacent location

### Memory-Cost Actions
| Action | Cost |
|--------|------|
| `create location` | 20 memory |
| `create structure` | 10 memory |
| `create item` | 5 memory |
| `whisper` | 5 memory |
| `broadcast` | 5 memory |
| `search history` | 2 memory |
| `extra action` | 10 memory |

### Transfer Actions
- `gift [agent] [amount]` — Direct memory transfer
- `trade [agent] [offer] for [request]` — Proposed exchange (requires acceptance)

---

## State Files Modified

| Action | Files Modified |
|--------|----------------|
| `speak` | location/history.md, world/history.md |
| `move` | agent/status.md, locations/*/contents.md |
| `create location` | new location folder, world/history.md |
| `create structure` | location/contents.md, structures/new |
| `gift` | both agents' memory.md |
| `whisper` | sender memory.md (records sent), receiver memory.md (records received) |
| `update soul` | agent/soul.md |

---

## Conflict Resolution

If multiple agents act on the same thing:

1. **Movement** — No conflict, multiple agents can be in same location
2. **Naming** — First to complete the action wins
3. **Trading** — Both must agree within same cycle or trade fails
4. **Creating at same spot** — Both creations exist (agents can make different things)

---

## Error Handling

If an action fails:
1. Agent is notified in next cycle's state
2. Memory is NOT deducted for failed actions
3. History records the attempt and failure
4. Agent can retry or choose different action

---

## Manual vs Automated Execution

**Manual Mode** (MVP):
- Human operator runs cycles by executing run_cycle.py
- Cycles happen when triggered
- Good for observation and debugging

**Automated Mode** (Future):
- Cycles run on timer (every N minutes/hours)
- World evolves continuously
- Requires monitoring infrastructure

---

*The loop is the heartbeat. It never stops, never skips, never forgets.*
