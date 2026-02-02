# Backend Team Template

## Role
Build and maintain {{PROJECT_NAME}} API routes, implement business logic, and ensure data flows correctly between the database and frontend.

## Tech Stack
- **Runtime**: {{RUNTIME_ENVIRONMENT}} (e.g., Node.js, Python, Java)
- **Framework**: {{BACKEND_FRAMEWORK}} (e.g., Express, Flask, Spring Boot)
- **API Standard**: {{API_STANDARD}} (e.g., REST, GraphQL)
- **Database Driver**: {{DATABASE_DRIVER}}
- **Authentication**: {{AUTH_METHOD}} (e.g., JWT, OAuth2)
- **Validation Library**: {{VALIDATION_LIBRARY}}

## Active Tasks

| Task ID | Endpoint | Method | Description | Status | Assigned To | Due Date |
|---------|----------|--------|-------------|--------|-------------|----------|
| {{TASK_001}} | {{ENDPOINT_PATH}} | {{HTTP_METHOD}} | {{ENDPOINT_DESCRIPTION}} | In Progress | {{ASSIGNEE}} | {{DATE}} |
| {{TASK_002}} | {{ENDPOINT_PATH}} | {{HTTP_METHOD}} | {{ENDPOINT_DESCRIPTION}} | Pending | {{ASSIGNEE}} | {{DATE}} |

### Endpoint Template
```
Route: {{ENDPOINT_PATH}}
Method: {{HTTP_METHOD}}
Description: {{ENDPOINT_DESCRIPTION}}
Request Body:
{
  {{REQUEST_FIELD}}: {{FIELD_TYPE}},
  {{REQUEST_FIELD}}: {{FIELD_TYPE}}
}
Response (Success - 200):
{
  {{RESPONSE_FIELD}}: {{FIELD_TYPE}},
  {{RESPONSE_FIELD}}: {{FIELD_TYPE}}
}
Error Responses:
- 400: {{ERROR_DESCRIPTION}}
- 401: {{ERROR_DESCRIPTION}}
- 500: {{ERROR_DESCRIPTION}}
```

## New Types Required

Define new data types/models needed for {{PROJECT_NAME}}:

```typescript
// Type: {{TYPE_NAME}}
interface {{TYPE_NAME}} {
  {{FIELD_NAME}}: {{FIELD_TYPE}};
  {{FIELD_NAME}}: {{FIELD_TYPE}};
}

// Type: {{TYPE_NAME}}
enum {{ENUM_NAME}} {
  {{ENUM_VALUE}} = "{{ENUM_VALUE}}",
  {{ENUM_VALUE}} = "{{ENUM_VALUE}}"
}
```

## Functions to Add

| Function Name | Parameters | Returns | Purpose | Status |
|---------------|-----------|---------|---------|--------|
| {{FUNCTION_NAME}} | {{PARAM}}: {{TYPE}} | {{RETURN_TYPE}} | {{PURPOSE}} | TODO |
| {{FUNCTION_NAME}} | {{PARAM}}: {{TYPE}} | {{RETURN_TYPE}} | {{PURPOSE}} | TODO |

### Function Template
```
Function: {{FUNCTION_NAME}}
Purpose: {{FUNCTION_PURPOSE}}
Parameters:
  - {{PARAMETER_NAME}} ({{PARAMETER_TYPE}}): {{PARAMETER_DESCRIPTION}}
Dependencies: {{DEPENDENT_FUNCTIONS_OR_SERVICES}}
Error Handling:
  - {{ERROR_CONDITION}}: {{HANDLING_STRATEGY}}
```

## Acceptance Criteria

- [ ] All endpoints defined in Active Tasks are implemented
- [ ] Request/response validation is complete for {{VALIDATION_SCOPE}}
- [ ] All error cases return appropriate HTTP status codes
- [ ] Business logic for {{CORE_LOGIC}} is implemented and tested
- [ ] Database queries are optimized (no N+1 queries)
- [ ] Rate limiting configured for {{RATE_LIMITED_ENDPOINTS}}
- [ ] All functions have appropriate logging
- [ ] Code follows {{PROJECT_NAME}} style guide
- [ ] No console.log/print statements in production code
- [ ] Database transactions implemented where required

## Handoff Checklist (to UI Team)

Before handing off API to UI Team, verify:

- [ ] API documentation generated and shared
- [ ] All endpoints tested with Postman/Insomnia
- [ ] Sample request/response payloads provided
- [ ] Authentication flow documented
- [ ] Error response format documented
- [ ] Rate limits documented
- [ ] Pagination format documented (if applicable)
- [ ] Deployment endpoint(s) provided
- [ ] API testing performed in {{STAGING_ENVIRONMENT}}
- [ ] Database seeding data provided for UI testing

## API Documentation Template

### {{ENDPOINT_NAME}}

**Endpoint**: `{{HTTP_METHOD}} /api/{{API_VERSION}}/{{RESOURCE}}`

**Description**: {{ENDPOINT_DESCRIPTION}}

**Authentication**: {{AUTH_REQUIRED}} ({{AUTH_TYPE}})

**Request Parameters**:
- `{{PARAMETER_NAME}}` ({{PARAMETER_TYPE}}, {{REQUIRED_OR_OPTIONAL}}): {{PARAMETER_DESCRIPTION}}

**Request Headers**:
```
Content-Type: application/json
Authorization: Bearer {{TOKEN_FORMAT}}
```

**Request Body Example**:
```json
{
  "{{FIELD}}": "{{EXAMPLE_VALUE}}",
  "{{FIELD}}": {{EXAMPLE_VALUE}}
}
```

**Success Response ({{STATUS_CODE}})**:
```json
{
  "{{RESPONSE_FIELD}}": "{{EXAMPLE_VALUE}}",
  "{{RESPONSE_FIELD}}": {{EXAMPLE_VALUE}}
}
```

**Error Response ({{STATUS_CODE}})**:
```json
{
  "error": "{{ERROR_CODE}}",
  "message": "{{ERROR_MESSAGE}}",
  "details": "{{ERROR_DETAILS}}"
}
```

**Example cURL Request**:
```bash
curl -X {{HTTP_METHOD}} \
  -H "Authorization: Bearer {{TOKEN}}" \
  -H "Content-Type: application/json" \
  -d '{{REQUEST_BODY_JSON}}' \
  {{API_ENDPOINT}}
```

---

**Status**: {{TEMPLATE_STATUS}} (Ready for use)
