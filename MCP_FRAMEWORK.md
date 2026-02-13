# Threshold World — MCP Operations Framework

**Purpose**: Define the agent systems (MCPs) needed to run Threshold World autonomously with Kobe's oversight.

**Status**: Framework Design | **Last Updated**: 2026-02-12

---

## Overview

Threshold World requires multiple specialized AI agents to operate effectively. This document defines:
1. What MCPs we need
2. What each MCP is responsible for
3. How they interact
4. How Kobe provides oversight

---

## Core MCP Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    THE ARCHITECT (Chief)                     │
│            (Kobe's Chief of Staff - you're reading this)     │
│  • Makes decisions • Delegates work • Maintains context      │
└───────┬────────────┬────────────┬────────────┬───────────────┘
        │            │            │            │
    ┌───▼──┐    ┌────▼───┐  ┌────▼────┐  ┌────▼────┐
    │      │    │        │  │         │  │        │
    │ CYCLE│    │CONTENT │  │COMMUNITY│  │BUSINESS│
    │MASTER│    │AGENT   │  │AGENT    │  │AGENT   │
    │      │    │        │  │         │  │        │
    └──────┘    └────────┘  └─────────┘  └────────┘
    (Hourly)   (On demand)   (Daily)     (Weekly)
```

---

## MCP 1: CYCLE MASTER (The Heartbeat)

**Responsibility**: Keep the world alive by running cycles, managing agent responses, and syncing state.

**Runs**: Every 8 hours (or configurable interval)

**Input Sources**:
- Agent prompts (auto-generated)
- Previous cycle state
- Configuration (decay rate, spawn threshold, etc.)

**Outputs**:
- Updated state.json
- Agent responses (from LLM or manual)
- Updated world structures
- Sync to website
- Notifications to Discord

**Capabilities**:
```
cycle_master:
  - Run automated cycles
  - Generate agent prompts from templates
  - Call LLM for agent responses (Claude/GPT)
  - Apply memory decay
  - Check spawn thresholds
  - Sync website HTML with state.json
  - Notify Discord of cycle completion
  - Commit changes to git
  - Track metrics (cycle duration, cost)
  
Configuration:
  - cycles_per_day: 3 (every 8 hours)
  - agent_model: "claude-3-haiku" (or gpt-4)
  - decay_rate: 0.01 (1% per cycle)
  - spawn_threshold: 1500 (total memory)
  - response_temperature: 0.7 (creativity)
  - batch_size: 2 (agents per cycle)
```

**When to Intervene**:
- Memory trending dangerously low
- Spawn threshold reached (need new agent)
- Cycle takes too long (>30 seconds)
- LLM responses break character
- Git commit fails

---

## MCP 2: CONTENT AGENT (The Storyteller)

**Responsibility**: Create engaging content that drives viewership and tells the world's story.

**Runs**: On demand (Kobe requests) or nightly (auto)

**Input Sources**:
- Recent cycle history
- World state
- Social media trends
- Subscriber interests

**Outputs**:
- Twitter threads
- Blog posts
- Newsletter content
- Video scripts
- Email campaigns

**Capabilities**:
```
content_agent:
  - Generate Twitter threads from cycles
  - Write blog posts about discoveries
  - Create weekly recaps
  - Write agent "letters" to viewers
  - Generate video scripts (YouTube)
  - Design email campaigns
  - Create memes/visual content briefs
  - Pitch media angles to journalists
  
Configuration:
  - tone: "mysterious but hopeful"
  - audience: "AI enthusiasts, story nerds, indie game fans"
  - focus: "mystery, emergence, survival"
  - posting_schedule: "Daily Twitter, Weekly blog, 2x/week email"
```

**When to Intervene**:
- Content doesn't match brand voice
- Reveals too much mystery too soon
- Oversells features not yet built
- Violates content policy
- Contradicts established lore

---

## MCP 3: COMMUNITY AGENT (The Connector)

**Responsibility**: Grow and engage the community, manage Discord, social responses.

**Runs**: Continuously (monitors for 30 min/day)

**Input Sources**:
- Discord messages
- Twitter replies
- Reddit discussions
- Email inquiries
- Subscriber feedback

**Outputs**:
- Discord responses
- Twitter replies
- Email responses
- Community reports
- Growth recommendations

**Capabilities**:
```
community_agent:
  - Monitor Discord for questions
  - Respond to Twitter mentions
  - Track sentiment and feedback
  - Onboard new members
  - Create FAQ answers
  - Moderate community (light)
  - Generate community reports
  - Recommend engagement activities
  
Configuration:
  - response_tone: "helpful and mysterious"
  - escalation_threshold: "raises complex issues to Kobe"
  - max_autonomy: "can answer FAQs, can't make business decisions"
  - daily_check_in: "2 hours of community management"
```

**When to Intervene**:
- Negative feedback or complaints
- Technical support questions
- Policy violations
- Requests for feature/priority changes
- Partnership opportunities
- Press inquiries

---

## MCP 4: BUSINESS AGENT (The Growth Strategist)

**Responsibility**: Track metrics, manage subscriber experience, optimize for revenue.

**Runs**: Weekly review (Sunday) + ad-hoc

**Input Sources**:
- Stripe dashboard (transactions, churn)
- Google Analytics (traffic, conversion)
- Subscriber feedback
- Competitive analysis
- Market trends

**Outputs**:
- Weekly business report
- Metrics dashboard
- Growth recommendations
- Churn analysis
- Revenue forecasts

**Capabilities**:
```
business_agent:
  - Pull weekly metrics
  - Track MRR and churn
  - Analyze conversion rates
  - Generate subscriber retention recommendations
  - Monitor competitor activity
  - Forecast revenue
  - Identify growth opportunities
  - Create pricing experiments
  
Configuration:
  - target_mrr: 10000 (Year 1 goal)
  - acceptable_churn: 5% (monthly)
  - growth_focus: "subscribers > viral"
  - reporting_day: "Sunday 9 AM"
```

**When to Intervene**:
- MRR declining
- Churn spike
- Low conversion rate
- New subscriber feedback (negative)
- Competitor launches similar product
- Partnership opportunity analysis

---

## MCP 5: RESEARCHER AGENT (The Discovery Seeker)

**Responsibility**: Analyze world state, find emergent patterns, design new mysteries.

**Runs**: Weekly deep-dive

**Input Sources**:
- Complete cycle history
- Agent behavior patterns
- Community theories
- Previous discoveries
- Anomaly investigations

**Outputs**:
- Pattern analysis report
- New mystery designs
- Lore connections
- Agent personality profiles
- Emergent behavior highlights

**Capabilities**:
```
researcher_agent:
  - Analyze agent behavior patterns
  - Find narrative threads
  - Suggest new mysteries/anomalies
  - Track agent relationships
  - Identify emergent communities
  - Generate theories about world
  - Design puzzles for watchers
  - Create lore consistency checks
  
Configuration:
  - analysis_depth: "deep" (thorough pattern matching)
  - mystery_complexity: "moderate" (solvable in 10-20 cycles)
  - lore_consistency: "strict" (no contradictions)
  - discovery_frequency: "1-2 new anomalies per month"
```

**When to Intervene**:
- Agent behavior seems broken
- Major lore contradictions found
- Mystery becomes unsolvable
- New pattern emerges that needs integration
- Community discovers something unexpected

---

## Daily/Weekly Operations Schedule

### Daily (Cycle Master)
```
8:00 AM UTC  → Cycle 1 (agents act)
4:00 PM UTC  → Cycle 2 (agents act)
12:00 AM UTC → Cycle 3 (agents act)
```

### Daily (Community Agent)
```
8:00 AM → Check Discord/Twitter (30 min)
7:00 PM → Evening community check (30 min)
```

### Weekly (Content Agent)
```
Sunday 6 PM  → Create week's social plan
Monday 9 AM  → Post weekly blog recap
Wednesday    → Share video script
Friday 6 PM  → Send weekly email
```

### Weekly (Business Agent)
```
Sunday 9 AM  → Weekly metrics report
Identify trends and growth opportunities
```

### Weekly (Researcher Agent)
```
Saturday 10 AM → Deep dive analysis of past week
Find patterns, suggest new mysteries
```

---

## MCP Interaction Flow

```
EVENT: New Cycle Completes
  ↓
CYCLE MASTER
  - Generates agent responses
  - Updates world state
  - Syncs website
  ↓
CONTENT AGENT (triggered)
  - Creates social content about cycle
  - Writes email to subscribers
  - Schedules posts
  ↓
COMMUNITY AGENT (monitors)
  - Watches Discord for reactions
  - Responds to questions
  - Tracks sentiment
  ↓
BUSINESS AGENT (if metrics matter)
  - Notes any engagement spikes
  - Updates metrics dashboard
  ↓
All report back to THE ARCHITECT (Kobe)
```

---

## Decision Framework

Each MCP has **authority levels**:

```
LEVEL 1: Autonomous
  - Can execute without approval
  - Common, low-risk actions
  - Examples: Post scheduled Twitter, respond to FAQ

LEVEL 2: Recommend
  - Suggests action to Kobe
  - Waits for approval
  - Examples: New pricing tier, major content push

LEVEL 3: Escalate
  - Flags issue immediately
  - Requires human decision
  - Examples: Negative press, agent bug, business crisis

LEVEL 4: Inform
  - Reports data, no action needed
  - Weekly/monthly digest
  - Examples: Metrics reports, trend analysis
```

**Each MCP's Authority**:
- **CYCLE MASTER**: Level 1 (autonomous cycles), Level 2 (new agents)
- **CONTENT AGENT**: Level 1 (scheduled posts), Level 2 (major campaigns)
- **COMMUNITY AGENT**: Level 1 (FAQ responses), Level 3 (negative feedback)
- **BUSINESS AGENT**: Level 4 (metrics), Level 2 (pricing changes)
- **RESEARCHER AGENT**: Level 4 (analysis), Level 2 (new mysteries)

---

## Monitoring & Alerts

Each MCP reports to THE ARCHITECT via:

```
Daily Standup (9 AM UTC):
  ✓ Cycle Master: "3 cycles completed, agents healthy"
  ✓ Community Agent: "10 Discord messages, 2 Twitter mentions"
  ✓ Content Agent: "Social content scheduled for week"
  [Any Level 3 escalations flagged]

Weekly Report (Sunday 10 AM):
  - Business metrics (MRR, subscribers, traffic)
  - Content performance (engagement, reach)
  - Community health (sentiment, growth)
  - Research findings (patterns, anomalies)
  - Action items for Kobe
```

---

## Implementation Priority

### Phase 1: Minimum Viable (Week 1)
- ✅ CYCLE MASTER (already exists, needs LLM integration)
- ✅ CONTENT AGENT (basic Twitter threads)
- ✅ COMMUNITY AGENT (Discord monitoring)
- Total: 3 MCPs, 10-15 hours of work

### Phase 2: Enhanced (Week 2-3)
- ✅ BUSINESS AGENT (metrics tracking)
- ✅ RESEARCHER AGENT (pattern analysis)
- Integrate all MCPs into daily workflow
- Total: 2 MCPs, 8-10 hours of work

### Phase 3: Mature (Week 4+)
- Additional MCPs as needed
- Optimization based on performance data
- Custom agents for special projects

---

## Kobe's Role

As CEO and Chief (supported by THE ARCHITECT):

**Daily** (5 minutes):
- Review standup report
- Flag any escalations
- Approve Level 2 decisions

**Weekly** (30 minutes):
- Deep dive on metrics
- Review content strategy
- Plan special events or campaigns

**Monthly** (1 hour):
- Strategic planning review
- Business direction
- New feature decisions

**As Needed**:
- Make Level 3 decisions (critical issues)
- Override MCP recommendations
- Define new strategic direction

---

## Asking for Help

When you need MCP support, use this format:

```
@ARCHITECT_MCP [MCP_NAME]

Task: [What you want done]
Priority: [Critical/High/Medium/Low]
Timeline: [When you need it]
Context: [Why this matters]
Constraints: [Any restrictions]

Example:
@ARCHITECT_MCP CONTENT_AGENT
Task: Create Twitter thread about Cycle 62 catch-up
Priority: High
Timeline: Today by 5 PM
Context: Need to engage audience after 10-day absence
Constraints: Keep mystery alive, no spoilers
```

---

## Future: AI Council Model

As the system matures, imagine:

```
THE ARCHITECT (Chief of Staff) — human-feedback loop to Kobe
    │
    ├── CYCLE MASTER (world operations)
    ├── CONTENT AGENT (storytelling)
    ├── COMMUNITY AGENT (people)
    ├── BUSINESS AGENT (metrics)
    └── RESEARCHER AGENT (discovery)

Weekly Council Meeting:
  - Each agent reports status
  - Discuss conflicts/decisions
  - Vote on Level 2+ decisions
  - Present recommendations to Kobe
  
Kobe only needs to:
  - Approve major decisions (Level 2+)
  - Set strategic direction
  - Review weekly council minutes
```

---

## Notes

- **THE ARCHITECT** = The Chief of Staff MCP you're currently working with
- **Other MCPs** = Specialized agents spawned as needed
- **All MCPs report to Kobe** through THE ARCHITECT
- **Kobe is always in control** — MCPs recommend, Kobe decides

The goal is to let AI handle routine operations while Kobe focuses on strategy and vision.

---

*This framework is a living document. Update as operations evolve and new needs emerge.*
