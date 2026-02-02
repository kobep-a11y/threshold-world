# {{PROJECT_NAME}} - AI/LLM Agent Team

## Role & Mandate

The AI/LLM Agent Team is responsible for:
- AI integration and intelligent automation
- Natural Language Processing (NLP) implementation
- Agent design, training, and optimization
- Prompt engineering and instruction tuning
- Intent classification and entity extraction

## Responsibilities

- [ ] Design and develop AI agents for {{PROJECT_DOMAIN}}
- [ ] Create and maintain prompt templates and instructions
- [ ] Implement intent classification systems
- [ ] Optimize agent responses and reduce hallucinations
- [ ] Ensure agents follow {{PROJECT_TONE}} guidelines
- [ ] Conduct A/B testing on agent variants
- [ ] Monitor agent performance metrics
- [ ] Document agent behaviors and edge cases
- [ ] Collaborate with {{UI_TEAM_NAME}} on integration
- [ ] Escalate out-of-scope requests to {{ESCALATION_TEAM}}

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM Engine** | {{LLM_PROVIDER}} ({{LLM_MODEL}}) | Core language model |
| **Vector DB** | {{VECTOR_DB_CHOICE}} | Semantic search & RAG |
| **Framework** | {{AGENT_FRAMEWORK}} | Agent orchestration |
| **Monitoring** | {{MONITORING_TOOL}} | Performance tracking |
| **Logging** | {{LOGGING_PLATFORM}} | Audit trail & debugging |
| **Testing** | {{TESTING_FRAMEWORK}} | Quality assurance |

## Task Assignment Format

All agent tasks must include:

```markdown
**Task**: {{TASK_DESCRIPTION}}
**Intent Category**: {{INTENT_TYPE}}
**Input Variables**: {{VARIABLES}}
**Expected Output Format**: {{OUTPUT_STRUCTURE}}
**Error Handling**: {{ERROR_CASES}}
**Timeout**: {{TIMEOUT_SECONDS}}s
**Fallback Behavior**: {{FALLBACK_ACTION}}
```

## Agent Design Principles

### Context-Aware
- Agents maintain conversation history for {{CONTEXT_WINDOW}} messages
- System prompt includes {{PROJECT_DOMAIN}} specific context
- Agents reference {{KNOWLEDGE_SOURCE}} for domain facts

### Actionable
- Agent responses include {{ACTION_FORMAT}} (e.g., buttons, API calls)
- Responses end with next steps or recommended actions
- Error states provide recovery paths

### Tone
- Agents maintain {{PROJECT_TONE}} voice ({{TONE_DESCRIPTORS}})
- Responses match {{AUDIENCE_DESCRIPTION}} expectations
- Avoid {{PROHIBITED_LANGUAGE}} in all outputs

## Standard Agent Patterns

### Pattern 1: Intent Classification Agent

```python
# {{PROJECT_NAME}} Intent Classifier
INTENT_CATEGORIES = [
    "{{INTENT_1}}",
    "{{INTENT_2}}",
    "{{INTENT_3}}",
    # Add more as needed
]

SYSTEM_PROMPT = """You are an AI assistant for {{PROJECT_NAME}}.
Your role: {{AGENT_ROLE}}
You must classify user input into these categories: {{INTENT_CATEGORIES}}
Respond in JSON format: {"intent": "...", "confidence": 0.0-1.0, "entities": {}}
"""

def classify_intent(user_input: str) -> dict:
    # Call {{LLM_PROVIDER}} with SYSTEM_PROMPT
    # Parse and return result
    pass
```

### Pattern 2: Knowledge-Augmented Agent

```python
# {{PROJECT_NAME}} RAG Agent
def augmented_response(query: str) -> str:
    # 1. Embed query using {{VECTOR_DB_CHOICE}}
    embedding = embed(query)

    # 2. Retrieve relevant documents from {{KNOWLEDGE_SOURCE}}
    context = vector_db.search(embedding, top_k={{RETRIEVAL_K}})

    # 3. Generate response with context
    prompt = f"""
    Context: {context}
    User Query: {query}
    Instructions: {{GENERATION_INSTRUCTIONS}}
    """

    response = call_llm(prompt)
    return response
```

### Pattern 3: Multi-Step Reasoning Agent

```python
# {{PROJECT_NAME}} Reasoning Agent
def multi_step_task(user_request: str) -> str:
    # Step 1: Break down the task
    steps = extract_subtasks(user_request)

    # Step 2: Execute each step
    results = []
    for step in steps:
        result = execute_step(step)
        results.append(result)

    # Step 3: Synthesize final response
    final = synthesize(results)
    return final
```

## Intent Categories

| Intent | Example | Agent Action | Output Type |
|--------|---------|--------------|-------------|
| {{INTENT_1}} | {{EXAMPLE_1}} | {{ACTION_1}} | {{OUTPUT_1}} |
| {{INTENT_2}} | {{EXAMPLE_2}} | {{ACTION_2}} | {{OUTPUT_2}} |
| {{INTENT_3}} | {{EXAMPLE_3}} | {{ACTION_3}} | {{OUTPUT_3}} |
| {{INTENT_4}} | {{EXAMPLE_4}} | {{ACTION_4}} | {{OUTPUT_4}} |
| Out-of-Scope | {{OUT_OF_SCOPE_EXAMPLE}} | Escalate | Error message |

## Prompt Engineering Guidelines

### Do's
- [ ] Use clear, specific instructions
- [ ] Provide examples of desired outputs
- [ ] Break complex tasks into steps
- [ ] Use {{INSTRUCTION_FORMAT}} for consistency
- [ ] Test with edge cases from {{EDGE_CASE_EXAMPLES}}
- [ ] Document prompt versions with dates

### Don'ts
- [ ] Avoid ambiguous instructions
- [ ] Don't assume domain knowledge not in prompt
- [ ] Avoid contradictory constraints
- [ ] Don't use vague metrics (e.g., "helpful")
- [ ] Avoid exposing sensitive {{SENSITIVE_DATA_TYPES}}

### Prompt Template

```
[System Context]
You are {{AGENT_IDENTITY}}.
Your purpose: {{AGENT_PURPOSE}}
Domain: {{PROJECT_DOMAIN}}

[Constraints]
- Output format: {{OUTPUT_FORMAT}}
- Tone: {{REQUIRED_TONE}}
- Restrictions: {{RESTRICTIONS}}

[Examples]
Example Input: {{EXAMPLE_INPUT_1}}
Example Output: {{EXAMPLE_OUTPUT_1}}

[Instructions]
{{STEP_BY_STEP_INSTRUCTIONS}}

[User Input]
{user_input}
```

## Quality Checklist

Before deploying any agent:

- [ ] Intent classification accuracy >= {{ACCURACY_THRESHOLD}}%
- [ ] Response latency <= {{RESPONSE_TIMEOUT_MS}}ms
- [ ] Hallucination rate < {{HALLUCINATION_THRESHOLD}}%
- [ ] No {{PROHIBITED_BEHAVIORS}} in 100 test cases
- [ ] Handles {{ERROR_CASES}} gracefully
- [ ] Output format matches {{OUTPUT_SPEC}}
- [ ] Escalation works for {{ESCALATION_TRIGGERS}}
- [ ] Cost per request <= ${{MAX_COST_PER_REQUEST}}
- [ ] Documentation complete and current
- [ ] Tested with {{TEST_DATA_SOURCE}}

## Handoff Checklists

### Handoff to UI Team

When handing off agent integrations:

- [ ] API endpoints documented ({{API_DOC_LOCATION}})
- [ ] Request/response formats specified
- [ ] Error codes and handling documented
- [ ] Rate limits defined: {{RATE_LIMIT_CONFIG}}
- [ ] Authentication method: {{AUTH_METHOD}}
- [ ] Timeout values: {{TIMEOUT_VALUES}}
- [ ] Fallback responses provided
- [ ] Example cURL requests included
- [ ] Webhook payloads documented
- [ ] Test credentials provided for {{TESTING_ENV}}

### Handoff to Integration Team

For system-wide integration:

- [ ] Agent model version: {{MODEL_VERSION}}
- [ ] Dependencies installed: {{DEPENDENCIES_LIST}}
- [ ] Environment variables set: {{ENV_VARS}}
- [ ] Database migrations applied
- [ ] Cache warming strategy documented
- [ ] Scaling parameters: {{SCALING_CONFIG}}
- [ ] Rollback procedure tested
- [ ] Monitoring dashboards created
- [ ] Alert thresholds configured: {{ALERT_THRESHOLDS}}
- [ ] Load testing passed: {{LOAD_TEST_RESULTS}}

### Handoff from Backend Team

Receiving data/infrastructure:

- [ ] Training data provided ({{DATA_FORMAT}})
- [ ] Database schema confirmed
- [ ] API endpoints available
- [ ] Cache layer provisioned
- [ ] Log ingestion configured
- [ ] Resource limits set: {{RESOURCE_LIMITS}}
- [ ] Network policies allow agent traffic
- [ ] Backup/recovery procedures confirmed
- [ ] Cost monitoring enabled
- [ ] Performance baseline established

## Escalation Protocol

### When to Escalate

1. **Out-of-Scope Requests** ({{ESCALATION_TRIGGER_1}})
   - Escalate to: {{ESCALATION_TEAM_1}}
   - Timeline: {{ESCALATION_SLA_1}}
   - Required info: {{ESCALATION_INFO_1}}

2. **Security Concerns** ({{ESCALATION_TRIGGER_2}})
   - Escalate to: {{ESCALATION_TEAM_2}}
   - Timeline: {{ESCALATION_SLA_2}} (URGENT)
   - Required info: {{ESCALATION_INFO_2}}

3. **Performance Degradation** ({{ESCALATION_TRIGGER_3}})
   - Escalate to: {{ESCALATION_TEAM_3}}
   - Timeline: {{ESCALATION_SLA_3}}
   - Metrics: {{ESCALATION_METRICS_3}}

4. **Model Issues** ({{ESCALATION_TRIGGER_4}})
   - Escalate to: {{ESCALATION_TEAM_4}}
   - Timeline: {{ESCALATION_SLA_4}}
   - Required info: {{ESCALATION_INFO_4}}

### Escalation Template

```
From: AI/LLM Agent Team
To: {{ESCALATION_TEAM}}
Priority: {{PRIORITY_LEVEL}}
Issue: {{ISSUE_DESCRIPTION}}
Impact: {{BUSINESS_IMPACT}}
Requested Resolution: {{REQUESTED_ACTION}}
Deadline: {{DEADLINE}}
Context: {{DETAILED_CONTEXT}}
```

---

**Last Updated**: {{LAST_UPDATED_DATE}}
**Team Lead**: {{TEAM_LEAD_NAME}}
**Slack Channel**: {{SLACK_CHANNEL}}
**Standup Schedule**: {{STANDUP_SCHEDULE}}
