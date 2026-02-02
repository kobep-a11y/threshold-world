# UI Team — {{PROJECT_NAME}}

**Frontend Development | Component Architecture | User Experience**

## Role

The UI Team builds React components and frontend interfaces for {{PROJECT_NAME}}, responsible for:
- Implementing React components and feature UIs
- Translating designs into functional code
- Building and maintaining the component library
- Ensuring accessibility and mobile responsiveness
- Optimizing frontend performance
- Establishing code standards and best practices

---

## Tech Stack

**Framework:** {{FRAMEWORK}} ({{VERSION}})
**State Management:** {{STATE_MANAGEMENT}}
**Styling:** {{CSS_APPROACH}}
**Build Tool:** {{BUILD_TOOL}}
**Package Manager:** {{PACKAGE_MANAGER}}
**Testing:** {{TEST_FRAMEWORK}}
**Linting:** {{LINTER}}

### Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| {{PACKAGE_NAME}} | {{VERSION}} | {{PURPOSE}} |
| {{PACKAGE_NAME}} | {{VERSION}} | {{PURPOSE}} |
| {{PACKAGE_NAME}} | {{VERSION}} | {{PURPOSE}} |

---

## Design System

### Color Palette

**Primary Colors:**

| Name | Hex | Usage |
|------|-----|-------|
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |

**Secondary Colors:**

| Name | Hex | Usage |
|------|-----|-------|
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |

**Neutral Colors:**

| Name | Hex | Usage |
|------|-----|-------|
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |
| {{COLOR_NAME}} | {{HEX}} | {{USAGE}} |

### Typography

| Element | Font Family | Size | Weight | Line Height |
|---------|------------|------|--------|------------|
| H1 | {{FONT}} | {{SIZE}} | {{WEIGHT}} | {{HEIGHT}} |
| H2 | {{FONT}} | {{SIZE}} | {{WEIGHT}} | {{HEIGHT}} |
| Body | {{FONT}} | {{SIZE}} | {{WEIGHT}} | {{HEIGHT}} |
| Small | {{FONT}} | {{SIZE}} | {{WEIGHT}} | {{HEIGHT}} |

### Spacing Scale

```
xs: 4px
sm: 8px
md: 16px
lg: 24px
xl: 32px
xxl: 48px
```

### Badge & Status Colors

**Badge Variants:**

| Variant | Background | Text | Use Case |
|---------|-----------|------|----------|
| {{VARIANT}} | {{COLOR}} | {{COLOR}} | {{USE_CASE}} |
| {{VARIANT}} | {{COLOR}} | {{COLOR}} | {{USE_CASE}} |
| {{VARIANT}} | {{COLOR}} | {{COLOR}} | {{USE_CASE}} |

**Status Indicators:**

| Status | Color | Icon | Meaning |
|--------|-------|------|---------|
| {{STATUS}} | {{COLOR}} | {{ICON}} | {{MEANING}} |
| {{STATUS}} | {{COLOR}} | {{ICON}} | {{MEANING}} |
| {{STATUS}} | {{COLOR}} | {{ICON}} | {{MEANING}} |

---

## Active Tasks

### Component Specification Template

**Component Name:** `{{COMPONENT_NAME}}`

**Status:** {{STATUS_PLANNING_DESIGN_IN_PROGRESS_REVIEW_COMPLETE}}
**Owner:** {{DEVELOPER_NAME}}
**Priority:** {{P0_P1_P2}}
**Target Completion:** {{TARGET_DATE}}

**Component Path:** `src/components/{{FOLDER}}/{{COMPONENT_NAME}}.tsx`

**One-Line Description:**
```
{{BRIEF_FUNCTIONAL_DESCRIPTION}}
```

**Purpose & Context:**
```
{{WHY_IS_THIS_COMPONENT_NEEDED}}
```

**Props Interface:**

```typescript
export interface {{COMPONENT_NAME}}Props {
  /**
   * {{PROP_DESCRIPTION}}
   */
  {{PROP_NAME}}?: {{TYPE}};

  /**
   * {{PROP_DESCRIPTION}}
   */
  {{PROP_NAME}}: {{TYPE}};

  /**
   * {{PROP_DESCRIPTION}}
   * @default "{{DEFAULT_VALUE}}"
   */
  {{PROP_NAME}}?: {{TYPE}};

  // Event handlers
  on{{EVENT_NAME}}?: ({{PARAM}}: {{TYPE}}) => void;
  on{{EVENT_NAME}}?: ({{PARAM}}: {{TYPE}}) => void;
}
```

**Component Usage Example:**

```tsx
import { {{COMPONENT_NAME}} } from '@/components/{{FOLDER}}';

export function Example() {
  return (
    <{{COMPONENT_NAME}}
      {{REQUIRED_PROP}}="{{VALUE}}"
      {{PROP_NAME}}="{{VALUE}}"
      on{{EVENT_NAME}}={({{PARAM}}) => {
        // Handle event
      }}
    />
  );
}
```

**Styling:**
- CSS-in-JS Library: {{LIBRARY}}
- Themed: {{YES_NO}}
- Responsive: {{YES_NO}}

**States & Variants:**

| Variant | Props | Visual Difference | Example |
|---------|-------|-------------------|---------|
| {{VARIANT}} | {{PROPS}} | {{DIFFERENCE}} | {{EXAMPLE}} |
| {{VARIANT}} | {{PROPS}} | {{DIFFERENCE}} | {{EXAMPLE}} |
| {{VARIANT}} | {{PROPS}} | {{DIFFERENCE}} | {{EXAMPLE}} |

**Accessibility Requirements:**

- [ ] Semantic HTML used
- [ ] ARIA labels added where needed
- [ ] Keyboard navigation supported
- [ ] Focus states visible
- [ ] Color contrast meets WCAG {{STANDARD}}
- [ ] Screen reader tested

**Browser Support:**

- {{BROWSER}} {{VERSION}}+
- {{BROWSER}} {{VERSION}}+
- {{BROWSER}} {{VERSION}}+

**Testing Requirements:**

- [ ] Unit tests: {{COVERAGE}}%
- [ ] Integration tests: {{COVERAGE}}%
- [ ] Visual regression tests: {{YES_NO}}
- [ ] Accessibility audit: {{AUTOMATED_MANUAL}}

**Dependencies:**

| Component | Type | Notes |
|-----------|------|-------|
| {{DEP_NAME}} | {{TYPE}} | {{NOTES}} |
| {{DEP_NAME}} | {{TYPE}} | {{NOTES}} |

**Open Questions:**

- {{QUESTION_1}}
- {{QUESTION_2}}
- {{QUESTION_3}}

**Notes:**

```
{{ADDITIONAL_CONTEXT}}
```

---

## Component Library

**Library Status:** {{NUM_COMPONENTS}} components | {{NUM_IN_PROGRESS}} in progress

### Published Components

| Component | Status | Last Updated | Usage | Notes |
|-----------|--------|--------------|-------|-------|
| {{COMPONENT}} | {{STATUS}} | {{DATE}} | {{APPS}} | {{NOTES}} |
| {{COMPONENT}} | {{STATUS}} | {{DATE}} | {{APPS}} | {{NOTES}} |
| {{COMPONENT}} | {{STATUS}} | {{DATE}} | {{APPS}} | {{NOTES}} |

### Component Hierarchy

```
components/
├── atoms/
│   ├── Button
│   ├── Input
│   ├── Label
│   └── Badge
├── molecules/
│   ├── SearchBar
│   ├── Modal
│   ├── Card
│   └── Dropdown
├── organisms/
│   ├── Header
│   ├── Sidebar
│   ├── Footer
│   └── Form
└── templates/
    ├── PageLayout
    ├── AuthLayout
    └── DashboardLayout
```

### Component Inventory

| Component | Type | Status | Tests | a11y | Mobile |
|-----------|------|--------|-------|------|--------|
| {{COMPONENT}} | {{TYPE}} | {{STATUS}} | {{YES_NO}} | {{YES_NO}} | {{YES_NO}} |
| {{COMPONENT}} | {{TYPE}} | {{STATUS}} | {{YES_NO}} | {{YES_NO}} | {{YES_NO}} |

---

## Mobile Considerations

### Responsive Breakpoints

| Device | Breakpoint | Min Width | Max Width | Primary Focus |
|--------|-----------|-----------|-----------|---------------|
| {{DEVICE}} | {{BREAKPOINT}} | {{MIN}} | {{MAX}} | {{FOCUS}} |
| {{DEVICE}} | {{BREAKPOINT}} | {{MIN}} | {{MAX}} | {{FOCUS}} |
| {{DEVICE}} | {{BREAKPOINT}} | {{MIN}} | {{MAX}} | {{FOCUS}} |

### Mobile Priorities

**High Priority:**
- {{PRIORITY_1}}
- {{PRIORITY_2}}
- {{PRIORITY_3}}

**Medium Priority:**
- {{PRIORITY_1}}
- {{PRIORITY_2}}

**Low Priority:**
- {{PRIORITY_1}}

### Mobile Testing Checklist

- [ ] Touch targets minimum 44x44px
- [ ] Tap interactions responsive (no 300ms delay issues)
- [ ] Scrolling smooth and performant
- [ ] Form inputs touch-optimized
- [ ] Bottom navigation accessible
- [ ] Tested on {{TEST_DEVICES}}

### Mobile Performance Targets

| Metric | Target | Current |
|--------|--------|---------|
| Lighthouse Mobile Score | {{SCORE}} | {{SCORE}} |
| First Contentful Paint | {{TIME}}ms | {{TIME}}ms |
| Largest Contentful Paint | {{TIME}}ms | {{TIME}}ms |
| Cumulative Layout Shift | {{VALUE}} | {{VALUE}} |

---

## Handoff Checklist

**Used before:** Passing component/feature from one phase to another or team to another

### Pre-Handoff Review

**Component/Feature:** {{NAME}}
**From:** {{TEAM_OR_PHASE}}
**To:** {{TEAM_OR_PHASE}}
**Date:** {{HANDOFF_DATE}}

**Code Quality:**

- [ ] All required tests passing ({{TEST_COUNT}} tests)
- [ ] Code coverage at {{COVERAGE}}%+
- [ ] Linting passes with zero warnings
- [ ] TypeScript strict mode compiles
- [ ] No console errors or warnings in development
- [ ] Performance profiling reviewed
- [ ] Bundle size impact documented

**Documentation:**

- [ ] Component/function JSDoc comments complete
- [ ] Storybook stories created ({{NUM_STORIES}})
- [ ] README with usage examples provided
- [ ] Props documentation complete
- [ ] Type definitions exported and documented
- [ ] Known limitations documented
- [ ] Migration guide provided (if applicable)

**Accessibility:**

- [ ] WCAG 2.1 Level AA compliant
- [ ] Screen reader tested with {{READER}}
- [ ] Keyboard navigation tested
- [ ] Color contrast verified (WAVE/Axe)
- [ ] Focus management verified
- [ ] ARIA labels appropriately applied

**Browser & Device Testing:**

- [ ] Tested on Chrome {{VERSION}}+
- [ ] Tested on Firefox {{VERSION}}+
- [ ] Tested on Safari {{VERSION}}+
- [ ] Tested on Edge {{VERSION}}+
- [ ] Mobile testing completed ({{DEVICES}})
- [ ] Touch interactions verified
- [ ] Responsive design verified

**Feature Completion:**

- [ ] All acceptance criteria met
- [ ] Required features implemented: {{FEATURE_1}}, {{FEATURE_2}}
- [ ] No P0 bugs remaining
- [ ] Error states handled
- [ ] Loading states implemented
- [ ] Empty states handled

**Design Compliance:**

- [ ] Matches design system colors
- [ ] Matches design system typography
- [ ] Spacing/padding per design system
- [ ] Icons match design language
- [ ] Animations/transitions match spec
- [ ] Design review approved

**Performance:**

- [ ] Component renders < {{TIME}}ms
- [ ] No unnecessary re-renders
- [ ] Memoization applied where needed
- [ ] Lazy loading implemented (if applicable)
- [ ] Image optimization reviewed
- [ ] Bundle size impact < {{SIZE_LIMIT}}KB

**Security:**

- [ ] No XSS vulnerabilities
- [ ] Input sanitization applied
- [ ] No sensitive data in logs
- [ ] Security review completed
- [ ] Dependencies audited (npm audit clean)

**Integration:**

- [ ] API integration complete
- [ ] State management setup
- [ ] Error boundaries implemented
- [ ] Loading states connected
- [ ] Environment variables configured
- [ ] Feature flags implemented (if needed)

**Release Notes:**

- [ ] Changes documented
- [ ] Breaking changes noted
- [ ] New features listed
- [ ] Bug fixes listed
- [ ] Deprecations noted
- [ ] Migration guide provided (if needed)

### Sign-Off

**Reviewed By:** {{REVIEWER_NAME}}
**Approved By:** {{APPROVER_NAME}}
**Date Approved:** {{DATE}}

**Sign-Off Comments:**
```
{{ADDITIONAL_NOTES}}
```

**Known Issues:**
- {{ISSUE_1}}
- {{ISSUE_2}}

**Next Steps:**
- [ ] {{ACTION_ITEM_1}}
- [ ] {{ACTION_ITEM_2}}

---

## Development Standards

### Code Style Guide

**File Naming:**
- Components: PascalCase (`Button.tsx`)
- Utilities: camelCase (`formatDate.ts`)
- Styles: camelCase or kebab-case based on tool
- Tests: `{{FileName}}.test.tsx`

**Component Structure:**

```typescript
// imports
import React, { useState } from 'react';
import styles from './Component.module.css';

// types
export interface ComponentProps {
  // props here
}

// component
export const Component: React.FC<ComponentProps> = ({
  // destructured props
}) => {
  // hooks
  const [state, setState] = useState();

  // handlers
  const handleEvent = () => {
    // handle event
  };

  // render
  return (
    <div>
      {/* JSX */}
    </div>
  );
};

// exports
export default Component;
```

**Commit Message Format:**

```
type(scope): description

[optional body]

[optional footer]
```

Example: `feat(Button): add loading state support`

---

**Last Updated:** {{CURRENT_DATE}}
**Next Review:** {{NEXT_REVIEW_DATE}}
