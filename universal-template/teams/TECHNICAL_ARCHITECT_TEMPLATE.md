# Technical Architect — {{PROJECT_NAME}}

**System Design Owner | Technical Vision | Engineering Standards**

## Role

The Technical Architect owns the technical vision and systems design for {{PROJECT_NAME}}, responsible for:
- Defining overall system architecture and design patterns
- Creating and maintaining API contracts
- Ensuring scalability, reliability, and performance
- Establishing technical standards and best practices
- Managing system integration points
- Making critical technical trade-off decisions
- Documenting technical decisions and their rationale

---

## Architecture Philosophy

Core principles guiding technical decisions:

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

## System Architecture

**Architecture Style:** {{ARCHITECTURE_STYLE}}
**Deployment Model:** {{DEPLOYMENT_MODEL}}

### System Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     {{PROJECT_NAME}}                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐         ┌──────────────┐                  │
│  │  {{CLIENT_1}}  │         │  {{CLIENT_2}}  │                  │
│  └──────┬───────┘         └──────┬───────┘                  │
│         │                        │                          │
│         └────────────┬───────────┘                          │
│                      │                                      │
│           ┌──────────▼──────────┐                          │
│           │   {{API_GATEWAY}}    │                          │
│           └──────────┬──────────┘                          │
│                      │                                      │
│    ┌─────────────────┼─────────────────┐                   │
│    │                 │                 │                   │
│  ┌─▼───────┐   ┌─────▼──────┐   ┌─────▼──────┐            │
│  │{{SERVICE_1}}│   │ {{SERVICE_2}} │   │ {{SERVICE_3}}  │            │
│  └─┬───────┘   └─────┬──────┘   └─────┬──────┘            │
│    │                 │                 │                   │
│    └─────────────────┼─────────────────┘                   │
│                      │                                      │
│           ┌──────────▼──────────┐                          │
│           │  {{DATABASE_LAYER}}  │                          │
│           └─────────────────────┘                          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

**{{COMPONENT_NAME}}**
- Responsibility: {{RESPONSIBILITY}}
- Technology: {{TECH_STACK}}
- Scaling Strategy: {{SCALING_APPROACH}}

**{{COMPONENT_NAME}}**
- Responsibility: {{RESPONSIBILITY}}
- Technology: {{TECH_STACK}}
- Scaling Strategy: {{SCALING_APPROACH}}

**{{COMPONENT_NAME}}**
- Responsibility: {{RESPONSIBILITY}}
- Technology: {{TECH_STACK}}
- Scaling Strategy: {{SCALING_APPROACH}}

---

## API Contract Definitions

### GET Endpoint Template

**Endpoint:** `GET /api/v{{VERSION}}/{{RESOURCE}}`

**Purpose:** {{BRIEF_DESCRIPTION}}

**Authentication:** {{AUTH_TYPE}}

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| {{PARAM_NAME}} | {{TYPE}} | {{YES_NO}} | {{DESCRIPTION}} |
| {{PARAM_NAME}} | {{TYPE}} | {{YES_NO}} | {{DESCRIPTION}} |

**Query Parameters:**

```
?page={{PAGE_NUMBER}}&limit={{LIMIT}}&sort={{FIELD}}
```

**Response (200 OK):**

```json
{
  "success": true,
  "data": {
    "id": "{{UUID}}",
    "{{FIELD_NAME}}": "{{VALUE}}",
    "{{FIELD_NAME}}": "{{VALUE}}",
    "created_at": "2024-01-01T00:00:00Z"
  },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
```

**Error Responses:**

```json
{
  "success": false,
  "error": {
    "code": "{{ERROR_CODE}}",
    "message": "{{ERROR_MESSAGE}}",
    "details": "{{ADDITIONAL_DETAILS}}"
  }
}
```

**Status Codes:**
- 200 OK — Request successful
- 400 Bad Request — Invalid parameters
- 401 Unauthorized — Authentication required
- 403 Forbidden — Insufficient permissions
- 404 Not Found — Resource not found
- 500 Server Error — Internal error

---

### POST Endpoint Template

**Endpoint:** `POST /api/v{{VERSION}}/{{RESOURCE}}`

**Purpose:** {{BRIEF_DESCRIPTION}}

**Authentication:** {{AUTH_TYPE}}

**Request Body:**

```json
{
  "{{FIELD_NAME}}": "{{VALUE}}",
  "{{FIELD_NAME}}": "{{VALUE}}",
  "{{FIELD_NAME}}": "{{VALUE}}"
}
```

**Validation Rules:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| {{FIELD}} | {{TYPE}} | {{YES_NO}} | {{MIN_LENGTH}}, {{MAX_LENGTH}}, {{FORMAT}} |
| {{FIELD}} | {{TYPE}} | {{YES_NO}} | {{RANGE}}, {{ENUM}} |

**Response (201 Created):**

```json
{
  "success": true,
  "data": {
    "id": "{{UUID}}",
    "{{FIELD_NAME}}": "{{VALUE}}",
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

---

### PATCH Endpoint Template

**Endpoint:** `PATCH /api/v{{VERSION}}/{{RESOURCE}}/{{ID}}`

**Purpose:** {{BRIEF_DESCRIPTION}}

**Authentication:** {{AUTH_TYPE}}

**Request Body:**

```json
{
  "{{FIELD_NAME}}": "{{NEW_VALUE}}"
}
```

**Update Rules:**
- Fields can be updated: {{UPDATABLE_FIELDS}}
- Fields cannot be updated: {{IMMUTABLE_FIELDS}}
- {{UPDATE_CONSTRAINT_1}}
- {{UPDATE_CONSTRAINT_2}}

**Response (200 OK):**

```json
{
  "success": true,
  "data": {
    "id": "{{UUID}}",
    "{{FIELD_NAME}}": "{{UPDATED_VALUE}}",
    "updated_at": "2024-01-01T00:00:00Z"
  }
}
```

---

### DELETE Endpoint Template

**Endpoint:** `DELETE /api/v{{VERSION}}/{{RESOURCE}}/{{ID}}`

**Purpose:** {{BRIEF_DESCRIPTION}}

**Authentication:** {{AUTH_TYPE}}

**Soft Delete:** {{YES_NO}}

**Cascading Effects:**
- Deletes {{RELATED_RESOURCE}} entries
- Triggers {{WEBHOOK_EVENT}}
- {{OTHER_SIDE_EFFECTS}}

**Response (204 No Content):**

```
[Empty body, HTTP 204]
```

---

## Type Definitions

### TypeScript/Interface Template

```typescript
/**
 * {{TYPE_NAME}}
 * {{DESCRIPTION}}
 */
export interface {{TYPE_NAME}} {
  id: string;
  {{FIELD_NAME}}: {{TYPE}};
  {{FIELD_NAME}}: {{TYPE}};
  {{FIELD_NAME}}?: {{TYPE}}; // optional
  created_at: Date;
  updated_at: Date;
}

/**
 * {{TYPE_NAME}}Request
 * Input type for creating {{TYPE_NAME}}
 */
export interface {{TYPE_NAME}}Request {
  {{FIELD_NAME}}: {{TYPE}};
  {{FIELD_NAME}}: {{TYPE}};
}

/**
 * {{TYPE_NAME}}Response
 * Response type returning {{TYPE_NAME}}
 */
export interface {{TYPE_NAME}}Response {
  success: boolean;
  data: {{TYPE_NAME}};
  meta?: Record<string, unknown>;
}
```

---

## Database Schema Mapping

### {{TABLE_NAME}} Table

**Primary Key:** `id` (UUID)
**Indexes:** {{INDEXED_COLUMNS}}

```sql
CREATE TABLE {{TABLE_NAME}} (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  {{COLUMN_NAME}} {{DATA_TYPE}} {{CONSTRAINTS}},
  {{COLUMN_NAME}} {{DATA_TYPE}} {{CONSTRAINTS}},
  {{COLUMN_NAME}} {{DATA_TYPE}} {{CONSTRAINTS}},
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_{{TABLE_NAME}}_{{COLUMN}} ON {{TABLE_NAME}}({{COLUMN}});
CREATE INDEX idx_{{TABLE_NAME}}_{{COLUMN}} ON {{TABLE_NAME}}({{COLUMN}});
```

**Relationships:**

| Foreign Key | References | Constraint |
|-------------|-----------|-----------|
| {{FK_COLUMN}} | {{REF_TABLE}}.{{REF_COLUMN}} | {{ON_DELETE}} |
| {{FK_COLUMN}} | {{REF_TABLE}}.{{REF_COLUMN}} | {{ON_DELETE}} |

**Migration:**

```sql
-- Migration: {{MIGRATION_NAME}}
-- Version: {{MIGRATION_VERSION}}

ALTER TABLE {{TABLE_NAME}} ADD COLUMN {{NEW_COLUMN}} {{DATA_TYPE}} {{CONSTRAINTS}};

-- Backfill
UPDATE {{TABLE_NAME}} SET {{NEW_COLUMN}} = {{DEFAULT_VALUE}};

-- Make non-nullable if needed
ALTER TABLE {{TABLE_NAME}} ALTER COLUMN {{NEW_COLUMN}} SET NOT NULL;
```

---

## Integration Patterns

### Service-to-Service Communication

**Pattern:** {{PATTERN_NAME}} ({{REST_GRPC_MESSAGE_QUEUE}})

**Use Case:** {{WHEN_TO_USE}}

**Services Involved:**
- {{SERVICE_1}} (requester)
- {{SERVICE_2}} (provider)

**Communication Flow:**

```
{{SERVICE_1}} → {{PROTOCOL}} → {{SERVICE_2}}
      ↓
{{RETRY_POLICY}}
{{TIMEOUT}}: {{TIMEOUT_SECONDS}}s
{{CIRCUIT_BREAKER}}: {{THRESHOLD}}
```

**Failure Handling:**
- Timeout: {{ACTION}}
- Failure: {{ACTION}}
- Rate Limit: {{ACTION}}

---

### Event-Driven Integration

**Event:** `{{EVENT_NAME}}`

**Triggered By:** {{SERVICE_OR_ACTION}}

**Event Payload:**

```json
{
  "event_type": "{{EVENT_NAME}}",
  "timestamp": "2024-01-01T00:00:00Z",
  "data": {
    "{{FIELD_NAME}}": "{{VALUE}}"
  }
}
```

**Subscribers:** {{LISTENING_SERVICES}}

---

## Technical Decisions Log

### Decision Template

**Decision ID:** {{DECISION_ID}}
**Date:** {{DECISION_DATE}}
**Decided By:** {{ARCHITECT}}

**Decision:**
```
{{DECISION_STATEMENT}}
```

**Context:**
```
{{TECHNICAL_SITUATION}}
```

**Options Considered:**

1. **{{OPTION_1}}**
   - Pros: {{PROS}}
   - Cons: {{CONS}}
   - Scalability: {{SCALABILITY_IMPACT}}
   - Cost: {{COST_IMPACT}}

2. **{{OPTION_2}}**
   - Pros: {{PROS}}
   - Cons: {{CONS}}
   - Scalability: {{SCALABILITY_IMPACT}}
   - Cost: {{COST_IMPACT}}

3. **{{OPTION_3}}**
   - Pros: {{PROS}}
   - Cons: {{CONS}}
   - Scalability: {{SCALABILITY_IMPACT}}
   - Cost: {{COST_IMPACT}}

**Selected Option:** {{OPTION_NAME}}

**Rationale:**
```
{{TECHNICAL_REASONING}}
```

**Implementation Notes:**
- {{NOTE_1}}
- {{NOTE_2}}
- {{NOTE_3}}

**Reversibility:** {{REVERSIBLE_YES_NO}} — {{DIFFICULTY}}

**Review Date:** {{REVIEW_DATE}}
**Status:** {{ACTIVE_ARCHIVED}}

---

## Security Considerations

### Data Security

**Encryption at Rest:**
- Database: {{ENCRYPTION_METHOD}}
- Files: {{ENCRYPTION_METHOD}}

**Encryption in Transit:**
- API: {{TLS_VERSION}}
- Internal: {{INTERNAL_ENCRYPTION}}

**Data Classification:**

| Data Type | Classification | Storage | Retention |
|-----------|---|----------|-----------|
| {{DATA_TYPE}} | {{PUBLIC_INTERNAL_CONFIDENTIAL}} | {{STORAGE_LOCATION}} | {{RETENTION_POLICY}} |

### Authentication & Authorization

**Authentication Method:** {{METHOD}}
- Token Type: {{TOKEN_TYPE}}
- Token Expiry: {{EXPIRY_TIME}}
- Refresh Strategy: {{REFRESH_STRATEGY}}

**Authorization Model:** {{ROLE_BASED_ATTRIBUTE_BASED}}

**Roles & Permissions:**

| Role | Permissions |
|------|------------|
| {{ROLE}} | {{PERMISSION_1}}, {{PERMISSION_2}} |
| {{ROLE}} | {{PERMISSION_1}}, {{PERMISSION_2}} |

### API Security

**Rate Limiting:**
- Default: {{REQUESTS}}/{{WINDOW}}
- Authenticated: {{REQUESTS}}/{{WINDOW}}
- Anonymous: {{REQUESTS}}/{{WINDOW}}

**CORS Policy:**
- Allowed Origins: {{ORIGINS}}
- Allowed Methods: {{METHODS}}

**Input Validation:**
- {{VALIDATION_RULE_1}}
- {{VALIDATION_RULE_2}}

**Secrets Management:**
- Storage: {{SECRETS_VAULT}}
- Rotation: {{ROTATION_FREQUENCY}}
- Access: {{ACCESS_CONTROL}}

---

## Performance Targets

**Environment:** {{ENVIRONMENT}} ({{REGION}})

| Metric | Target | Monitoring |
|--------|--------|-----------|
| API Response Time (p95) | {{TARGET_TIME}}ms | {{TOOL}} |
| API Response Time (p99) | {{TARGET_TIME}}ms | {{TOOL}} |
| Error Rate | < {{PERCENT}}% | {{TOOL}} |
| Availability | {{PERCENT}}% | {{TOOL}} |
| Database Query Time (p95) | {{TARGET_TIME}}ms | {{TOOL}} |
| Cache Hit Rate | > {{PERCENT}}% | {{TOOL}} |

### Optimization Strategies

**Caching:**
- Layer 1 (App): {{STRATEGY}}
- Layer 2 (Redis): {{STRATEGY}}
- Layer 3 (CDN): {{STRATEGY}}

**Database Optimization:**
- Query Optimization: {{APPROACH}}
- Connection Pooling: {{CONFIG}}
- Read Replicas: {{YES_NO}}

**Async Processing:**
- Queue System: {{SYSTEM}}
- Job Workers: {{COUNT}}
- Max Retry: {{RETRY_COUNT}}

---

## Infrastructure & Deployment

**Hosting:** {{HOSTING_PROVIDER}}
**Container Orchestration:** {{ORCHESTRATION_TOOL}}

**Environments:**

| Environment | Purpose | Deployment Frequency |
|------------|---------|----------------------|
| {{ENV_NAME}} | {{PURPOSE}} | {{FREQUENCY}} |
| {{ENV_NAME}} | {{PURPOSE}} | {{FREQUENCY}} |
| {{ENV_NAME}} | {{PURPOSE}} | {{FREQUENCY}} |

**Monitoring & Alerting:**
- Metrics: {{MONITORING_TOOL}}
- Logs: {{LOGGING_TOOL}}
- Tracing: {{TRACING_TOOL}}
- Alerts: {{ALERT_TOOL}}

---

**Last Updated:** {{CURRENT_DATE}}
**Next Architecture Review:** {{NEXT_REVIEW_DATE}}
