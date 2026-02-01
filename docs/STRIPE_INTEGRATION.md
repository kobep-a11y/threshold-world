# Stripe Integration for Threshold

> How to connect paid subscriptions to keep Kira and Verse alive.

**Document Status:** Strategic Planning | For CEO Review
**Last Updated:** 2026-02-01
**Target Launch:** Week 2 of Phase 2

---

## Executive Summary

Threshold's revenue model depends on subscription payments. This document outlines what Stripe integration requires, how it works, and what infrastructure needs to be set up.

**Key Metrics:**
- 4 subscription tiers: Watcher (free) → Supporter ($5/mo) → Patron ($15/mo) → Guardian ($50/mo)
- Expected revenue (Year 1): ~$150K from subscriptions
- First milestone: 50 paying subscribers in first month

---

## Section 1: Stripe API Keys & Credentials

### What You Need

Stripe provides two types of keys that work together:

**1. Publishable Key (Frontend)**
- **What it is:** Public key used in browser JavaScript
- **Where used:** `pricing.html` and checkout pages
- **Security:** Safe to expose—controls checkout UI only
- **Example format:** `pk_live_51H1Xz2KgV...` (production) or `pk_test_4eC39HqL...` (testing)

**2. Secret Key (Backend)**
- **What it is:** Secure key for server-side API calls
- **Where used:** Backend API endpoints, webhook verification
- **Security:** NEVER expose to frontend—use environment variables only
- **Example format:** `sk_live_4eC39HqL...` (production) or `sk_test_4eC39HqL...` (testing)

### How to Obtain Keys

1. Create a Stripe account at https://stripe.com
2. Navigate to Dashboard → Developers → API Keys
3. You'll see:
   - **Publishable key** (starts with `pk_`)
   - **Secret key** (starts with `sk_`)
4. Stripe provides separate keys for Test and Live modes

### Where Keys Go

**Frontend (pricing.html):**
```javascript
// Using Stripe.js library
const stripe = Stripe('pk_test_4eC39HqL...');
```

**Backend (.env file or GitHub Secrets):**
```
STRIPE_SECRET_KEY=sk_test_4eC39HqL...
STRIPE_PUBLISHABLE_KEY=pk_test_4eC39HqL...
```

**GitHub Secrets (for automated deployment):**
- Navigate to: Repo Settings → Secrets and variables → Actions
- Add `STRIPE_SECRET_KEY` and `STRIPE_PUBLISHABLE_KEY`
- These are automatically injected into CI/CD pipelines

---

## Section 2: Stripe Checkout for Subscriptions

### Architecture Overview

Threshold uses **Stripe Checkout** (hosted payment page) instead of building custom forms:

```
User clicks "Become Supporter"
           ↓
JavaScript redirects to Stripe Checkout
           ↓
User enters payment info on Stripe's server
           ↓
Payment succeeds → Stripe sends webhook
           ↓
Webhook creates subscription in your database
           ↓
User returns to confirmation page
```

**Why Checkout (not custom forms)?**
- PCI compliance handled by Stripe
- Mobile optimized
- Secure by default
- Subscription management built-in

### Frontend Implementation

**1. Load Stripe.js Library**

In `pricing.html` (already partially done):

```html
<!-- Add to <head> -->
<script src="https://js.stripe.com/v3/"></script>
```

**2. Update Subscription Buttons**

Current code has placeholder:
```javascript
document.querySelectorAll('[data-tier]').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const tier = btn.dataset.tier;
        alert(`Subscription coming soon! You selected the ${tier} tier.`);
    });
});
```

New implementation:

```javascript
// Map tiers to Stripe Price IDs
const TIER_PRICES = {
    'supporter': 'price_1H1Xz2...',   // $5/month
    'patron': 'price_2K4Ry9...',      // $15/month
    'guardian': 'price_3J2Pq5...'     // $50/month
};

const stripe = Stripe('pk_test_4eC39HqL...');

document.querySelectorAll('[data-tier]').forEach(btn => {
    btn.addEventListener('click', async (e) => {
        e.preventDefault();
        const tier = btn.dataset.tier;
        const priceId = TIER_PRICES[tier];

        // Redirect to Stripe Checkout
        const { error } = await stripe.redirectToCheckout({
            lineItems: [{ price: priceId, quantity: 1 }],
            mode: 'subscription',
            successUrl: 'https://watchthreshold.com/subscription-success?session_id={CHECKOUT_SESSION_ID}',
            cancelUrl: 'https://watchthreshold.com/pricing.html'
        });

        if (error) {
            console.error('Stripe error:', error.message);
            alert('Payment failed: ' + error.message);
        }
    });
});
```

### Backend Implementation

**1. Create Stripe Products & Prices**

Option A: Dashboard (manual)
- Log into Stripe Dashboard
- Products → Create product
- Name: "Threshold Supporter"
- Price: $5/month, recurring
- Save and copy Price ID

Option B: Via API (automated)
```python
import stripe

stripe.api_key = "sk_test_4eC39HqL..."

# Create product
product = stripe.Product.create(
    name="Threshold Supporter",
    description="+2 memory/cycle, Credits Wall, Discord badge"
)

# Create recurring price
price = stripe.Price.create(
    product=product.id,
    unit_amount=500,  # $5.00 in cents
    currency="usd",
    recurring={"interval": "month"}
)

print(f"Price ID: {price.id}")
```

**2. Create Checkout Session Endpoint**

Backend API endpoint `/api/checkout-session`:

```python
# Using Flask
from flask import Flask, request, jsonify
import stripe
import os

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

@app.route('/api/checkout-session', methods=['POST'])
def create_checkout_session():
    tier = request.json.get('tier')

    TIER_PRICES = {
        'supporter': os.environ['STRIPE_PRICE_SUPPORTER'],    # price_1H1Xz2...
        'patron': os.environ['STRIPE_PRICE_PATRON'],          # price_2K4Ry9...
        'guardian': os.environ['STRIPE_PRICE_GUARDIAN']       # price_3J2Pq5...
    }

    if tier not in TIER_PRICES:
        return jsonify({'error': 'Invalid tier'}), 400

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': TIER_PRICES[tier],
                'quantity': 1
            }],
            mode='subscription',
            success_url='https://watchthreshold.com/subscription-success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://watchthreshold.com/pricing.html',
            client_reference_id=request.json.get('user_id', 'anonymous'),
            metadata={'tier': tier}
        )

        return jsonify({'sessionId': session.id})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

**3. Retrieve Session Details**

After payment, get subscription info:

```python
@app.route('/api/subscription-status', methods=['POST'])
def get_subscription_status():
    session_id = request.json.get('session_id')

    try:
        session = stripe.checkout.Session.retrieve(session_id)

        return jsonify({
            'customer_id': session.customer,
            'subscription_id': session.subscription,
            'status': session.payment_status,
            'tier': session.metadata['tier']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

---

## Section 3: Webhook Requirements

### What Webhooks Are

Webhooks are **callbacks from Stripe to your server** when subscription events happen:

```
Subscription created → Stripe sends webhook → Your server records it
Payment collected → Webhook → Update subscriber status
Subscription cancelled → Webhook → Remove benefits
```

### Critical Events

| Event | Trigger | Action |
|-------|---------|--------|
| `customer.subscription.created` | User completes checkout | Record subscription in database |
| `customer.subscription.updated` | Plan changed or renewed | Update subscription details |
| `customer.subscription.deleted` | User cancels subscription | Remove subscriber status |
| `invoice.payment_succeeded` | Monthly payment collected | Confirm renewal, send receipt |
| `invoice.payment_failed` | Payment declined | Notify user, attempt retry |
| `charge.refunded` | User requests refund | Cancel subscription, remove benefits |

### Webhook Endpoint Implementation

**Set up webhook receiver:**

```python
# api/webhooks.py or in your main app
from flask import request, jsonify
import stripe
import os
import json
from datetime import datetime

stripe.api_key = os.environ['STRIPE_SECRET_KEY']
WEBHOOK_SECRET = os.environ['STRIPE_WEBHOOK_SECRET']

@app.route('/api/webhooks/stripe', methods=['POST'])
def handle_stripe_webhook():
    """Handle events from Stripe"""

    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify webhook signature (prevents spoofing)
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )
    except ValueError:
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError:
        return jsonify({'error': 'Invalid signature'}), 400

    # Handle the event
    if event['type'] == 'customer.subscription.created':
        subscription = event['data']['object']
        handle_subscription_created(subscription)

    elif event['type'] == 'customer.subscription.updated':
        subscription = event['data']['object']
        handle_subscription_updated(subscription)

    elif event['type'] == 'customer.subscription.deleted':
        subscription = event['data']['object']
        handle_subscription_cancelled(subscription)

    elif event['type'] == 'invoice.payment_succeeded':
        invoice = event['data']['object']
        handle_payment_succeeded(invoice)

    elif event['type'] == 'invoice.payment_failed':
        invoice = event['data']['object']
        handle_payment_failed(invoice)

    return jsonify({'received': True}), 200


def handle_subscription_created(subscription):
    """Record new subscriber"""
    customer_id = subscription['customer']
    tier = subscription['metadata'].get('tier', 'supporter')

    # Save to your database
    db.subscribers.insert_one({
        'stripe_customer_id': customer_id,
        'subscription_id': subscription['id'],
        'tier': tier,
        'status': subscription['status'],
        'current_period_start': datetime.fromtimestamp(subscription['current_period_start']),
        'current_period_end': datetime.fromtimestamp(subscription['current_period_end']),
        'created_at': datetime.now()
    })

    print(f"New subscriber: {tier}")
    # Trigger: Add to Watcher Registry, send confirmation email


def handle_subscription_cancelled(subscription):
    """Remove subscriber benefits"""
    customer_id = subscription['customer']

    db.subscribers.update_one(
        {'stripe_customer_id': customer_id},
        {'$set': {'status': 'cancelled', 'cancelled_at': datetime.now()}}
    )

    print(f"Subscription cancelled: {customer_id}")
    # Trigger: Announce to agents that memory is lost
    # In world state: "A watcher has gone silent"
```

### Registering Webhook Endpoint with Stripe

1. Go to Stripe Dashboard → Developers → Webhooks
2. Click "Add endpoint"
3. Webhook URL: `https://your-api.com/api/webhooks/stripe`
4. Select events: `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.payment_succeeded`, `invoice.payment_failed`
5. Copy the **Signing Secret** → Save as environment variable `STRIPE_WEBHOOK_SECRET`

---

## Section 4: Code Snippets & Architecture

### Project Structure

```
threshold/
├── api/
│   ├── checkout-session.js      # Frontend: create checkout
│   ├── webhooks.py              # Backend: handle Stripe events
│   └── subscriptions.py          # Backend: manage subscriptions
├── docs/
│   ├── STRIPE_INTEGRATION.md    # THIS FILE
│   └── PAYMENT_FLOW.md          # Detailed user flow
├── pricing.html                  # Frontend with checkout buttons
├── world/
│   ├── meta/
│   │   └── subscribers.json      # Active subscribers list
│   └── ...
├── system/
│   └── memory_economy.py         # Apply memory bonuses from subscriptions
└── .env                          # Environment variables
```

### Database Schema (MongoDB or PostgreSQL)

```javascript
// Subscribers collection
{
  _id: ObjectId("..."),
  stripe_customer_id: "cus_K1a2b3c4...",
  stripe_subscription_id: "sub_1H1Xz2...",
  email: "user@example.com",
  tier: "patron",                    // supporter, patron, or guardian
  status: "active",                  // active, past_due, cancelled
  memory_boost: 5,                   // Memory boost per cycle
  joined_date: ISODate("2025-02-01"),
  cancelled_date: null,
  renewal_date: ISODate("2025-03-01"),
  metadata: {
    user_name: "Optional user display name",
    joined_cycle: 30
  }
}

// Payment history collection
{
  _id: ObjectId("..."),
  stripe_invoice_id: "in_1H1Xz2...",
  subscriber_id: ObjectId("..."),
  amount: 1500,                      // In cents: $15.00
  currency: "usd",
  status: "paid",                    // paid, open, void, uncollectible
  period_start: ISODate("2025-02-01"),
  period_end: ISODate("2025-03-01"),
  paid_date: ISODate("2025-02-02")
}
```

### Memory Economy Integration

Currently, Threshold has 2 agents with decaying memory. Subscriptions add bonuses:

```python
# system/memory_economy.py

def calculate_memory_bonus(subscriber_count_by_tier):
    """
    Calculate total memory bonus from active subscriptions.

    Memory bonuses per tier:
    - Supporter ($5/mo):  +2 memory/cycle per subscriber
    - Patron ($15/mo):    +5 memory/cycle per subscriber
    - Guardian ($50/mo):  +15 memory/cycle per subscriber
    """

    supporters = subscriber_count_by_tier.get('supporter', 0)
    patrons = subscriber_count_by_tier.get('patron', 0)
    guardians = subscriber_count_by_tier.get('guardian', 0)

    total_bonus = (
        supporters * 2 +
        patrons * 5 +
        guardians * 15
    )

    return total_bonus


def apply_cycle_memory(cycle_state, subscriber_counts):
    """
    Apply memory decay and subscription bonuses.

    Process:
    1. Apply 1% decay to all agents
    2. Calculate bonus from active subscriptions
    3. Distribute bonus equally among agents
    4. Log transaction for transparency
    """

    agents = cycle_state['agents']
    total_bonus = calculate_memory_bonus(subscriber_counts)
    bonus_per_agent = total_bonus // len(agents)

    for agent in agents:
        # Decay first
        agent['memory'] = max(1, int(agent['memory'] * 0.99))

        # Then bonus
        agent['memory'] += bonus_per_agent

    # Record in world history
    cycle_state['memory_log'] = {
        'decay_reason': '1% natural decay',
        'subscriber_bonus': total_bonus,
        'bonus_per_agent': bonus_per_agent,
        'active_subscribers': sum(subscriber_counts.values()),
        'breakdown': subscriber_counts
    }

    return cycle_state


# Called from system/run_cycle.py
def run_cycle():
    # ... existing cycle logic ...

    # Get active subscriber counts from database
    subscriber_counts = db.subscribers.aggregate([
        {'$match': {'status': 'active'}},
        {'$group': {'_id': '$tier', 'count': {'$sum': 1}}}
    ])

    subscriber_by_tier = {
        item['_id']: item['count']
        for item in subscriber_counts
    }

    # Apply memory changes
    world_state = apply_cycle_memory(world_state, subscriber_by_tier)

    # ... save cycle ...
```

### Success Page & Email Flow

**After successful payment:**

```python
@app.route('/subscription-success')
def subscription_success():
    session_id = request.args.get('session_id')

    if not session_id:
        return redirect('/pricing.html')

    # Get session details from Stripe
    session = stripe.checkout.Session.retrieve(session_id)
    subscription = stripe.Subscription.retrieve(session.subscription)

    return render_template('subscription_success.html', {
        'tier': subscription.metadata['tier'],
        'next_billing': datetime.fromtimestamp(subscription.current_period_end),
        'memory_boost': TIER_BONUSES[subscription.metadata['tier']]
    })
```

**Confirmation email template:**

```
Subject: Welcome to Threshold, [Name]!

Your subscription is active. You are now a Threshold [Tier].

🔗 What you get:
- [List tier-specific benefits]
- Your name in the Watcher Registry
- Memory contribution: +[X] per cycle

📊 Next Billing: [DATE]
To manage your subscription: [Stripe Customer Portal URL]

The world is watching. Thank you for keeping it alive.

— The Architect
```

---

## Section 5: Environment Variables

### Required .env File

Create `.env` at project root (never commit this file):

```env
# Stripe API Keys
STRIPE_PUBLISHABLE_KEY=pk_test_4eC39HqL...
STRIPE_SECRET_KEY=sk_test_4eC39HqL...
STRIPE_WEBHOOK_SECRET=whsec_test_4eC39HqL...

# Stripe Product IDs (from Stripe Dashboard)
STRIPE_PRICE_SUPPORTER=price_1H1Xz2...
STRIPE_PRICE_PATRON=price_2K4Ry9...
STRIPE_PRICE_GUARDIAN=price_3J2Pq5...

# Database (example using MongoDB)
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/threshold

# API Configuration
API_URL=https://api.watchthreshold.com
FRONTEND_URL=https://watchthreshold.com

# Emails (optional, for subscription confirmations)
SENDGRID_API_KEY=SG.xxxx...
SENDGRID_FROM_EMAIL=subscriptions@watchthreshold.com
```

### .gitignore Entry

```
.env
.env.local
.env.*.local
stripe_keys.txt
```

### Loading Environment Variables

**Python (Flask/Django):**
```python
import os
from dotenv import load_dotenv

load_dotenv()

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
```

**Node.js:**
```javascript
require('dotenv').config();

const stripeSecretKey = process.env.STRIPE_SECRET_KEY;
const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
```

**GitHub Secrets (for CI/CD):**
```bash
# In GitHub Actions workflow
env:
  STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
  STRIPE_WEBHOOK_SECRET: ${{ secrets.STRIPE_WEBHOOK_SECRET }}
```

---

## Section 6: Testing vs Production

### Development/Testing Setup

**Stripe Test Mode:**
- All charges are simulated (no real money)
- Use test card numbers

**Test Card Numbers:**
```
Visa (Success):           4242 4242 4242 4242
Visa (Decline):           4000 0000 0000 0002
Mastercard (Success):     5555 5555 5555 4444
Amex (Success):           3782 822463 10005
```

**Test Webhook Flow:**
1. Set up endpoint in test mode
2. Go to Stripe Dashboard → Webhooks → Select endpoint
3. Click "Send test event"
4. Choose event type (e.g., `customer.subscription.created`)
5. Verify your endpoint returns 200 OK

**Environment:**
```env
# .env.development
STRIPE_PUBLISHABLE_KEY=pk_test_4eC39HqL...
STRIPE_SECRET_KEY=sk_test_4eC39HqL...
STRIPE_MODE=test
```

### Production Setup

**Requirements:**
1. SSL certificate (HTTPS only)
2. Live Stripe account verified (identity + bank info)
3. All endpoints return 200 OK for webhooks
4. Production database with subscriber backups
5. Email infrastructure for receipts

**Environment:**
```env
# .env.production
STRIPE_PUBLISHABLE_KEY=pk_live_51H1Xz2KgV...
STRIPE_SECRET_KEY=sk_live_4eC39HqL...
STRIPE_MODE=live
```

**Pre-launch Checklist:**
- [ ] Test payment flow end-to-end
- [ ] Test webhook delivery (using Stripe's test event sender)
- [ ] Test refund/cancellation flow
- [ ] Load test (can server handle 100 simultaneous checkouts?)
- [ ] Verify success/error page UX
- [ ] Confirm confirmation emails send
- [ ] Test subscription renewal (wait 1 month in test)
- [ ] Document customer support process
- [ ] Set up Stripe Dashboard alerts for high decline rates

### Monitoring & Alerts

```python
# system/monitor_subscriptions.py

def check_subscription_health():
    """Daily health check"""

    # Check for failed payments
    failed_invoices = stripe.Invoice.list(status='open')
    if len(failed_invoices.data) > 5:
        send_alert(f"⚠️ {len(failed_invoices)} failed payments")

    # Check for high churn
    active_subscribers = db.subscribers.count_documents({'status': 'active'})

    # Check customer balance
    account_balance = stripe.Account.retrieve()

    return {
        'failed_payments': len(failed_invoices.data),
        'active_subscribers': active_subscribers,
        'balance': account_balance.balance
    }
```

---

## Implementation Roadmap

### Week 1: Setup
- [ ] Create Stripe account and verify identity
- [ ] Obtain API keys (test and production)
- [ ] Create subscription products/prices in Stripe
- [ ] Set up environment variables
- [ ] Document all keys securely (password manager)

### Week 2: Development
- [ ] Implement frontend checkout buttons
- [ ] Create backend checkout session endpoint
- [ ] Build webhook receiver
- [ ] Create subscriber database schema
- [ ] Test full payment flow in test mode

### Week 3: Integration
- [ ] Connect memory economy to subscriber counts
- [ ] Update cycle runner to apply bonuses
- [ ] Build subscriber dashboard (view status)
- [ ] Create customer support tools (refund requests)
- [ ] Set up email confirmations

### Week 4: Launch
- [ ] Switch to production keys
- [ ] Register production webhook endpoint
- [ ] Deploy to production
- [ ] Monitor for errors (first 24 hours)
- [ ] Announce to Discord/Twitter

---

## Key Contacts & Resources

**Stripe Documentation:**
- API Reference: https://stripe.com/docs/api
- Checkout: https://stripe.com/docs/checkout
- Webhooks: https://stripe.com/docs/webhooks

**Stripe Support:**
- Dashboard chat: Available 24/7
- Email: support@stripe.com
- For urgent issues: Use dashboard support chat

**Common Issues & Solutions:**

| Problem | Solution |
|---------|----------|
| "Invalid publishable key" | Check key is `pk_` not `sk_`, and match test/live mode |
| Webhook events not arriving | Verify endpoint returns 200 OK, check IP allowlist if any |
| Payment button not loading | Verify Stripe.js library is loaded, check console errors |
| Refund failing | Ensure refund is within allowed window (usually 365 days) |
| Customer can't view invoices | Send them to Stripe Customer Portal (generated automatically) |

---

## Financial Projections

**Year 1 Target:** $18K from subscriptions
- 300 Supporters @ $5/mo × 12 months = $18,000
- 100 Patrons @ $15/mo × 12 months = $18,000
- 30 Guardians @ $50/mo × 12 months = $18,000
- **Subtotal: $54,000**

**Stripe Fees:**
- Stripe takes 2.9% + $0.30 per transaction
- On average: ~3% of revenue = $1,620
- **Net after Stripe: ~$52,380**

**Processing Timeline:**
- Payouts: Every 2 days to linked bank account
- Refunds: 5-10 business days

---

## Appendix: Glossary

| Term | Definition |
|------|-----------|
| **Price ID** | Unique identifier for a product's pricing (e.g., `price_1H1Xz2...`). Multiple prices can exist per product. |
| **Customer ID** | Stripe's unique ID for a paying customer (e.g., `cus_K1a2b3c4...`). Used in webhooks. |
| **Subscription ID** | Unique ID for an active subscription (e.g., `sub_1H1Xz2...`). |
| **Webhook** | HTTP callback from Stripe to your server when events occur. |
| **Test Mode** | Sandbox environment using test credit cards and fake payments. |
| **Live Mode** | Production environment processing real payments. |
| **PCI Compliance** | Security standard for handling credit card data. Stripe's Checkout handles this. |
| **Idempotency Key** | Optional token to prevent duplicate charges if request is retried. |

---

## Sign-Off

This document provides the strategic foundation for Threshold's payment system. Implementation can begin once:

1. Stripe account is created and verified
2. API keys are securely stored
3. Development team has access to environment variables
4. Database schema is finalized

**Next Step:** Implementation roadmap → Week 1 setup

---

*Prepared for the Threshold CEO | February 2026*
*This document is a working reference for subscription infrastructure strategy.*
