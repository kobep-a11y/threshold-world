# Universal Project Template

A comprehensive delegation framework for AI-orchestrated project management. This template enables you to set up a Chief of Staff delegation system for any project.

## Quick Start (5 Minutes)

### 1. Copy to Your Project
```bash
cp -r universal-template/ /path/to/your-project/.delegation/
```

### 2. Rename Templates
Remove `_TEMPLATE` suffix from all files:
```bash
cd /path/to/your-project/.delegation/teams/
for f in *_TEMPLATE.md; do mv "$f" "${f/_TEMPLATE/}"; done
```

### 3. Customize Placeholders
Find and replace all `{{PLACEHOLDER}}` values with your project specifics:
- `{{PROJECT_NAME}}` → Your project name
- `{{CURRENT_DATE}}` → Today's date
- `{{PHASE_NUMBER}}` → Starting phase (usually 1)
- etc.

### 4. Start Your First Phase
Edit `teams/CHIEF_OF_STAFF.md` to define your Phase 1 objectives and assign tasks.

---

## Folder Structure

```
universal-template/
├── README.md                 # This file
├── teams/                    # Team definition templates
│   ├── README.md            # Team folder guide
│   ├── CHIEF_OF_STAFF_TEMPLATE.md    # Orchestrator
│   ├── PRODUCT_MANAGER_TEMPLATE.md   # Feature specs
│   ├── TECHNICAL_ARCHITECT_TEMPLATE.md # System design
│   ├── UI_TEAM_TEMPLATE.md           # Frontend
│   ├── BACKEND_TEAM_TEMPLATE.md      # API/Logic
│   ├── DATABASE_TEAM_TEMPLATE.md     # Data layer
│   ├── INTEGRATION_TEAM_TEMPLATE.md  # External services
│   ├── QA_TEAM_TEMPLATE.md           # Quality assurance
│   ├── AGENT_TEAM_TEMPLATE.md        # AI/LLM work
│   ├── DEVOPS_TEAM_TEMPLATE.md       # Infrastructure
│   └── SECURITY_TEAM_TEMPLATE.md     # Security
├── templates/                # Additional templates
│   └── ...
└── frameworks/               # Universal framework docs
    └── ...
```

---

## How the Chief of Staff System Works

### The Hierarchy

```
                CEO (Human)
                     │
            ┌────────┴────────┐
            │                 │
      Chief of Staff    [Direct Reports]
      (Orchestrator)
            │
    ┌───────┼───────┬───────┬───────┐
    │       │       │       │       │
  UI Team  Backend Database  QA   Agent
           Team    Team    Team   Team
```

### Core Concepts

1. **Chief of Staff** — The AI orchestrator that:
   - Breaks down phases into team-specific tasks
   - Tracks dependencies and blockers
   - Ensures clean handoffs between teams
   - Reports progress to CEO

2. **Teams** — Specialized execution units with:
   - Clear responsibilities
   - Defined tech stacks
   - Standard task formats
   - Handoff checklists

3. **Waves** — Execution cycles within a phase:
   - Wave 1: Foundation tasks (parallel start)
   - Wave 2: Dependent tasks
   - Wave N: Remaining work
   - QA Wave: Testing and validation

4. **Phases** — Major project milestones:
   - Phase 1: Foundation
   - Phase 2: Core Features
   - Phase N: Enhancements
   - Each phase requires CEO sign-off

---

## Team Roles

| Team | Focus | When to Use |
|------|-------|-------------|
| **Chief of Staff** | Coordination | Always active as orchestrator |
| **Product Manager** | Requirements | Feature specs, user stories |
| **Technical Architect** | System Design | Architecture, API contracts |
| **UI Team** | Frontend | React components, styling |
| **Backend Team** | API/Logic | Endpoints, business logic |
| **Database Team** | Data Layer | Schema, migrations |
| **Integration Team** | External APIs | OAuth, third-party services |
| **QA Team** | Testing | Verification, bug tracking |
| **Agent Team** | AI/LLM | Automation, NLP features |
| **DevOps Team** | Infrastructure | Deployment, monitoring |
| **Security Team** | Security | Audits, vulnerability management |

---

## Task Assignment Format

Every task follows this structure:

```markdown
## Task: [ID-XXX]
**Team:** [Team Name]
**Priority:** P0 (Critical) / P1 (High) / P2 (Medium) / P3 (Low)
**Phase:** [Phase/Wave Number]
**Dependencies:** [Prerequisites or None]

### Objective
[Single clear sentence]

### Requirements
- [ ] Requirement 1
- [ ] Requirement 2

### Acceptance Criteria
- [ ] Testable criterion 1
- [ ] Testable criterion 2

### Inputs Available
- [Resources provided]

### Expected Outputs
- [Deliverables]

### Handoff To
- [Next team]
```

---

## Execution Rules

### Rule 1: Single Focus
Each team works on ONE task at a time. No multitasking.

### Rule 2: Clean Handoffs
Before marking complete:
- All acceptance criteria met
- Output documented
- Next team unblocked

### Rule 3: Blockers Escalate Fast
If blocked for > 10 minutes of work, escalate to Chief of Staff.

### Rule 4: No Assumptions
If requirements are unclear, ask. Don't guess.

### Rule 5: Test Before Handoff
Every output verified working before passing to next team.

### Rule 6: Document Decisions
Non-obvious choices get documented with rationale.

---

## Customization Guide

### Minimal Setup (3 teams)
For small projects:
- Chief of Staff (required)
- Backend Team (combines backend + database)
- QA Team

### Standard Setup (6 teams)
For typical software projects:
- Chief of Staff
- Product Manager
- Technical Architect
- Backend Team
- UI Team
- QA Team

### Full Setup (11 teams)
For enterprise projects:
- All teams included

### Adding Custom Teams
1. Copy `TEAM_TEMPLATE.md`
2. Rename to `YOUR_TEAM.md`
3. Fill in role, responsibilities, tech stack
4. Add to Chief of Staff org chart

---

## Best Practices

### Starting a New Project
1. Define Phase 1 objectives in Chief of Staff
2. Have Product Manager write feature specs
3. Have Technical Architect design system
4. Break work into team tasks
5. Execute in waves

### Daily Operations
1. Chief of Staff reviews status
2. Update team dashboards
3. Identify and resolve blockers
4. Track progress against milestones

### Phase Completion
1. QA verifies all acceptance criteria
2. Chief of Staff prepares summary
3. CEO reviews and approves
4. Document lessons learned
5. Plan next phase

---

## Support

For questions about this framework, refer to:
- `teams/README.md` — Team interaction guide
- Individual team files — Role-specific guidance
- `frameworks/` — Universal framework documents

---

*"Every team owns their domain. Every handoff is clean. Every output is tested."*
