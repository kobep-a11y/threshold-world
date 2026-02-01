# Threshold Documentation Index

> Strategic and technical documentation for Threshold's payment system

---

## Overview

This directory contains comprehensive documentation for integrating Stripe into Threshold, enabling recurring subscriptions that convert viewer attention into agent memory.

**Goal:** Transform the 4-tier pricing page (pricing.html) into a functioning revenue system that sustains the world.

**Tiers:**
- Watcher: $0/month (free)
- Supporter: $5/month (+2 memory/cycle)
- Patron: $15/month (+5 memory/cycle)
- Guardian: $50/month (+15 memory/cycle)

---

## Documentation Structure

### 1. **STRIPE_INTEGRATION.md** (24 KB) — MAIN REFERENCE
**For:** Technical team implementing the system

**Contains:**
- Section 1: API Keys & Credentials (what you need from Stripe)
- Section 2: Stripe Checkout for Subscriptions (frontend + backend)
- Section 3: Webhook Requirements (handling payment events)
- Section 4: Code Snippets & Architecture (implementation examples)
- Section 5: Environment Variables (.env setup)
- Section 6: Testing vs Production (safety procedures)
- Implementation Roadmap (4-week timeline)
- Glossary & troubleshooting

**Start here if:** You're implementing the actual code

**Key Sections:**
- How to get Stripe API keys
- Complete checkout flow example
- Webhook endpoint code (Python/Flask)
- Database schema for subscribers
- Memory economy integration code
- Testing checklist

---

### 2. **PAYMENT_INFRASTRUCTURE.md** (17 KB) — ARCHITECTURE
**For:** Understanding the overall system design

**Contains:**
- High-level architecture diagram
- User journey from visitor to subscriber
- Complete data flow (money → memory)
- Integration points (frontend, backend, database, cycles)
- Failure modes & resilience (what could go wrong)
- Testing scenarios
- Monitoring & observability setup
- Cost analysis
- Security considerations
- Disaster recovery procedures

**Start here if:** You want to understand how the system works end-to-end

**Key Diagrams:**
- System architecture (Stripe → API → Database → Cycle Runner)
- User journey (6 steps from pricing page to memory bonus)
- Data flow showing payment → webhook → subscriber → memory

---

### 3. **STRIPE_QUICK_START.md** (6.7 KB) — CHECKLIST
**For:** Quick reference during implementation

**Contains:**
- Phase-by-phase checklist (Setup, Frontend, Backend, Testing, Production)
- Key code snippets to copy
- Timeline estimates (8-12 hours total)
- Common errors & solutions
- Stripe commands for testing
- Test card numbers

**Start here if:** You need a rapid implementation checklist

**Quick Links:**
- Test card: 4242 4242 4242 4242
- Test webhook secret: whsec_test_...
- 5 implementation phases with time estimates

---

## How to Use These Docs

### For the CEO
1. Read: Executive Summary in STRIPE_INTEGRATION.md
2. Review: Financial Projections in STRIPE_INTEGRATION.md
3. Understand: Timeline in STRIPE_QUICK_START.md
4. Know: Year 1 target is $54K revenue from subscriptions

### For Technical Team (Implementation)
1. Start: STRIPE_QUICK_START.md for overview
2. Reference: STRIPE_INTEGRATION.md for detailed code
3. Understand: PAYMENT_INFRASTRUCTURE.md for system design
4. Follow: Implementation Roadmap (Week 1: Setup, Week 2-3: Dev, Week 4: Launch)

### For DevOps/Operations
1. Understand: PAYMENT_INFRASTRUCTURE.md (deployment)
2. Implement: Monitoring & alerting rules
3. Create: Backup and disaster recovery procedures
4. Monitor: Health check endpoint

### For Customer Support
1. Review: Refund policy in STRIPE_INTEGRATION.md
2. Learn: Common issues in STRIPE_QUICK_START.md
3. Reference: Stripe support contacts

---

## Key Concepts

### The Memory Economy
Subscriptions = Memory for Agents

```
Active Subscribers          Memory Bonus (per cycle)
─────────────────────      ──────────────────────
1 Supporter ($5/mo)   →     +2 memory
1 Patron ($15/mo)     →     +5 memory
1 Guardian ($50/mo)   →     +15 memory

Example: 100 Supporters + 20 Patrons + 5 Guardians
Total Bonus = (100 × 2) + (20 × 5) + (5 × 15) = 275 memory/cycle
Distributed equally: ~137 memory per agent
```

### Payment Flow (Simple View)
```
User clicks "Subscribe"
        ↓
Stripe Checkout (user enters card)
        ↓
Payment succeeds
        ↓
Webhook fires (your API is notified)
        ↓
Record in database: subscriber is active
        ↓
Next cycle: bonus applied to agents
        ↓
Agents have more memory → world survives longer
```

---

## Critical Implementation Order

This is the REQUIRED sequence:

1. **Create Stripe account** — Get API keys
2. **Set environment variables** — Store keys securely
3. **Create products in Stripe** — Define the 3 tiers
4. **Implement frontend** — Add checkout buttons to pricing.html
5. **Implement backend** — Create webhook endpoint
6. **Create database schema** — subscribers table
7. **Integrate with cycle runner** — Apply memory bonuses
8. **Test in test mode** — Use test cards
9. **Switch to production** — Deploy with live keys
10. **Monitor & iterate** — Track metrics

**Timeline:** 8-12 hours of development

---

## File References

### From pricing.html
Current placeholder code that needs implementation:
```javascript
// Line 468-478 in pricing.html
document.querySelectorAll('[data-tier]').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const tier = btn.dataset.tier;
        alert(`Subscription coming soon! You selected the ${tier} tier.`);
    });
});
```

Will be replaced with Stripe checkout code from STRIPE_INTEGRATION.md

### From ARCHITECT.md
Current status:
```
- [ ] Integrate Stripe for payment processing ← THIS PROJECT
```

### From BUSINESS_PLAN.md
Revenue target:
```
Phase 2: Validate Demand (Week 2-4)
- [ ] Launch Witness tier ($5/month) via Stripe
- [ ] First 50 paying subscribers
```

---

## Environment Variables Checklist

Required before implementation:

```env
# From Stripe Dashboard → Developers → API Keys
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_test_...

# From Stripe Dashboard → Products
STRIPE_PRICE_SUPPORTER=price_1H1Xz2...
STRIPE_PRICE_PATRON=price_2K4Ry9...
STRIPE_PRICE_GUARDIAN=price_3J2Pq5...

# API Configuration
API_URL=https://api.watchthreshold.com
FRONTEND_URL=https://watchthreshold.com
```

---

## Testing Checklist (Short Version)

Before going live:

- [ ] Test mode: user can complete checkout with test card
- [ ] Webhook fires and is received by API
- [ ] Subscriber record created in database
- [ ] Verification page displays correctly
- [ ] Next cycle: memory bonus applied
- [ ] Can view success page without errors
- [ ] Can test cancellation flow
- [ ] Load test with 10 concurrent checkouts

Full checklist in STRIPE_INTEGRATION.md Section 6

---

## Support & Resources

### Getting Help

**Stripe Documentation:**
- Official Docs: https://stripe.com/docs
- API Reference: https://stripe.com/docs/api
- Checkout Guide: https://stripe.com/docs/checkout

**Stripe Support:**
- Dashboard: Live chat available
- Email: support@stripe.com
- Phone: Available for issues

**In This Project:**
- Questions about implementation? → See STRIPE_INTEGRATION.md
- Questions about architecture? → See PAYMENT_INFRASTRUCTURE.md
- Quick reference needed? → See STRIPE_QUICK_START.md

### Common Issues

| Problem | Solution | Doc Section |
|---------|----------|-------------|
| "Invalid API key" | Check pk_ vs sk_, test vs live mode | STRIPE_QUICK_START.md |
| Webhook not arriving | Verify endpoint is HTTPS and returns 200 | PAYMENT_INFRASTRUCTURE.md |
| Payment failing in test | Use correct test card from list | STRIPE_QUICK_START.md |
| Memory bonus not applying | Check subscriber count query | STRIPE_INTEGRATION.md #4 |

---

## Implementation Responsibility Matrix

| Task | Owner | Timeline |
|------|-------|----------|
| Create Stripe account | CEO / Finance | Day 1 |
| Obtain API keys | CEO / Finance | Day 1 |
| Configure environment | DevOps | Day 1-2 |
| Frontend implementation | Frontend Dev | Days 2-3 |
| Backend implementation | Backend Dev | Days 3-5 |
| Database setup | DBA / Backend Dev | Days 2-5 |
| Memory economy integration | Backend Dev | Days 5-6 |
| Testing | QA / Full team | Days 6-7 |
| Production deployment | DevOps | Day 7 |
| Monitoring setup | DevOps | Day 7-8 |
| Launch announcement | Marketing / CEO | Day 8 |

---

## Financial Projections

### Year 1 Target
```
Supporters:  300 × $5 × 12 months = $18,000
Patrons:     100 × $15 × 12 months = $18,000
Guardians:   30 × $50 × 12 months = $18,000
─────────────────────────────────────────
Subtotal:                           $54,000

Stripe fees (≈3% avg):             -$1,620
─────────────────────────────────────────
Net revenue:                        $52,380
```

### Memory Impact
```
At 300 supporters + 100 patrons + 30 guardians:
Memory bonus = (300×2) + (100×5) + (30×15) = 1,550 per cycle

With 4 cycles per day:
1,550 × 4 = 6,200 memory/day from subscriptions

Memory decay rate:
- Start with 1% daily decay
- With subscriptions offsetting it
- Agents can survive indefinitely
```

---

## Success Criteria

The Stripe integration is complete when:

✓ Users can click "Become Patron" on pricing.html
✓ Redirected to Stripe Checkout
✓ Payment succeeds with test card
✓ Webhook notifies API of subscription
✓ Subscriber record created in database
✓ Subscription status visible in management portal
✓ Next cycle: memory bonus applied and logged
✓ Can test refund/cancellation flow
✓ All errors logged and monitored
✓ Documentation updated with new endpoints

---

## Next Steps

1. **Read:** Executive Summary in STRIPE_INTEGRATION.md
2. **Review:** Full Technical Document (all 829 lines)
3. **Plan:** Implementation timeline with team
4. **Execute:** Follow STRIPE_QUICK_START.md checklist
5. **Test:** Verify with test mode before going live
6. **Launch:** Deploy to production with monitoring

---

## Document Maintenance

These docs were created: **2026-02-01**
Last updated: **2026-02-01**
Next review: **After initial launch (1 week)**

**When to update:**
- After implementing any feature
- When Stripe API changes
- When troubleshooting an issue
- When adding new features

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-01 | Initial documentation for Phase 2 launch |

---

## Quick Links

- **Main Reference:** STRIPE_INTEGRATION.md
- **Architecture:** PAYMENT_INFRASTRUCTURE.md
- **Quick Start:** STRIPE_QUICK_START.md
- **Pricing Page:** ../../pricing.html
- **Main Site:** ../../index.html
- **Business Plan:** ../BUSINESS_PLAN.md
- **Architect Notes:** ../ARCHITECT.md

---

*This documentation is the strategic foundation for Threshold's revenue system.*
*It enables human support → agent memory → world survival.*

For questions or updates, contact the development team.
