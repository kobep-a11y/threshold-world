# Integration Team Template

## Role
Connect and manage {{PROJECT_NAME}} with external services and third-party APIs. Configure authentication, implement service functions, handle errors, and maintain integration documentation for the Backend Team.

## Service Overview Table

| Service Name | Type | Purpose | Provider | Status | Integration Owner | Last Updated |
|--------------|------|---------|----------|--------|-------------------|--------------|
| {{SERVICE_NAME}} | {{SERVICE_TYPE}} | {{SERVICE_PURPOSE}} | {{PROVIDER}} | {{STATUS}} | {{OWNER}} | {{DATE}} |
| {{SERVICE_NAME}} | {{SERVICE_TYPE}} | {{SERVICE_PURPOSE}} | {{PROVIDER}} | {{STATUS}} | {{OWNER}} | {{DATE}} |

### Service Types
- **Payment**: Payment processing, billing, invoicing
- **Communication**: Email, SMS, push notifications
- **Analytics**: User tracking, metrics, monitoring
- **Storage**: File storage, CDN, backup
- **Authentication**: OAuth providers, identity management
- **Data**: External data sources, APIs
- **Utilities**: Rate limiting, caching, scheduling

## Active Tasks

| Task ID | Service | Integration Task | Type | Status | Assigned To | Due Date |
|---------|---------|------------------|------|--------|-------------|----------|
| {{TASK_001}} | {{SERVICE_NAME}} | {{INTEGRATION_TASK}} | {{TASK_TYPE}} | In Progress | {{ASSIGNEE}} | {{DATE}} |
| {{TASK_002}} | {{SERVICE_NAME}} | {{INTEGRATION_TASK}} | {{TASK_TYPE}} | Pending | {{ASSIGNEE}} | {{DATE}} |

### Integration Setup Format

```
Service: {{SERVICE_NAME}}
Provider: {{PROVIDER_NAME}}
Purpose: {{INTEGRATION_PURPOSE}}
Integration Lead: {{LEAD_NAME}}

Setup Steps:
1. {{SETUP_STEP_1}}
2. {{SETUP_STEP_2}}
3. {{SETUP_STEP_3}}

Configuration:
  - {{CONFIG_PARAMETER}}: {{CONFIG_VALUE}}
  - {{CONFIG_PARAMETER}}: {{CONFIG_VALUE}}

Testing:
  - Endpoint: {{TEST_ENDPOINT}}
  - Test Payload: {{TEST_PAYLOAD}}
  - Expected Response: {{EXPECTED_RESPONSE}}

Deployment Checklist:
  - [ ] Credentials secured in {{CREDENTIAL_STORAGE}}
  - [ ] Environment variables configured
  - [ ] Rate limits documented
  - [ ] Error handling implemented
  - [ ] Monitoring/alerts configured
  - [ ] Fallback strategy defined
  - [ ] Documentation complete
```

## OAuth Configuration Template

### {{SERVICE_NAME}} OAuth Setup

**OAuth Provider**: {{OAUTH_PROVIDER}}

**Application Name**: {{APPLICATION_NAME}}

**OAuth Version**: {{OAUTH_VERSION}} (OAuth 2.0, OpenID Connect)

**Flow Type**: {{FLOW_TYPE}} (Authorization Code, Client Credentials, PKCE)

#### Credentials

| Credential | Value | Environment | Last Rotated |
|-----------|-------|-------------|--------------|
| Client ID | {{CLIENT_ID}} | {{ENVIRONMENT}} | {{DATE}} |
| Client Secret | {{CLIENT_SECRET}} | {{ENVIRONMENT}} | {{DATE}} |
| Redirect URI | {{REDIRECT_URI}} | {{ENVIRONMENT}} | {{DATE}} |

#### Authorization Endpoints

| Endpoint | URL | Purpose |
|----------|-----|---------|
| Authorization | {{AUTHORIZATION_URL}} | User login and consent |
| Token | {{TOKEN_URL}} | Exchange code for token |
| Refresh | {{REFRESH_URL}} | Get new access token |
| Revoke | {{REVOKE_URL}} | Invalidate token |

#### Scopes Required

| Scope | Permission | Purpose | Default |
|-------|-----------|---------|---------|
| {{SCOPE_NAME}} | {{PERMISSION}} | {{PURPOSE}} | {{REQUIRED/OPTIONAL}} |
| {{SCOPE_NAME}} | {{PERMISSION}} | {{PURPOSE}} | {{REQUIRED/OPTIONAL}} |

#### Implementation Steps

1. **Request Authorization**
   ```
   GET {{AUTHORIZATION_URL}}
   ?client_id={{CLIENT_ID}}
   &redirect_uri={{REDIRECT_URI}}
   &response_type=code
   &scope={{SCOPES}}
   &state={{STATE_VALUE}}
   ```

2. **Exchange Code for Token**
   ```
   POST {{TOKEN_URL}}
   Authorization: Basic {{BASE64_ENCODED_CREDENTIALS}}
   Content-Type: application/x-www-form-urlencoded

   grant_type=authorization_code
   &code={{AUTHORIZATION_CODE}}
   &redirect_uri={{REDIRECT_URI}}
   ```

3. **Use Access Token**
   ```
   GET {{RESOURCE_URL}}
   Authorization: Bearer {{ACCESS_TOKEN}}
   ```

4. **Refresh Token (if expired)**
   ```
   POST {{TOKEN_URL}}
   Content-Type: application/x-www-form-urlencoded

   grant_type=refresh_token
   &refresh_token={{REFRESH_TOKEN}}
   &client_id={{CLIENT_ID}}
   &client_secret={{CLIENT_SECRET}}
   ```

#### Token Management

- **Token Expiry**: {{TOKEN_EXPIRY_TIME}} seconds
- **Refresh Token Expiry**: {{REFRESH_TOKEN_EXPIRY_TIME}} days
- **Token Storage**: {{TOKEN_STORAGE_METHOD}} (secure, httpOnly cookie, etc.)
- **Rotation Policy**: {{ROTATION_POLICY}}

## Service Functions Template

### {{SERVICE_NAME}} Integration

**Service Base URL**: `{{SERVICE_BASE_URL}}`

**API Version**: `{{API_VERSION}}`

**Authentication Type**: {{AUTH_TYPE}} (API Key, OAuth2, Bearer Token)

#### Function: {{FUNCTION_NAME}}

**Purpose**: {{FUNCTION_PURPOSE}}

**Method**: `{{HTTP_METHOD}} {{ENDPOINT_PATH}}`

**Required Parameters**:
- `{{PARAMETER_NAME}}` ({{PARAMETER_TYPE}}, {{REQUIRED/OPTIONAL}}): {{PARAMETER_DESCRIPTION}}

**Request Example**:
```javascript
// Function signature
async function {{FUNCTION_NAME}}({{PARAM1}}, {{PARAM2}}) {
  const response = await callService('{{SERVICE_NAME}}', {
    method: '{{HTTP_METHOD}}',
    path: '{{ENDPOINT_PATH}}',
    data: {
      {{REQUEST_FIELD}}: {{PARAM1}},
      {{REQUEST_FIELD}}: {{PARAM2}}
    }
  });
  return response;
}
```

**Success Response**:
```json
{
  "status": "success",
  "data": {
    "{{RESPONSE_FIELD}}": "{{FIELD_VALUE}}",
    "{{RESPONSE_FIELD}}": "{{FIELD_VALUE}}"
  }
}
```

**Error Responses**:
```json
{
  "status": "error",
  "code": "{{ERROR_CODE}}",
  "message": "{{ERROR_MESSAGE}}"
}
```

**Retry Logic**:
- {{CONDITION_FOR_RETRY}}: {{RETRY_STRATEGY}}
- Max retries: {{MAX_RETRIES}}
- Backoff: {{BACKOFF_STRATEGY}}

**Rate Limiting**:
- Limit: {{REQUESTS_PER_TIME_UNIT}}
- Window: {{TIME_WINDOW}}
- Headers: {{RATE_LIMIT_HEADERS}}

---

#### Function: {{FUNCTION_NAME}}

**Purpose**: {{FUNCTION_PURPOSE}}

**Method**: `{{HTTP_METHOD}} {{ENDPOINT_PATH}}`

**Required Parameters**:
- `{{PARAMETER_NAME}}` ({{PARAMETER_TYPE}}, {{REQUIRED/OPTIONAL}}): {{PARAMETER_DESCRIPTION}}

**Implementation**:
```javascript
async function {{FUNCTION_NAME}}({{PARAMETERS}}) {
  try {
    const response = await callService('{{SERVICE_NAME}}', {
      method: '{{HTTP_METHOD}}',
      path: '{{ENDPOINT_PATH}}',
      data: {{REQUEST_BODY}},
      headers: {
        'Authorization': `Bearer {{TOKEN_VAR}}`
      }
    });
    return response.data;
  } catch (error) {
    handleServiceError('{{SERVICE_NAME}}', error);
  }
}
```

## Service Credentials Reference Table

| Service | Environment | Credential Type | Value/Reference | Rotation Schedule | Last Rotated | Owner |
|---------|------------|-----------------|-----------------|-------------------|-------------|-------|
| {{SERVICE_NAME}} | {{ENVIRONMENT}} | {{CREDENTIAL_TYPE}} | {{VAULT_REF}} | {{SCHEDULE}} | {{DATE}} | {{OWNER}} |
| {{SERVICE_NAME}} | {{ENVIRONMENT}} | {{CREDENTIAL_TYPE}} | {{VAULT_REF}} | {{SCHEDULE}} | {{DATE}} | {{OWNER}} |

**Credential Storage**: {{CREDENTIAL_VAULT_SYSTEM}} (AWS Secrets Manager, Vault, etc.)

**Access Control**: {{ACCESS_CONTROL_METHOD}} (IAM roles, service accounts, etc.)

**Rotation Policy**: {{ROTATION_POLICY}} (e.g., quarterly, upon team changes)

## Error Handling Tables

### Common Integration Errors

| Error Code | HTTP Status | Meaning | Cause | Recovery |
|-----------|-----------|---------|-------|----------|
| {{ERROR_CODE}} | {{STATUS}} | {{ERROR_MEANING}} | {{TYPICAL_CAUSE}} | {{RECOVERY_ACTION}} |
| {{ERROR_CODE}} | {{STATUS}} | {{ERROR_MEANING}} | {{TYPICAL_CAUSE}} | {{RECOVERY_ACTION}} |

### {{SERVICE_NAME}} Error Handling

| Error Code | Error Message | Status Code | Handling Strategy | Retry? | Fallback |
|-----------|---------------|------------|-------------------|--------|----------|
| {{SERVICE_ERROR_CODE}} | {{ERROR_MESSAGE}} | {{HTTP_STATUS}} | {{HANDLING_STRATEGY}} | {{YES/NO}} | {{FALLBACK_ACTION}} |
| {{SERVICE_ERROR_CODE}} | {{ERROR_MESSAGE}} | {{HTTP_STATUS}} | {{HANDLING_STRATEGY}} | {{YES/NO}} | {{FALLBACK_ACTION}} |

### Retry Policy

| Scenario | Retry Count | Backoff Strategy | Max Wait Time |
|----------|------------|------------------|--------------|
| {{SCENARIO}} ({{ERROR_CONDITION}}) | {{RETRY_COUNT}} | {{BACKOFF_TYPE}} | {{MAX_WAIT}} |
| {{SCENARIO}} ({{ERROR_CONDITION}}) | {{RETRY_COUNT}} | {{BACKOFF_TYPE}} | {{MAX_WAIT}} |

### Fallback Strategies

| Service | Failure Scenario | Fallback Action | User Impact | Priority |
|---------|-----------------|-----------------|-------------|----------|
| {{SERVICE_NAME}} | {{FAILURE_SCENARIO}} | {{FALLBACK_ACTION}} | {{USER_IMPACT}} | {{PRIORITY}} |
| {{SERVICE_NAME}} | {{FAILURE_SCENARIO}} | {{FALLBACK_ACTION}} | {{USER_IMPACT}} | {{PRIORITY}} |

## Integration Status Monitoring

### Health Check Configuration

| Service | Health Check URL | Interval | Alert Threshold | Status | Last Check |
|---------|------------------|----------|-----------------|--------|-----------|
| {{SERVICE_NAME}} | {{HEALTH_CHECK_URL}} | {{INTERVAL}} | {{THRESHOLD}} | {{STATUS}} | {{DATE}} |
| {{SERVICE_NAME}} | {{HEALTH_CHECK_URL}} | {{INTERVAL}} | {{THRESHOLD}} | {{STATUS}} | {{DATE}} |

### Monitoring & Alerts

- **Uptime Target**: {{UPTIME_TARGET}} (e.g., 99.9%)
- **Response Time Target**: {{RESPONSE_TIME_TARGET}} ms
- **Alert Channel**: {{ALERT_CHANNEL}} (Slack, PagerDuty, etc.)
- **Escalation Policy**: {{ESCALATION_POLICY}}

## Integration Testing Checklist

- [ ] Service credentials configured in {{ENVIRONMENT}}
- [ ] Authentication tested and successful
- [ ] All endpoints tested with sample requests
- [ ] Error responses handled gracefully
- [ ] Rate limiting respected and implemented
- [ ] Retry logic tested for transient failures
- [ ] Fallback strategies verified
- [ ] Logging configured for debugging
- [ ] Monitoring and alerts set up
- [ ] Load testing completed for {{EXPECTED_LOAD}}
- [ ] Security review completed
- [ ] Documentation updated for Backend Team

## Handoff to Backend Team

Before integrating services into main application:

- [ ] Integration functions ready in {{CODE_LOCATION}}
- [ ] Function documentation with examples provided
- [ ] Error codes and handling documented
- [ ] Rate limits and quota requirements documented
- [ ] Service dependencies listed
- [ ] Monitoring/alerting configured
- [ ] Sample requests and responses provided
- [ ] Credentials securely configured per environment
- [ ] Fallback strategies implemented
- [ ] API documentation from service provider shared

---

**Status**: {{TEMPLATE_STATUS}} (Ready for use)
