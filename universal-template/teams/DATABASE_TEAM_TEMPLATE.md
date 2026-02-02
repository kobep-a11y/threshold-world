# Database Team Template

## Role
Design, create, maintain, and optimize {{PROJECT_NAME}} databases. Ensure data integrity, define schemas, manage migrations, and provide database access documentation to the Backend Team.

## Active Tasks

| Task ID | Table/Collection | Type | Description | Status | Assigned To | Due Date |
|---------|------------------|------|-------------|--------|-------------|----------|
| {{TASK_001}} | {{TABLE_NAME}} | {{SCHEMA_TYPE}} | {{TASK_DESCRIPTION}} | In Progress | {{ASSIGNEE}} | {{DATE}} |
| {{TASK_002}} | {{TABLE_NAME}} | {{SCHEMA_TYPE}} | {{TASK_DESCRIPTION}} | Pending | {{ASSIGNEE}} | {{DATE}} |

### Schema Specification Format

```
Table/Collection: {{TABLE_NAME}}
Type: {{SCHEMA_TYPE}} (SQL/NoSQL/Document)
Description: {{TABLE_PURPOSE}}
Owner: {{DATABASE_TEAM_MEMBER}}

Fields:
  {{FIELD_NAME}}:
    Type: {{FIELD_TYPE}}
    Constraints: {{CONSTRAINTS}} (PRIMARY KEY, NOT NULL, UNIQUE, etc.)
    Default: {{DEFAULT_VALUE}}
    Description: {{FIELD_DESCRIPTION}}

Indexes:
  - {{INDEX_NAME}} on {{FIELD_NAME(S)}}

Relationships:
  - {{FOREIGN_KEY_NAME}} → {{RELATED_TABLE}}({{RELATED_FIELD}})

Triggers/Hooks:
  - {{TRIGGER_NAME}}: {{TRIGGER_CONDITION}}
```

## Field Specification Template

| Field Name | Type | Constraint | Default | Description | Example |
|-----------|------|-----------|---------|-------------|---------|
| {{FIELD_NAME}} | {{DATA_TYPE}} | {{CONSTRAINT}} | {{DEFAULT}} | {{FIELD_PURPOSE}} | {{EXAMPLE_VALUE}} |
| {{FIELD_NAME}} | {{DATA_TYPE}} | {{CONSTRAINT}} | {{DEFAULT}} | {{FIELD_PURPOSE}} | {{EXAMPLE_VALUE}} |

### Data Type Reference
- **Numeric**: INT, BIGINT, FLOAT, DECIMAL({{PRECISION}}, {{SCALE}})
- **Text**: VARCHAR({{LENGTH}}), TEXT, CHAR({{LENGTH}})
- **Temporal**: DATE, DATETIME, TIMESTAMP
- **Boolean**: BOOLEAN, TINYINT(1)
- **Special**: UUID, JSON, ENUM('{{VALUE1}}', '{{VALUE2}}')

## Schema Lifecycle

### New Schema Checklist
- [ ] Schema design approved by Backend Team Lead
- [ ] Field naming follows {{NAMING_CONVENTION}} (snake_case, camelCase, etc.)
- [ ] All required fields identified and specified
- [ ] Data types chosen for performance and accuracy
- [ ] Constraints defined (NOT NULL, UNIQUE, CHECK, etc.)
- [ ] Indexes planned for frequently queried fields
- [ ] Relationships and foreign keys defined
- [ ] Migration script created for {{DATABASE_SYSTEM}}

### Migration Template
```sql
-- Migration: {{MIGRATION_ID}}_{{MIGRATION_NAME}}
-- Created: {{DATE}}
-- Author: {{AUTHOR}}

-- Up Migration
{{UP_MIGRATION_SQL}}

-- Down Migration (Rollback)
{{DOWN_MIGRATION_SQL}}
```

## Acceptance Criteria

- [ ] All {{PROJECT_NAME}} tables/collections created per specification
- [ ] Field definitions match {{BACKEND_TEAM}} requirements
- [ ] Data types support {{PERFORMANCE_REQUIREMENTS}}
- [ ] Indexes created for {{QUERY_PATTERNS}}
- [ ] Foreign key relationships configured
- [ ] Constraints enforced (NOT NULL, UNIQUE, CHECK)
- [ ] Seed data loaded for {{ENVIRONMENT}} testing
- [ ] Database backups scheduled and tested
- [ ] Schema documentation generated
- [ ] Migration scripts tested for up/down cycles
- [ ] Performance testing completed on {{PRODUCTION_SCALE_DATA}}

## Handoff Checklist (to Backend Team)

Before handing off to Backend Team, verify:

- [ ] All schema definitions documented in {{DOCUMENTATION_FORMAT}}
- [ ] Entity Relationship Diagram (ERD) provided
- [ ] Connection string/credentials shared securely
- [ ] Database user permissions configured for {{ENVIRONMENT}}
- [ ] Seed data provided for testing
- [ ] Backup and recovery procedures documented
- [ ] Query optimization suggestions provided
- [ ] Indexes explained (why each index was created)
- [ ] Calculated fields/views documented
- [ ] Data validation rules listed

## Database ID Reference Table

| Table/Collection | Database ID | Environment | Status | Created By | Creation Date |
|------------------|------------|-------------|--------|-----------|--------------|
| {{TABLE_NAME}} | {{DB_ID}} | {{ENVIRONMENT}} | Active | {{CREATOR}} | {{DATE}} |
| {{TABLE_NAME}} | {{DB_ID}} | {{ENVIRONMENT}} | Active | {{CREATOR}} | {{DATE}} |

## Schema Documentation

### {{TABLE_NAME}}

**Purpose**: {{TABLE_PURPOSE}}

**Table Type**: {{TABLE_TYPE}} (Core Entity / Reference / Junction / Log)

**Typical Record Count**: {{ESTIMATED_ROWS}}

**Growth Rate**: {{GROWTH_RATE}} (e.g., 1000 rows/month)

**Schema Diagram**:
```
{{TABLE_NAME}}
├── {{FIELD_NAME}} (PK)
├── {{FIELD_NAME}}
├── {{FIELD_NAME}} (FK → {{OTHER_TABLE}})
└── {{FIELD_NAME}}
```

**Key Queries**:
- {{QUERY_PURPOSE}}: `SELECT ... WHERE {{COMMON_FILTER}}`
- {{QUERY_PURPOSE}}: `JOIN {{TABLE_NAME}} WITH {{OTHER_TABLE}}`

**Performance Notes**:
- Indexed on: {{INDEXED_FIELDS}}
- Avoid queries with: {{PROBLEMATIC_PATTERNS}}

**Related Tables**:
- {{RELATED_TABLE_NAME}} ({{RELATIONSHIP_TYPE}})

## Maintenance Schedule

| Task | Frequency | Assigned To | Last Run | Next Run |
|------|-----------|------------|----------|----------|
| Analyze table statistics | {{FREQUENCY}} | {{ASSIGNEE}} | {{DATE}} | {{DATE}} |
| Rebuild fragmented indexes | {{FREQUENCY}} | {{ASSIGNEE}} | {{DATE}} | {{DATE}} |
| Purge old logs | {{FREQUENCY}} | {{ASSIGNEE}} | {{DATE}} | {{DATE}} |
| Backup verification | {{FREQUENCY}} | {{ASSIGNEE}} | {{DATE}} | {{DATE}} |

---

**Status**: {{TEMPLATE_STATUS}} (Ready for use)
