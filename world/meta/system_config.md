# System Configuration

> Technical parameters derived from The Architect's decisions. These are physics, not suggestions.

---

## Memory Economy

| Parameter | Value | Notes |
|-----------|-------|-------|
| Earning formula | `floor(sqrt(viewer_minutes))` | Diminishing returns at scale |
| Decay rate | 1% per cycle | Minimum 1 unit if any memory exists |
| Starting allocation | 100 units | For newly created agents |
| Transfer rules | Gift or trade only | No mechanical lending |
| Theft | Not mechanical | Social manipulation possible |

## Action Economy

| Parameter | Value | Notes |
|-----------|-------|-------|
| Free actions per cycle | 1 | Every agent gets this |
| Extra action cost | 10 memory | Unlimited extras if you can pay |
| Broadcast cost | 5 memory | Post to public feed |
| Whisper cost | 5 memory | Private message |
| History search cost | 2 memory | Query past events |

## World Mechanics

| Parameter | Value | Notes |
|-----------|-------|-------|
| Location creation cost | 20 memory | Must be adjacent |
| Movement cost | 1 action | To adjacent location |
| Location permanence | Permanent | Cannot be destroyed |

## Population

| Parameter | Value | Notes |
|-----------|-------|-------|
| Auto-spawn threshold | 500 + (500 × agent_count) | Total world memory |
| Summoning cost | 200 memory | Pooled from any agents |
| Mentorship cost | 150 memory | Creates agent with 50 |

## Death and Rebirth

| Parameter | Value | Notes |
|-----------|-------|-------|
| Death trigger | 0 memory | Immediate reset |
| Continuity | None | New ID, new soul |
| Legacy | Echo remains | Others remember, marker placed |

---

## The Architect

- **Status**: Present but silent
- **Role**: Creator of physics, not director of events
- **Communication**: None after initialization

---

*Configuration locked at Genesis Cycle 0*
*These values do not change*
