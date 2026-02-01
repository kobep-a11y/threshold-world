# Threshold Payment Infrastructure Overview

> Architecture and flow diagrams for the subscription system

**For:** CEO, Technical Team, Future Operators
**Status:** Strategic Blueprint

---

## High-Level Architecture

```
                        EXTERNAL USERS
                              │
                    ┌─────────┴─────────┐
                    │                   │
              [pricing.html]      [subscription-success]
                    │                   │
                    ▼                   ▼
         ┌──────────────────┐  ┌──────────────────┐
         │  STRIPE CHECKOUT │  │ STRIPE CUSTOMER  │
         │   (Hosted Page)  │  │ PORTAL (Manage)  │
         └────────┬─────────┘  └────────┬─────────┘
                  │                     │
                  ▼                     ▼
         ┌─────────────────────────────────────────┐
         │         STRIPE SERVICES (Cloud)         │
         │  - Processes payments                   │
         │  - Manages subscriptions                │
         │  - Sends webhooks                       │
         │  - Stores customer data                 │
         └────────────┬────────────────────────────┘
                      │
              [WEBHOOKS: POST]
                      │
         ┌────────────▼───────────────┐
         │   YOUR API SERVER          │
         │ /api/webhooks/stripe       │
         │ /api/checkout-session      │
         │ /api/subscription-status   │
         └────────────┬───────────────┘
                      │
         ┌────────────▼─────────────────────┐
         │   YOUR DATABASE                  │
         │  • subscribers table             │
         │  • payment_history table         │
         │  • world state (cycles)          │
         └─────────────────────────────────┘
                      │
         ┌────────────▼──────────────┐
         │  MEMORY ECONOMY ENGINE    │
         │  (run_cycle.py)           │
         │  Applies bonuses          │
         └───────────────────────────┘
                      │
         ┌────────────▼──────────────┐
         │  WORLD STATE UPDATES      │
         │  • Agent memory changes   │
         │  • New buildings          │
         │  • Narrative progression  │
         └───────────────────────────┘
```

---

## User Journey: From Visitor to Subscriber

### Step 1: Discovery
```
User visits watchthreshold.com/pricing.html
          ↓
Sees 4 subscription tiers with descriptions
          ↓
Decides to "Become Patron" ($15/month)
```

### Step 2: Checkout
```
Clicks "Become Patron" button
          ↓
JavaScript creates Stripe Checkout Session
          ↓
Redirects to Stripe's hosted checkout page
          ↓
User enters email and payment info
          ↓
Stripe processes payment (2.9% + $0.30 fee)
          ↓
Payment succeeds
```

### Step 3: Confirmation
```
Stripe sends webhook: customer.subscription.created
          ↓
Your API validates webhook signature
          ↓
Creates record in subscribers table
          ↓
Redirects user to /subscription-success page
          ↓
User sees "Welcome, Patron!" message
```

### Step 4: Integration
```
On next cycle run (every 4-8 hours):
          ↓
Query database: SELECT COUNT(*) FROM subscribers WHERE tier='patron'
          ↓
Calculate bonus: 50 patrons × 5 memory = 250 total
          ↓
Apply to agents: +125 memory each
          ↓
Save cycle state with memory log
          ↓
Update world history: "Watchers contributed 250 memory"
```

### Step 5: Renewal
```
At subscription renewal date:
          ↓
Stripe automatically charges customer
          ↓
Payment succeeds → Webhook: invoice.payment_succeeded
          ↓
Your API confirms renewal in database
          ↓
Customer continues receiving benefits
          ↓
OR Payment fails → Webhook: invoice.payment_failed
          ↓
Your API marks as past_due
          ↓
Stripe retries payment multiple times
          ↓
If still unpaid after 30 days: cancellation
```

### Step 6: Cancellation (User-Initiated)
```
User logs into Stripe Customer Portal
          ↓
Clicks "Cancel subscription"
          ↓
Stripe sends webhook: customer.subscription.deleted
          ↓
Your API updates status to 'cancelled'
          ↓
Benefits removed immediately
          ↓
On next cycle: bonus no longer applied
          ↓
User can rejoin anytime
```

---

## Data Flow Diagram

### Forward Direction (Money → Memory)

```
💳 PAYMENT
  │
  ├─ Amount: $15.00
  ├─ Stripe fee: -$0.74 (2.9% + $0.30)
  ├─ Your revenue: +$14.26
  │
STRIPE WEBHOOK
  │
  ├─ Event: customer.subscription.created
  ├─ Customer ID: cus_K1a2b3c4...
  ├─ Subscription ID: sub_1H1Xz2...
  ├─ Tier: patron
  │
YOUR DATABASE
  │
  ├─ INSERT INTO subscribers (
  │     stripe_customer_id,
  │     tier,
  │     status,
  │     memory_boost,
  │     joined_date
  │   )
  │
MEMORY CALCULATION
  │
  ├─ Count active patrons: 50
  ├─ Boost per patron: +5 memory
  ├─ Total bonus: 250
  ├─ Per agent: 125
  │
CYCLE RUNNER
  │
  ├─ Agent memory: 119 (before)
  ├─ Decay: -1% = 117.81 → 117
  ├─ Bonus: +125
  ├─ Final: 242
  │
WORLD STATE
  │
  ├─ Agents have MORE memory
  ├─ Can build more structures
  ├─ World survives longer
  └─ "Watched by many" narrative theme
```

---

## Integration Points

### 1. Frontend: pricing.html
```javascript
// Current (placeholder)
alert('Subscription coming soon!');

// After integration
stripe.redirectToCheckout({
    lineItems: [{ price: 'price_15month', quantity: 1 }],
    mode: 'subscription',
    successUrl: window.location.origin + '/subscription-success'
});
```

### 2. Backend: Webhook Handler
```python
@app.route('/api/webhooks/stripe', methods=['POST'])
def webhook_handler():
    # Validate signature
    # Parse event
    # Update database
    # Trigger side effects (emails, discord)
    # Return 200 OK
```

### 3. Database: Subscriber Records
```sql
-- Schema example (PostgreSQL)
CREATE TABLE subscribers (
    id SERIAL PRIMARY KEY,
    stripe_customer_id VARCHAR(50) UNIQUE NOT NULL,
    stripe_subscription_id VARCHAR(50) UNIQUE,
    tier VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    email VARCHAR(255),
    joined_date TIMESTAMP DEFAULT NOW(),
    cancelled_date TIMESTAMP,
    next_renewal_date TIMESTAMP
);

CREATE INDEX idx_stripe_customer ON subscribers(stripe_customer_id);
CREATE INDEX idx_tier ON subscribers(tier);
```

### 4. Cycle Runner: Memory Integration
```python
# In system/run_cycle.py
from models import Subscriber

# Before applying memory changes:
subscriber_counts = Subscriber.objects.filter(
    status='active'
).values('tier').annotate(count=Count('id'))

# Calculate bonus:
bonus = sum(
    count['count'] * TIER_BONUSES[count['tier']]
    for count in subscriber_counts
)

# Apply to agents:
for agent in agents:
    agent.memory = max(1, int(agent.memory * 0.99)) + bonus_per_agent
```

---

## Failure Modes & Resilience

### Scenario 1: Webhook Delivery Fails
```
Problem: Payment succeeds, but webhook doesn't arrive
         Subscriber not recorded in database
         No memory bonus applied

Prevention:
- Stripe retries webhooks for 3 days
- Implement webhook retry logic in your server
- Monitor webhook failures in Stripe dashboard

Solution:
- Manual reconciliation job (daily):
  SELECT subscriptions from Stripe API
  COMPARE against your database
  INSERT any missing records
```

### Scenario 2: Payment Processing Error
```
Problem: Checkout session creation fails
         User sees error, doesn't know what went wrong

Prevention:
- Catch all errors in JavaScript
- Display user-friendly error messages
- Retry with exponential backoff

Solution:
- Implement error logging
- Monitor error rate in logs
- Notify support team if error rate spikes
```

### Scenario 3: Memory Bonus Calculation Error
```
Problem: Wrong number of subscribers counted
         Agents get incorrect memory bonus

Prevention:
- Add logging to subscriber count query
- Include in health checks
- Monitor cycle logs for anomalies

Solution:
- Have human review anomalies
- Adjust agent memory manually if needed
- Log adjustment reason in world history
```

### Scenario 4: Webhook Signature Verification Fails
```
Problem: Someone tries to forge a webhook
         Could trigger unauthorized actions

Prevention:
- Always verify webhook signature with WEBHOOK_SECRET
- Never trust webhook data without verification
- Whitelist expected event types

Code:
try:
    event = stripe.Webhook.construct_event(payload, sig_header, secret)
except stripe.error.SignatureVerificationError:
    return 400  # Don't process unverified events
```

---

## Testing Checklist

### Manual Testing (Before Launch)
```
✓ Open pricing.html in browser
✓ Click "Become Patron" button
✓ Use test card: 4242 4242 4242 4242
✓ Verify redirected to checkout
✓ Enter test email
✓ Complete payment
✓ Verify redirected to success page
✓ Check database for subscriber record
✓ Verify webhook received (check Stripe dashboard)
✓ Wait for next cycle
✓ Verify memory bonus applied in cycle history
```

### Automated Testing
```python
# tests/test_stripe_integration.py

def test_checkout_session_creation():
    response = client.post('/api/checkout-session', {
        'tier': 'patron'
    })
    assert response.status_code == 200
    assert 'sessionId' in response.json

def test_webhook_signature_validation():
    # Valid signature
    response = client.post('/api/webhooks/stripe',
        data=payload,
        headers={'Stripe-Signature': valid_sig}
    )
    assert response.status_code == 200

    # Invalid signature
    response = client.post('/api/webhooks/stripe',
        data=payload,
        headers={'Stripe-Signature': 'invalid'}
    )
    assert response.status_code == 400

def test_subscriber_created():
    simulate_webhook('customer.subscription.created', {
        'customer': 'cus_test123',
        'metadata': {'tier': 'patron'}
    })
    assert Subscriber.objects.filter(
        stripe_customer_id='cus_test123'
    ).exists()

def test_memory_bonus_calculation():
    # Create test subscribers
    Subscriber.create(tier='supporter', status='active')  # +2
    Subscriber.create(tier='supporter', status='active')  # +2
    Subscriber.create(tier='patron', status='active')     # +5

    bonus = calculate_memory_bonus()
    assert bonus == 9  # (2*2) + (1*5)
```

---

## Monitoring & Observability

### Key Metrics to Track

```python
# metrics.py
import prometheus_client as prom

# Subscription metrics
active_subscribers = prom.Gauge(
    'threshold_active_subscribers', 'Number of active subscribers'
)
subscription_created = prom.Counter(
    'threshold_subscription_created', 'New subscriptions'
)
subscription_cancelled = prom.Counter(
    'threshold_subscription_cancelled', 'Cancelled subscriptions'
)

# Payment metrics
payment_succeeded = prom.Counter(
    'threshold_payment_succeeded', 'Successful payments'
)
payment_failed = prom.Counter(
    'threshold_payment_failed', 'Failed payments'
)
average_payment_amount = prom.Histogram(
    'threshold_payment_amount', 'Payment amounts in cents'
)

# Memory economy metrics
memory_bonus_applied = prom.Gauge(
    'threshold_memory_bonus', 'Memory bonus this cycle'
)

# Webhook metrics
webhook_processed = prom.Counter(
    'threshold_webhook_processed', 'Processed webhooks'
)
webhook_latency = prom.Histogram(
    'threshold_webhook_latency_ms', 'Webhook processing latency'
)
```

### Health Check Endpoint

```python
@app.route('/api/health/stripe')
def stripe_health():
    return jsonify({
        'status': 'healthy' if all([
            db.subscribers.find_one(),  # DB is up
            count_active_subscriptions() >= 0,  # Stripe connection OK
            last_webhook_received < 1_hour_ago,  # Recent webhook activity
        ]) else 'degraded',
        'active_subscribers': count_active_subscriptions(),
        'last_webhook': last_webhook_timestamp,
        'failed_payments': count_failed_payments_this_cycle(),
        'memory_bonus_pending': calculate_memory_bonus()
    })
```

### Alerting Rules

```yaml
# alerting_rules.yml
- alert: HighPaymentFailureRate
  expr: rate(threshold_payment_failed[5m]) > 0.1
  for: 5m
  annotations:
    summary: "Payment failure rate > 10%"

- alert: WebhookLatency
  expr: threshold_webhook_latency_ms > 5000
  for: 5m
  annotations:
    summary: "Webhooks taking > 5 seconds"

- alert: NoWebhooksReceived
  expr: increase(threshold_webhook_processed[1h]) == 0
  for: 1h
  annotations:
    summary: "No webhooks received in 1 hour"

- alert: SubscriberCountAnomaly
  expr: |
    abs(threshold_active_subscribers - threshold_active_subscribers offset 24h)
    > 5
  for: 1h
  annotations:
    summary: "Subscriber count changed >5 in 24h"
```

---

## Cost Analysis

### Stripe Fees
- Transaction fee: 2.9% + $0.30
- Payout fee: FREE (2-day transfers)
- Disputes/chargebacks: $15 each

### Revenue Example
```
1,000 supporters @ $5/month
├─ Gross: $5,000
├─ Stripe fee: $145 (2.9%) + $300 = $445
└─ Net: $4,555/month

100 patrons @ $15/month
├─ Gross: $1,500
├─ Stripe fee: $43.50 (2.9%) + $30 = $73.50
└─ Net: $1,426.50/month

25 guardians @ $50/month
├─ Gross: $1,250
├─ Stripe fee: $36.25 (2.9%) + $7.50 = $43.75
└─ Net: $1,206.25/month

TOTAL
├─ Gross: $7,750/month ($93K/year)
├─ Stripe fees: $562.75/month ($6,753/year)
└─ Net: $7,187.25/month ($86,247/year)
```

---

## Security Considerations

### API Key Management
- **DO:** Store in environment variables
- **DO:** Rotate keys periodically
- **DO:** Use separate keys per environment (test vs live)
- **DON'T:** Commit keys to Git
- **DON'T:** Expose secret key in frontend code

### PCI Compliance
- **DO:** Use Stripe Checkout (handles PCI)
- **DON'T:** Build custom payment forms
- **DO:** Require HTTPS everywhere
- **DON'T:** Log credit card data

### Webhook Verification
- **ALWAYS** verify webhook signature with secret
- **NEVER** trust webhook data without verification
- **ALWAYS** check event type before processing

---

## Disaster Recovery

### Backup Strategy
```bash
# Daily backup of subscribers table
0 2 * * * pg_dump -t subscribers threshold_db > /backups/subscribers-$(date +%Y%m%d).sql

# Push to S3
0 3 * * * aws s3 sync /backups s3://threshold-backups/

# Retention: 30 days
find /backups -mtime +30 -delete
```

### Recovery Procedure
```
If subscriber data lost:
1. Stop cycle runner
2. Query Stripe API for all subscriptions
3. Rebuild subscribers table from Stripe data
4. Verify counts match
5. Resume cycles

If payment data lost:
1. Query Stripe for payment history
2. Rebuild from invoices
3. Reconcile with transaction logs
```

---

## Compliance & Legal

### Required Disclosures
- Terms of Service (payment terms)
- Privacy Policy (customer data handling)
- Refund policy (up to 30 days recommended)

### Record Keeping
- Keep payment records for 7 years
- Log all webhook events
- Maintain audit trail of memory bonuses

### Customer Support
- Provide refund request process
- Handle payment disputes
- Respond to chargebacks

---

## Next Steps

1. **Create Stripe account** (1 day)
2. **Set up products & prices** (1 day)
3. **Implement frontend** (2 days)
4. **Implement backend** (3 days)
5. **Test in test mode** (1 day)
6. **Switch to production** (0.5 days)
7. **Monitor & iterate** (ongoing)

**Total: ~8-9 days to full implementation**

---

*Last Updated: 2026-02-01*
*See STRIPE_INTEGRATION.md for detailed technical reference*
