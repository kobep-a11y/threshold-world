# QA Team Template

## Role
Verify all {{PROJECT_NAME}} deliverables meet quality standards. Conduct thorough testing of API endpoints, UI components, integrations, and database operations. Identify, document, and track bugs. Provide sign-off approval for releases.

## QA Philosophy

The QA Team operates on five core principles:

1. **Comprehensive Coverage**: Test all user paths, edge cases, and error scenarios
2. **Shift-Left Testing**: Collaborate with teams early to prevent defects rather than find them late
3. **Documentation First**: All tests documented before execution
4. **Reproducibility**: Every bug must be reproducible with clear steps
5. **Continuous Improvement**: Automated tests increase, manual testing decreases over time

## Verification Checklist Template

### General Requirements

- [ ] Feature implemented per {{SPECIFICATION_DOCUMENT}}
- [ ] Code follows {{PROJECT_NAME}} style guide
- [ ] No console errors in browser/logs
- [ ] No security vulnerabilities identified
- [ ] Performance acceptable per {{PERFORMANCE_CRITERIA}}
- [ ] Accessibility compliance verified ({{WCAG_LEVEL}})
- [ ] Database consistency maintained
- [ ] All error cases handled gracefully

### Functional Requirements

- [ ] {{REQUIREMENT_1}} verified
- [ ] {{REQUIREMENT_2}} verified
- [ ] {{REQUIREMENT_3}} verified

### Data Requirements

- [ ] Valid data accepted correctly
- [ ] Invalid data rejected with clear error message
- [ ] {{FIELD_NAME}} validation: {{VALIDATION_RULE}}
- [ ] {{FIELD_NAME}} validation: {{VALIDATION_RULE}}

### UI/UX Requirements

- [ ] Layout correct on {{SUPPORTED_DEVICES}}
- [ ] {{COMPONENT_NAME}} displays correctly
- [ ] User feedback provided for {{ACTION_TYPE}}
- [ ] Loading states visible
- [ ] Error messages user-friendly and actionable

## Test Plan Template for API Endpoints

### {{ENDPOINT_NAME}}

**Endpoint**: `{{HTTP_METHOD}} /api/{{API_VERSION}}/{{RESOURCE}}`

**Owner**: {{BACKEND_TEAM_MEMBER}}

#### Positive Tests

| Test ID | Input | Expected Output | Status | Notes |
|---------|-------|-----------------|--------|-------|
| {{TEST_001}} | Valid {{INPUT_TYPE}}: {{SAMPLE_INPUT}} | {{EXPECTED_RESPONSE}} ({{STATUS_CODE}}) | PASS | {{NOTES}} |
| {{TEST_002}} | Valid {{INPUT_TYPE}}: {{SAMPLE_INPUT}} | {{EXPECTED_RESPONSE}} ({{STATUS_CODE}}) | PASS | {{NOTES}} |

#### Negative Tests

| Test ID | Input | Expected Behavior | Status | Notes |
|---------|-------|-------------------|--------|-------|
| {{TEST_N01}} | Missing required field: {{FIELD_NAME}} | {{ERROR_RESPONSE}} ({{STATUS_CODE}}) | PASS | {{NOTES}} |
| {{TEST_N02}} | Invalid {{FIELD_NAME}} format: {{INVALID_VALUE}} | {{ERROR_RESPONSE}} ({{STATUS_CODE}}) | PASS | {{NOTES}} |
| {{TEST_N03}} | Authentication token missing/invalid | 401 Unauthorized | PASS | {{NOTES}} |

#### Edge Cases

| Test ID | Scenario | Expected Behavior | Status | Notes |
|---------|----------|-------------------|--------|-------|
| {{TEST_E01}} | {{EDGE_CASE_SCENARIO}} | {{EXPECTED_RESPONSE}} | PASS | {{NOTES}} |
| {{TEST_E02}} | {{EDGE_CASE_SCENARIO}} | {{EXPECTED_RESPONSE}} | PASS | {{NOTES}} |

#### Load Tests

| Test ID | Load Scenario | Expected Behavior | Status | Notes |
|---------|---------------|-------------------|--------|-------|
| {{TEST_L01}} | {{NUMBER_OF_REQUESTS}} concurrent requests | Response time < {{TIME_LIMIT}}ms | PASS | {{NOTES}} |

## UI Component Test Template

### {{COMPONENT_NAME}}

**Owner**: {{UI_TEAM_MEMBER}}

**Component Path**: `{{COMPONENT_PATH}}`

#### Rendering Tests

- [ ] Component renders without errors
- [ ] All props passed correctly
- [ ] Default props applied when none provided
- [ ] {{COMPONENT_NAME}} appears on {{PAGES_WHERE_USED}}

#### Interaction Tests

- [ ] Click/tap events trigger correctly
- [ ] Hover states visible on desktop
- [ ] Focus states visible for keyboard navigation
- [ ] Form inputs capture values correctly
- [ ] {{INTERACTIVE_ELEMENT}} responds to user action

#### State Tests

- [ ] Default state displays correctly: {{DEFAULT_STATE}}
- [ ] Disabled state appears and functions: {{DISABLED_STATE}}
- [ ] Loading state visible: {{LOADING_STATE}}
- [ ] Error state displays with message: {{ERROR_STATE}}
- [ ] Success state visible: {{SUCCESS_STATE}}

#### Data Tests

- [ ] {{COMPONENT_NAME}} displays data from {{DATA_SOURCE}}
- [ ] Empty state handled gracefully
- [ ] Large data sets display: {{LARGE_DATA_TEST}}
- [ ] {{DYNAMIC_CONTENT}} updates in real-time

#### Responsive Design Tests

| Device | Viewport | Issues | Status |
|--------|----------|--------|--------|
| Desktop | {{DESKTOP_WIDTH}} | {{ISSUES}} | PASS |
| Tablet | {{TABLET_WIDTH}} | {{ISSUES}} | PASS |
| Mobile | {{MOBILE_WIDTH}} | {{ISSUES}} | PASS |

#### Accessibility Tests

- [ ] Keyboard navigation: Tab order logical
- [ ] Screen reader: All content announced
- [ ] Color contrast: WCAG {{LEVEL}} met
- [ ] ARIA labels: Present where needed
- [ ] Error messages: Announced to screen readers

## Error Handling Tests

### API Error Scenarios

| Error Code | Trigger Condition | Expected Response | Test Status |
|-----------|------------------|-------------------|------------|
| 400 | {{BAD_REQUEST_CONDITION}} | Clear error message about {{ERROR_DETAIL}} | PASS |
| 401 | {{UNAUTHORIZED_CONDITION}} | Redirect to login/refresh token | PASS |
| 403 | {{FORBIDDEN_CONDITION}} | "Access denied" message | PASS |
| 404 | {{NOT_FOUND_CONDITION}} | "Resource not found" message | PASS |
| 409 | {{CONFLICT_CONDITION}} | {{CONFLICT_RESOLUTION_HINT}} | PASS |
| 422 | {{VALIDATION_FAILURE_CONDITION}} | Field-level validation errors | PASS |
| 429 | {{RATE_LIMIT_CONDITION}} | Rate limit exceeded message | PASS |
| 500 | {{SERVER_ERROR_CONDITION}} | Generic error, logged for debugging | PASS |

### Database Error Scenarios

- [ ] Database connection fails: User sees graceful error message
- [ ] Data validation fails: Error explained to user
- [ ] Transaction rolls back: Data consistency maintained
- [ ] Concurrent update conflict: User notified, conflict resolution offered

### UI Error Handling

- [ ] Error messages are visible and readable
- [ ] Error messages suggest action to resolve
- [ ] Error state doesn't crash component
- [ ] User can recover from error state

## Bug Report Template

### Bug: {{BUG_TITLE}}

**Bug ID**: {{BUG_ID}}

**Severity**: {{SEVERITY}} (Critical / High / Medium / Low)

**Component**: {{COMPONENT_OR_FEATURE}}

**Environment**: {{ENVIRONMENT}} (Development / Staging / Production)

**Browser/Device**: {{BROWSER_VERSION}} / {{DEVICE_TYPE}}

**Assigned To**: {{ASSIGNEE}}

#### Description

{{BUG_DESCRIPTION}}

#### Steps to Reproduce

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}
4. {{STEP_4}}

#### Expected Behavior

{{EXPECTED_BEHAVIOR}}

#### Actual Behavior

{{ACTUAL_BEHAVIOR}}

#### Screenshots/Logs

{{ATTACHMENT_OR_LOG_REFERENCE}}

#### Root Cause (if identified)

{{ROOT_CAUSE_ANALYSIS}}

#### Resolution Steps

1. {{RESOLUTION_STEP_1}}
2. {{RESOLUTION_STEP_2}}

#### Test Sign-Off

- [ ] Bug reproduced by QA
- [ ] Fix verified in {{ENVIRONMENT}}
- [ ] Regression tests passed
- [ ] Closed by: {{QA_TEAM_MEMBER}}

## Test Environment Checklist

### Environment: {{ENVIRONMENT_NAME}}

- [ ] {{ENVIRONMENT_NAME}} database seeded with test data
- [ ] Test user accounts created
- [ ] {{EXTERNAL_SERVICE_1}} mock/staging connection verified
- [ ] {{EXTERNAL_SERVICE_2}} mock/staging connection verified
- [ ] API endpoints accessible
- [ ] UI deployed and accessible at {{URL}}
- [ ] Authentication/login tested
- [ ] Logs available for review
- [ ] Performance baseline established
- [ ] Known issues documented

## Sign-Off Criteria

Release requires QA sign-off confirming:

- [ ] All test cases executed
- [ ] All critical tests passed
- [ ] No critical or high-severity bugs remaining
- [ ] {{FEATURE_OR_RELEASE}} meets acceptance criteria
- [ ] Performance acceptable for {{LOAD_EXPECTATIONS}}
- [ ] Security reviewed ({{SECURITY_FOCUS_AREAS}})
- [ ] Data integrity verified
- [ ] {{THIRD_PARTY_INTEGRATIONS}} functioning correctly
- [ ] Backup/recovery tested
- [ ] Documentation complete and accurate

**QA Sign-Off By**: {{QA_LEAD_NAME}}

**Date**: {{SIGN_OFF_DATE}}

**Status**: APPROVED / APPROVED WITH CONDITIONS / REJECTED

## Bug Tracker Table

| Bug ID | Title | Severity | Status | Component | Assigned To | Created | Due |
|--------|-------|----------|--------|-----------|------------|---------|-----|
| {{BUG_ID}} | {{BUG_TITLE}} | {{SEVERITY}} | {{STATUS}} | {{COMPONENT}} | {{ASSIGNEE}} | {{DATE}} | {{DATE}} |
| {{BUG_ID}} | {{BUG_TITLE}} | {{SEVERITY}} | {{STATUS}} | {{COMPONENT}} | {{ASSIGNEE}} | {{DATE}} | {{DATE}} |

### Bug Status Legend
- **Open**: Newly reported, not yet reviewed
- **Assigned**: Under investigation by developer
- **In Progress**: Developer working on fix
- **Ready for QA**: Fix completed, awaiting verification
- **Verified**: QA confirmed fix works
- **Closed**: Bug resolved and deployed
- **Deferred**: Postponed to future release
- **Won't Fix**: Intentionally not addressed

---

**Status**: {{TEMPLATE_STATUS}} (Ready for use)
