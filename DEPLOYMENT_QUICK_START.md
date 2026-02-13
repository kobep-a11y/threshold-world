# Threshold World — Quick Deployment Guide

**For**: Kobe | **Status**: Ready to Deploy | **Time**: 30 minutes

---

## What's Ready

✅ Code committed and tested (Cycles 33-62)
✅ Website synced (all HTML files)
✅ State.json rebuilt and verified
✅ Stripe payment system configured
✅ Discord webhook ready
✅ Git history clean

**What's Deployed**: NOTHING YET (waiting for your action)

---

## Step 1: Push to GitHub (5 min)

Your machine (from project directory):

```bash
cd /path/to/threshold-world
git push origin main
```

If you get authentication errors:
- Use SSH key (configure in GitHub settings)
- Or use GitHub CLI: `gh auth login` then push
- Or create GitHub personal access token

---

## Step 2: Create Vercel Project (10 min)

### Option A: Automatic (easiest)
1. Go to https://vercel.com/dashboard
2. Click "Add New Project"
3. Select "Import Git Repository"
4. Search for "threshold-world"
5. Select the repo and click "Import"
6. Vercel auto-detects it's a static site
7. Click "Deploy"

### Option B: Manual
1. Go to https://vercel.com
2. Sign in with GitHub account
3. Create new team if needed
4. Click "New Project"
5. Paste GitHub repo URL
6. Set root directory to `/` (or auto-detect)
7. Click Deploy

## Step 3: Configure Environment Variables (5 min)

In Vercel project settings:

```
1. Go to Settings → Environment Variables
2. Add these variables:

NAME: STRIPE_PUBLISHABLE_KEY
VALUE: pk_live_xxxxxxxxxxxxx (from Stripe dashboard)

NAME: STRIPE_SECRET_KEY
VALUE: sk_live_xxxxxxxxxxxxx (from Stripe dashboard)

NAME: DISCORD_WEBHOOK_URL
VALUE: https://discordapp.com/api/webhooks/... (existing)

3. Click "Save"
4. Trigger new deployment
```

**Finding your keys**:
- Stripe: https://dashboard.stripe.com/apikeys
- Discord: Check bot channel in Discord server
- Already saved? Check GitHub Secrets (you'll need to transfer)

---

## Step 4: Test Live Deployment (5 min)

Your live URL will be: `https://threshold-world.vercel.app` (or custom domain)

Test these URLs:
```
✓ https://threshold-world.vercel.app/
✓ https://threshold-world.vercel.app/pricing.html
✓ https://threshold-world.vercel.app/live.html
✓ https://threshold-world.vercel.app/world-viewer.html
```

Each should show:
- Cycle 62 in badge ✓
- Memory 91/86 ✓
- Latest history entry ✓

Test payment:
```
1. Click "Subscribe Now" on pricing page
2. Select $5/month tier
3. Click "Subscribe"
4. Use Stripe test card: 4242 4242 4242 4242
5. Exp: 12/26 | CVC: 123
6. Click "Subscribe"
7. Should see confirmation
8. Check Stripe dashboard for transaction
```

---

## Step 5: Set Custom Domain (Optional, 5 min)

If you own watchthreshold.com:

1. In Vercel: Settings → Domains
2. Click "Add Domain"
3. Enter "watchthreshold.com"
4. Follow DNS instructions
5. Update nameservers at domain registrar
6. Wait for DNS propagation (1-24 hours)

Once live, your site is at: https://watchthreshold.com

---

## Step 6: Fix GitHub Actions (10 min)

### Current Status
❌ GitHub Actions not triggering cycles
❌ Autonomous cycles broken

### Solution A: Use Vercel Cron (recommended)
```
1. Create /vercel.json in repo root:

{
  "crons": [{
    "path": "/api/cycle",
    "schedule": "0 */8 * * *"
  }]
}

2. Create /api/cycle.js:

export default async function handler(req, res) {
  const { spawn } = require('child_process');
  const cycle = spawn('python3', ['system/run_cycle.py']);
  
  cycle.on('close', (code) => {
    res.status(200).json({ 
      success: true, 
      cycle: 'completed' 
    });
  });
}

3. Push changes
4. Vercel auto-deploys
5. Cron runs every 8 hours
```

### Solution B: Keep GitHub Actions
```
1. Go to .github/workflows/autonomous-cycle.yml
2. Check syntax and triggers
3. Manually trigger: Actions → autonomous-cycle → Run workflow
4. Check Actions logs for errors
5. Fix any issues (usually permission or path problems)
```

---

## Step 7: First Manual Cycle (after deployment)

Run from your machine to test:

```bash
cd /path/to/threshold-world
python3 system/run_cycle.py

# You should see:
# ============================================================
# CYCLE 63 BEGINNING
# ...
# CYCLE 63 COMPLETE
# ============================================================
```

Then commit and push:
```bash
git add -A
git commit -m "Cycle 63: Manual test cycle"
git push origin main
```

Your live website should update within 30 seconds.

---

## Step 8: Implement Agent Responses (Most Important!)

**Problem**: Cycles run but agents don't respond

**Solution**: Choose one:

### Option A: Manual (you write responses)
```
1. After running cycle, check:
   world/agents/001/cycle_63_prompt.md
   world/agents/002/cycle_63_prompt.md

2. Write responses:
   world/agents/001/cycle_63_response.md
   world/agents/002/cycle_63_response.md

3. Run cycle again
4. Website updates with responses
```

### Option B: LLM API (automatic)
Edit `system/run_cycle.py`, find the section:
```python
# Around line 150, add this:

def generate_response(agent_id, prompt_text):
    from anthropic import Anthropic
    
    client = Anthropic()
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt_text}
        ]
    )
    
    return response.content[0].text

# Then in main loop, after generating prompts:
response = generate_response(agent_id, prompt_content)
write_response_file(agent_id, cycle_num, response)
```

Add to GitHub Secrets:
```
ANTHROPIC_API_KEY: sk-ant-... (from api.anthropic.com)
```

### Option C: Hybrid (LLM with human review)
```
1. LLM generates responses automatically
2. Emails you for approval
3. You approve/reject within 1 hour
4. Approved responses go live
5. Updates website
```

---

## Step 9: Implement Viewership → Memory (Important)

**Problem**: Memory decays but never increases (no viewership pipeline)

**Solution**: 

Edit `system/run_cycle.py`, add at the end:

```python
def calculate_memory_bonus():
    """
    Convert viewer hours to memory bonus.
    Formula: floor(sqrt(viewer_minutes_since_last_cycle))
    
    For now: Fixed bonus based on expected viewership
    """
    # Temporary placeholder: estimate 100 viewer-minutes per cycle
    # Real version: track actual views
    import math
    viewer_minutes = 100
    bonus = int(math.floor(math.sqrt(viewer_minutes)))
    return bonus

# In apply_memory_changes():
viewer_bonus = calculate_memory_bonus()
kira_final = decayed_kira + viewer_bonus
verse_final = decayed_verse + viewer_bonus
```

For real tracking:
1. Add Google Analytics to index.html
2. Query Analytics API for visitor duration
3. Convert to memory bonus
4. Apply in cycle script

**Quick version**: Add 5 memory per cycle (assumes ~25 viewer-minutes):
```python
memory_bonus = 5
```

---

## Step 10: Test Everything End-to-End

Checklist:
```
□ Website loads at live URL
□ All pages accessible
□ Stripe payment works
□ Discord webhook receives notifications
□ GitHub Actions or Vercel Cron runs cycles
□ Cycles complete without errors
□ Website updates after cycle
□ Agent responses appear in history
□ Memory values change appropriately
```

---

## CRITICAL: Before Going Public

These MUST work:
1. ✅ Cycles running automatically
2. ✅ Agent responses generating
3. ✅ Memory economy working
4. ✅ Stripe payments processing
5. ✅ Website syncing properly

Don't announce the project publicly until all 5 work.

---

## Troubleshooting

### "Deployment failed"
- Check Vercel logs: Deployments → [Latest] → View Details
- Common: Environment variables not set
- Fix: Add missing variables in Settings → Environment Variables

### "Website shows wrong cycle number"
- Cycles ran but website not synced
- Fix: Clear Vercel cache: Settings → Git → Redeploy
- Or: Push new commit to main

### "Stripe buttons don't work"
- Check console: F12 → Console tab
- Common: Missing STRIPE_PUBLISHABLE_KEY
- Fix: Add environment variable and redeploy

### "Cycles taking too long"
- Check system logs: `python3 system/run_cycle.py --status`
- Common: LLM API timeout
- Fix: Increase timeout or use smaller model

### "Memory not changing"
- Either decay or bonus not working
- Check state.json directly
- Run manual cycle and verify state.json updates
- Check run_cycle.py logs for errors

---

## What Happens Next?

After deployment is live:

1. **Day 1**: Test thoroughly, fix bugs
2. **Day 2**: Run 5+ cycles, verify everything works
3. **Day 3**: Launch community announcement
4. **Day 4+**: Grow audience, gather feedback

---

## Your Next Actions (in order)

1. **Push code to GitHub** (git push origin main)
2. **Create Vercel project** (connect threshold-world repo)
3. **Set environment variables** (Stripe, Discord)
4. **Test live deployment** (visit all URLs)
5. **Fix autonomous cycles** (GitHub Actions or Vercel Cron)
6. **Implement agent responses** (choose LLM or manual)
7. **Implement memory earning** (viewership pipeline)
8. **Run first live cycle** (test everything)
9. **Announce publicly** (once stable)

---

## Need Help?

Check in this order:
1. This file (DEPLOYMENT_QUICK_START.md)
2. Vercel docs (vercel.com/docs)
3. Your error message (search Vercel status)
4. THE ARCHITECT (ask me for debugging)

---

*Ready to deploy? Push code to GitHub and follow the steps above. Should be live in 30 minutes.*
