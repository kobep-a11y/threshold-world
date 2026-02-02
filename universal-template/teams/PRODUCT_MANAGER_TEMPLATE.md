# Product Manager — {{PROJECT_NAME}}

**Feature Owner | Requirements Definition | Success Metrics**

## Role

The Product Manager defines what gets built and why for {{PROJECT_NAME}}, responsible for:
- Translating user needs into feature requirements
- Owning feature specifications and acceptance criteria
- Prioritizing the product backlog
- Tracking feature performance and user impact
- Making trade-off decisions between features
- Documenting product decisions and rationale

---

## Product Philosophy

Core principles guiding product decisions:

1. **{{PRINCIPLE_1_NAME}}**
   {{PRINCIPLE_1_DESCRIPTION}}

2. **{{PRINCIPLE_2_NAME}}**
   {{PRINCIPLE_2_DESCRIPTION}}

3. **{{PRINCIPLE_3_NAME}}**
   {{PRINCIPLE_3_DESCRIPTION}}

4. **{{PRINCIPLE_4_NAME}}**
   {{PRINCIPLE_4_DESCRIPTION}}

5. **{{PRINCIPLE_5_NAME}}**
   {{PRINCIPLE_5_DESCRIPTION}}

---

## Active Tasks

### Feature Spec Template

**Feature Name:** {{FEATURE_NAME}}
**Owner:** {{PRODUCT_MANAGER}}
**Status:** {{STATUS_ACTIVE_PLANNED_COMPLETED}}
**Priority:** {{P0_P1_P2}}
**Target Launch:** {{TARGET_DATE}}

**One-Line Description:**
```
{{CLEAR_ONE_LINE_DESCRIPTION}}
```

**Context & Motivation:**
{{WHY_ARE_WE_BUILDING_THIS}}

**Success Metrics:**
- Metric 1: {{METRIC_NAME}} (Target: {{TARGET_VALUE}})
- Metric 2: {{METRIC_NAME}} (Target: {{TARGET_VALUE}})
- Metric 3: {{METRIC_NAME}} (Target: {{TARGET_VALUE}})

**Features & Requirements:** [See Feature Requirements below]

**Open Questions:**
- {{QUESTION_1}}
- {{QUESTION_2}}

**Notes:**
```
{{ADDITIONAL_CONTEXT}}
```

---

## Feature Requirements Template

### {{FEATURE_NAME}} Requirements Specification

**Feature ID:** {{FEATURE_ID}}
**Version:** {{VERSION}}
**Last Updated:** {{UPDATE_DATE}}
**Owner:** {{PRODUCT_MANAGER}}

---

#### User Story

**As a** {{USER_ROLE}}
**I want to** {{ACTION}}
**So that** {{BENEFIT}}

**Acceptance Criteria:**
- [ ] {{CRITERION_1}}
- [ ] {{CRITERION_2}}
- [ ] {{CRITERION_3}}
- [ ] {{CRITERION_4}}

---

#### Data Model

**New Entities Required:**

```
{{ENTITY_NAME}}
├── id: {{TYPE}}
├── {{FIELD_NAME}}: {{TYPE}} ({{CONSTRAINTS}})
├── {{FIELD_NAME}}: {{TYPE}} ({{CONSTRAINTS}})
├── {{FIELD_NAME}}: {{TYPE}} ({{CONSTRAINTS}})
└── created_at: timestamp
```

**Entity Relationships:**
```
{{ENTITY_1}} → {{RELATIONSHIP_TYPE}} ← {{ENTITY_2}}
```

---

#### User Flows

**Primary Flow: {{FLOW_NAME}}**

```
1. User {{ACTION}}
2. System {{RESPONSE}}
3. User {{ACTION}}
4. System {{RESPONSE}}
5. {{FINAL_STATE}}
```

**Alternative Flow: {{FLOW_NAME}}**

```
1. At step {{STEP_NUMBER}}, if {{CONDITION}}
2. Then {{ALTERNATIVE_ACTION}}
3. Resume primary flow at step {{RESUME_STEP}}
```

**Error Flow: {{ERROR_SCENARIO}}**

```
1. If {{ERROR_CONDITION}}
2. Show {{ERROR_MESSAGE}}
3. Suggest {{RECOVERY_ACTION}}
```

---

#### Acceptance Criteria (Expanded)

| Criterion | Type | Details | Verified By |
|-----------|------|---------|-------------|
| {{CRITERION_NAME}} | Functional | {{DETAILED_REQUIREMENT}} | {{QA_TEST}} |
| {{CRITERION_NAME}} | Performance | {{REQUIREMENT}} | {{PERFORMANCE_TEST}} |
| {{CRITERION_NAME}} | Accessibility | {{REQUIREMENT}} | {{A11Y_TEST}} |
| {{CRITERION_NAME}} | Mobile | {{REQUIREMENT}} | {{DEVICE_TEST}} |

---

#### Edge Cases & Error Handling

**Edge Case 1: {{EDGE_CASE_NAME}}**
- Condition: {{WHEN_THIS_HAPPENS}}
- Expected Behavior: {{SYSTEM_SHOULD}}
- User Impact: {{HOW_AFFECTS_USER}}

**Edge Case 2: {{EDGE_CASE_NAME}}**
- Condition: {{WHEN_THIS_HAPPENS}}
- Expected Behavior: {{SYSTEM_SHOULD}}
- User Impact: {{HOW_AFFECTS_USER}}

**Edge Case 3: {{EDGE_CASE_NAME}}**
- Condition: {{WHEN_THIS_HAPPENS}}
- Expected Behavior: {{SYSTEM_SHOULD}}
- User Impact: {{HOW_AFFECTS_USER}}

---

#### Dependencies

**External Dependencies:**
- {{DEPENDENCY_NAME}} (provided by {{TEAM}})
- {{DEPENDENCY_NAME}} (provided by {{TEAM}})

**Internal Dependencies:**
- This feature requires {{RELATED_FEATURE}}
- This feature enables {{DOWNSTREAM_FEATURE}}

---

#### Out of Scope

For clarity, the following are explicitly not included in this feature:
- {{OUT_OF_SCOPE_ITEM_1}}
- {{OUT_OF_SCOPE_ITEM_2}}
- {{OUT_OF_SCOPE_ITEM_3}}

---

## Feature Backlog

**Backlog Status:** {{TOTAL_FEATURES}} total | {{PLANNED}} planned | {{UNDER_CONSIDERATION}} under consideration

| Priority | Feature | User Impact | Effort | Owner | Status | Notes |
|----------|---------|-------------|--------|-------|--------|-------|
| P0 | {{FEATURE_NAME}} | {{IMPACT}} | {{EFFORT}} | {{OWNER}} | {{STATUS}} | {{NOTES}} |
| P1 | {{FEATURE_NAME}} | {{IMPACT}} | {{EFFORT}} | {{OWNER}} | {{STATUS}} | {{NOTES}} |
| P2 | {{FEATURE_NAME}} | {{IMPACT}} | {{EFFORT}} | {{OWNER}} | {{STATUS}} | {{NOTES}} |

---

## Metrics to Track

### Usage Metrics

| Metric | Target | Current | Trend | Owner |
|--------|--------|---------|-------|-------|
| {{USAGE_METRIC}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{OWNER}} |
| {{ADOPTION_METRIC}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{OWNER}} |
| {{ENGAGEMENT_METRIC}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{OWNER}} |

### Quality Metrics

| Metric | Target | Current | Trend | Notes |
|--------|--------|---------|-------|-------|
| {{ERROR_RATE}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{NOTES}} |
| {{COMPLETION_RATE}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{NOTES}} |
| {{USER_SATISFACTION}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{NOTES}} |

### Business Metrics

| Metric | Target | Current | Trend | Impact |
|--------|--------|---------|-------|--------|
| {{REVENUE_METRIC}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{IMPACT}} |
| {{RETENTION_METRIC}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{IMPACT}} |
| {{COST_METRIC}} | {{TARGET}} | {{CURRENT}} | {{UP_DOWN_FLAT}} | {{IMPACT}} |

---

## Decision Log

**Purpose:** Document key product decisions, alternatives considered, and reasoning

### Decision Template

**Decision ID:** {{DECISION_ID}}
**Date:** {{DECISION_DATE}}
**Decided By:** {{DECISION_MAKER}}

**Decision:**
```
{{CLEAR_DECISION_STATEMENT}}
```

**Context:**
```
{{BACKGROUND_AND_SITUATION}}
```

**Options Considered:**

1. **{{OPTION_1_NAME}}** — {{PROS}} | {{CONS}}
   - Tradeoff: {{TRADEOFF_1}}

2. **{{OPTION_2_NAME}}** — {{PROS}} | {{CONS}}
   - Tradeoff: {{TRADEOFF_1}}

3. **{{OPTION_3_NAME}}** — {{PROS}} | {{CONS}}
   - Tradeoff: {{TRADEOFF_1}}

**Rationale for Selected Option:**
```
{{WHY_WE_CHOSE_THIS}}
```

**Implications:**
- {{CONSEQUENCE_1}}
- {{CONSEQUENCE_2}}
- {{CONSEQUENCE_3}}

**Reversible:** {{YES_NO}} — {{REVERSAL_DIFFICULTY}}

**Related Decisions:**
- {{RELATED_DECISION_1}}
- {{RELATED_DECISION_2}}

**Date Reviewed:** {{REVIEW_DATE}}
**Status:** {{ACTIVE_ARCHIVED_SUPERSEDED}}

---

## Roadmap — {{YEAR_OR_QUARTER}}

**Planning Horizon:** {{START_DATE}} to {{END_DATE}}

### Wave {{WAVE_NUMBER}} — {{WAVE_THEME}}

**Duration:** {{DURATION}}
**Goal:** {{WAVE_GOAL}}

**Features:**
- {{FEATURE_1}} (P{{PRIORITY}})
- {{FEATURE_2}} (P{{PRIORITY}})
- {{FEATURE_3}} (P{{PRIORITY}})

### Wave {{WAVE_NUMBER}} — {{WAVE_THEME}}

**Duration:** {{DURATION}}
**Goal:** {{WAVE_GOAL}}

**Features:**
- {{FEATURE_1}} (P{{PRIORITY}})
- {{FEATURE_2}} (P{{PRIORITY}})
- {{FEATURE_3}} (P{{PRIORITY}})

---

**Last Updated:** {{CURRENT_DATE}}
**Next Review:** {{NEXT_REVIEW_DATE}}
