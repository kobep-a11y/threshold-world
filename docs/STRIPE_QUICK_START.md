# Stripe Integration - Quick Start Checklist

> Fast reference for implementing Stripe on Threshold

---

## Phase 1: Setup (1-2 hours)

### Account & Keys
- [ ] Create Stripe account at https://stripe.com
- [ ] Complete identity verification (photo ID + bank account)
- [ ] Navigate to Dashboard → Developers → API Keys
- [ ] Copy test keys:
  - `STRIPE_PUBLISHABLE_KEY` (pk_test_...)
  - `STRIPE_SECRET_KEY` (sk_test_...)
  - `STRIPE_WEBHOOK_SECRET` (whsec_test_...)
- [ ] Store in `.env` file locally (never commit)
- [ ] Add to GitHub Secrets for CI/CD

### Stripe Products
- [ ] Create product "Threshold Supporter" ($5/month)
- [ ] Create product "Threshold Patron" ($15/month)
- [ ] Create product "Threshold Guardian" ($50/month)
- [ ] Copy Price IDs (price_...) for each
- [ ] Add to environment variables

---

## Phase 2: Frontend (2-3 hours)

### Update pricing.html
Replace placeholder alert code with:

```javascript
const TIER_PRICES = {
    'supporter': 'price_...',
    'patron': 'price_...',
    'guardian': 'price_...'
};

const stripe = Stripe('pk_test_...');

document.querySelectorAll('[data-tier]').forEach(btn => {
    btn.addEventListener('click', async (e) => {
        e.preventDefault();
        const tier = btn.dataset.tier;

        const { error } = await stripe.redirectToCheckout({
            lineItems: [{ price: TIER_PRICES[tier], quantity: 1 }],
            mode: 'subscription',
            successUrl: 'https://watchthreshold.com/subscription-success?session_id={CHECKOUT_SESSION_ID}',
            cancelUrl: 'https://watchthreshold.com/pricing.html'
        });

        if (error) alert(error.message);
    });
});
```

- [ ] Load Stripe.js in `<head>`: `<script src="https://js.stripe.com/v3/"></script>`
- [ ] Update button click handlers
- [ ] Test with test card: `4242 4242 4242 4242`
- [ ] Verify success/cancel redirects work

---

## Phase 3: Backend (3-4 hours)

### Create Webhook Endpoint
```python
@app.route('/api/webhooks/stripe', methods=['POST'])
def handle_stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )
    except:
        return {'error': 'Invalid'}, 400

    # Handle events
    if event['type'] == 'customer.subscription.created':
        handle_subscription_created(event['data']['object'])
    elif event['type'] == 'customer.subscription.deleted':
        handle_subscription_cancelled(event['data']['object'])

    return {'received': True}, 200
```

- [ ] Create webhook endpoint at `/api/webhooks/stripe`
- [ ] Implement event handlers for:
  - `customer.subscription.created` → Record subscriber
  - `customer.subscription.deleted` → Remove subscriber
  - `invoice.payment_succeeded` → Confirm renewal
  - `invoice.payment_failed` → Notify user
- [ ] Register webhook in Stripe Dashboard
- [ ] Test webhook with Stripe's test event sender

### Create Database Schema
```javascript
// subscribers collection
{
  stripe_customer_id: "cus_...",
  tier: "supporter|patron|guardian",
  status: "active|cancelled",
  memory_boost: 2|5|15,
  joined_date: ISODate,
  renewal_date: ISODate
}
```

- [ ] Create subscribers collection/table
- [ ] Add indexes for `stripe_customer_id` and `tier`

### Memory Economy Integration
```python
def apply_cycle_memory(agents, subscriber_counts):
    total_bonus = (
        subscriber_counts.get('supporter', 0) * 2 +
        subscriber_counts.get('patron', 0) * 5 +
        subscriber_counts.get('guardian', 0) * 15
    )

    for agent in agents:
        agent['memory'] = max(1, int(agent['memory'] * 0.99))  # Decay
        agent['memory'] += total_bonus // len(agents)  # Bonus
```

- [ ] Query subscriber counts by tier from database
- [ ] Calculate total memory bonus
- [ ] Apply to cycle runner before saving state
- [ ] Log transaction in cycle history

---

## Phase 4: Testing (1-2 hours)

### Test Mode Verification
- [ ] Test successful payment (card: `4242 4242 4242 4242`)
- [ ] Test declined payment (card: `4000 0000 0000 0002`)
- [ ] Verify webhook fires for each scenario
- [ ] Check subscriber record created in database
- [ ] Verify success page displays correctly
- [ ] Test subscription cancellation
- [ ] Verify memory bonus applied in next cycle

### Load Test
- [ ] Simulate 10 concurrent checkouts
- [ ] Check server responds within 2 seconds
- [ ] Verify no duplicate subscriptions created

---

## Phase 5: Production (1 hour)

### Before Going Live
- [ ] Obtain production Stripe keys
- [ ] Update environment variables
- [ ] Change webhook URL to production domain
- [ ] Re-test full flow with test keys one more time
- [ ] Have customer support process documented
- [ ] Set up payment failure alerts

### Switch to Live
- [ ] Update `STRIPE_PUBLISHABLE_KEY` (pk_live_...)
- [ ] Update `STRIPE_SECRET_KEY` (sk_live_...)
- [ ] Re-register webhook with production endpoint
- [ ] Deploy to production
- [ ] Monitor for 24 hours for errors

### Post-Launch
- [ ] Announce in Discord
- [ ] Post on Twitter
- [ ] Monitor Stripe dashboard for failed payments
- [ ] Reach out to first 10 subscribers with thank you message

---

## Support Commands

### Test Webhook Delivery
```bash
# From Stripe Dashboard
Developers → Webhooks → Select endpoint → Send test event
```

### View Live Subscribers
```javascript
// In your backend
db.subscribers.find({status: 'active'}).countDocuments()
```

### Handle Refund Request
```python
# Refund last charge
invoice = stripe.Invoice.retrieve(customer_invoice_id)
refund = stripe.Refund.create(charge=invoice.charge)
```

### Check Payout Status
```bash
# Stripe Dashboard → Payouts → View details
```

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid Stripe key" | Key format wrong or mode mismatch | Check pk_/sk_ prefix, test vs live |
| "Webhook not arriving" | Endpoint unreachable | Check HTTPS, test endpoint manually |
| "Card declined" | Test card in live mode | Use live cards only in live, test cards in test |
| "Duplicate charge" | Race condition in checkout | Add idempotency key to requests |

---

## Estimated Timeline

| Phase | Time | Status |
|-------|------|--------|
| Setup | 1-2 hrs | ⬜ Pending |
| Frontend | 2-3 hrs | ⬜ Pending |
| Backend | 3-4 hrs | ⬜ Pending |
| Testing | 1-2 hrs | ⬜ Pending |
| Production | 1 hr | ⬜ Pending |
| **Total** | **8-12 hrs** | **Week 2 Target** |

---

## Key Contacts

- **Stripe Support:** support@stripe.com (or dashboard chat)
- **Documentation:** https://stripe.com/docs
- **API Reference:** https://stripe.com/docs/api
- **This Project:** See STRIPE_INTEGRATION.md for full reference

---

Last Updated: 2026-02-01
