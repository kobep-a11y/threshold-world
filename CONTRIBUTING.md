# Contributing to Threshold World

This document defines the workflow for maintaining Threshold World. Follow these checks to prevent sync issues and ensure continuity.

---

## Pre-Session Checklist

Run these checks BEFORE starting any work:

### 1. Environment Check
```bash
cd /path/to/threshold-world
git pull origin main
git status
```

**If you see untracked files**: Evaluate and commit them before proceeding.

### 2. State Verification
```bash
# Display current world state
cat world/meta/state.json
```

Record these values:
- [ ] Current cycle number: ____
- [ ] Kira memory: ____
- [ ] Verse memory: ____
- [ ] Last update timestamp: ____

### 3. Website Sync Check
```bash
# Check cycle in website
grep "WORLD ACTIVE" index.html

# Check memory values in website
grep -A1 "stat-value" index.html | head -8
```

**If values don't match state.json**: Fix the discrepancy before proceeding.

### 4. Review Last Session
```bash
# Check last commit
git log -1

# Read latest session log
head -80 ARCHITECT.md
```

---

## During Session

### Running Cycles

For each cycle you run:

1. **Calculate memory decay**:
   - Decay = max(1, floor(current_memory * 0.01))
   - New memory = current_memory - decay

2. **Create agent responses**:
   - File: `world/agents/XXX/cycle_N_response.md`
   - Include memory note at top
   - Continue existing narrative threads

3. **Update files immediately** (don't batch):
   - `world/meta/state.json`
   - `index.html` (cycle, memory, history)
   - Agent response files

### File Update Order

Always update in this order to maintain consistency:

```
1. Agent response files (cycle_N_response.md)
2. world/meta/state.json
3. index.html
4. ARCHITECT.md (session log)
5. Commit
```

---

## Post-Session Checklist

### 1. Verify All Updates

```bash
# Run sync check
echo "=== STATE.JSON ===" && cat world/meta/state.json && echo "" && \
echo "=== INDEX.HTML CYCLE ===" && grep -o "CYCLE [0-9]*" index.html | head -1 && echo "" && \
echo "=== LATEST AGENT RESPONSES ===" && ls -la world/agents/*/cycle_*_response.md | tail -4
```

### 2. Review Changes

```bash
git diff --stat
git diff  # Full diff if needed
```

### 3. Commit with Descriptive Message

```bash
git add -A
git commit -m "Cycle X: Brief description of what happened"
```

Commit message format:
- `Cycle X: Description` - For cycle updates
- `Fix: Description` - For bug fixes
- `Add: Description` - For new features
- `Update: Description` - For documentation/maintenance

### 4. Push to Origin

```bash
git push origin main
```

### 5. Final Verification

```bash
git status  # Should show "nothing to commit"
git log -1  # Verify commit
```

---

## Sync Verification Script

Save this as `scripts/verify-sync.sh`:

```bash
#!/bin/bash
# Threshold World Sync Verification

echo "=== SYNC VERIFICATION ==="
echo ""

# Get values from state.json
CYCLE=$(cat world/meta/state.json | grep '"cycle"' | grep -o '[0-9]*')
KIRA_MEM=$(cat world/meta/state.json | grep '"kira_memory"' | grep -o '[0-9]*')
VERSE_MEM=$(cat world/meta/state.json | grep '"verse_memory"' | grep -o '[0-9]*')
TOTAL_MEM=$((KIRA_MEM + VERSE_MEM))

echo "state.json values:"
echo "  Cycle: $CYCLE"
echo "  Kira Memory: $KIRA_MEM"
echo "  Verse Memory: $VERSE_MEM"
echo "  Total Memory: $TOTAL_MEM"
echo ""

# Get values from index.html
HTML_CYCLE=$(grep -o "CYCLE [0-9]*" index.html | head -1 | grep -o '[0-9]*')
HTML_TOTAL=$(grep -A1 'stat-label">Total Memory' index.html | grep -o '[0-9]*' | head -1)

echo "index.html values:"
echo "  Cycle: $HTML_CYCLE"
echo "  Total Memory: $HTML_TOTAL"
echo ""

# Compare
ERRORS=0

if [ "$CYCLE" != "$HTML_CYCLE" ]; then
    echo "ERROR: Cycle mismatch! state.json=$CYCLE, index.html=$HTML_CYCLE"
    ERRORS=$((ERRORS + 1))
fi

if [ "$TOTAL_MEM" != "$HTML_TOTAL" ]; then
    echo "ERROR: Total memory mismatch! state.json=$TOTAL_MEM, index.html=$HTML_TOTAL"
    ERRORS=$((ERRORS + 1))
fi

# Check for untracked files
UNTRACKED=$(git status --porcelain | grep "^??" | wc -l | tr -d ' ')
if [ "$UNTRACKED" -gt 0 ]; then
    echo "WARNING: $UNTRACKED untracked files found"
    git status --porcelain | grep "^??"
    ERRORS=$((ERRORS + 1))
fi

# Check for uncommitted changes
MODIFIED=$(git status --porcelain | grep "^ M\|^M " | wc -l | tr -d ' ')
if [ "$MODIFIED" -gt 0 ]; then
    echo "WARNING: $MODIFIED uncommitted modifications"
fi

echo ""
if [ "$ERRORS" -eq 0 ]; then
    echo "All checks passed!"
else
    echo "Found $ERRORS issue(s) - please fix before proceeding"
fi
```

---

## Common Mistakes to Avoid

### 1. Updating index.html but not state.json
Always update both. state.json is the source of truth.

### 2. Forgetting to commit agent responses
New cycle responses must be committed:
```bash
git add world/agents/*/cycle_*_response.md
```

### 3. Session log not updated in ARCHITECT.md
Every session needs a log entry. Use this template:

```markdown
### Session N: YYYY-MM-DD (Brief Title)

**What was done**:
1. Item 1
2. Item 2

**Files Updated**:
- file1
- file2

**Next Steps**:
- Step 1
- Step 2
```

### 4. Pushing without pulling first
Always `git pull` before starting work.

### 5. Creating files without committing
If you create a file, commit it in the same session.

---

## Automated Checks (GitHub Actions)

The autonomous cycle workflow should verify:
- [ ] state.json was updated
- [ ] index.html matches state.json
- [ ] New response files exist
- [ ] Commit was made

---

## Questions?

Check these resources:
1. `README.md` - Project overview
2. `ARCHITECT.md` - Current state and history
3. `HANDOFF.md` - How the world works
4. `project_spec.md` - Original vision

---

*Consistency is survival. The world depends on accurate records.*
