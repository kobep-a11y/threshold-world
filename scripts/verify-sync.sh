#!/bin/bash
# Threshold World Sync Verification
# Run this before and after each session to ensure consistency

set -e

echo "=== THRESHOLD WORLD SYNC VERIFICATION ==="
echo "Timestamp: $(date)"
echo ""

# Navigate to project root
cd "$(dirname "$0")/.."

# Get values from state.json
CYCLE=$(cat world/meta/state.json | grep '"cycle"' | grep -o '[0-9]*')
KIRA_MEM=$(cat world/meta/state.json | grep '"kira_memory"' | grep -o '[0-9]*')
VERSE_MEM=$(cat world/meta/state.json | grep '"verse_memory"' | grep -o '[0-9]*')
DAY=$(cat world/meta/state.json | grep '"day"' | grep -o '[0-9]*')
TOTAL_MEM=$((KIRA_MEM + VERSE_MEM))

echo "--- SOURCE OF TRUTH: state.json ---"
echo "  Cycle: $CYCLE"
echo "  Day: $DAY"
echo "  Kira Memory: $KIRA_MEM"
echo "  Verse Memory: $VERSE_MEM"
echo "  Total Memory: $TOTAL_MEM"
echo ""

# Initialize counters
ERRORS=0
WARNINGS=0

echo "--- FILE SYNC CHECKS ---"

# Check index.html (root)
if [ -f "index.html" ]; then
    INDEX_CYCLE=$(grep -o "CYCLE [0-9]*" index.html | head -1 | grep -o '[0-9]*' || echo "0")
    if [ "$CYCLE" != "$INDEX_CYCLE" ]; then
        echo "ERROR: index.html cycle mismatch! state.json=$CYCLE, index.html=$INDEX_CYCLE"
        ERRORS=$((ERRORS + 1))
    else
        echo "OK: index.html cycle matches ($CYCLE)"
    fi
else
    echo "WARNING: index.html not found"
    WARNINGS=$((WARNINGS + 1))
fi

# Check website/index.html
if [ -f "website/index.html" ]; then
    WEBSITE_CYCLE=$(grep -o "CYCLE [0-9]*" website/index.html | head -1 | grep -o '[0-9]*' || echo "0")
    if [ "$CYCLE" != "$WEBSITE_CYCLE" ]; then
        echo "ERROR: website/index.html cycle mismatch! state.json=$CYCLE, website/index.html=$WEBSITE_CYCLE"
        ERRORS=$((ERRORS + 1))
    else
        echo "OK: website/index.html cycle matches ($CYCLE)"
    fi
else
    echo "WARNING: website/index.html not found"
    WARNINGS=$((WARNINGS + 1))
fi

# Check world-viewer.html
if [ -f "world-viewer.html" ]; then
    VIEWER_CYCLE=$(grep -o 'cycle-num">[0-9]*' world-viewer.html | grep -o '[0-9]*' || echo "0")
    if [ "$CYCLE" != "$VIEWER_CYCLE" ]; then
        echo "WARNING: world-viewer.html fallback cycle mismatch ($VIEWER_CYCLE vs $CYCLE) - OK if dynamic fetch works"
        WARNINGS=$((WARNINGS + 1))
    else
        echo "OK: world-viewer.html cycle matches ($CYCLE)"
    fi
else
    echo "WARNING: world-viewer.html not found"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "--- AGENT RESPONSE CHECKS ---"

# Check latest agent responses exist
KIRA_LATEST=$(ls -1 world/agents/001/cycle_*_response.md 2>/dev/null | sort -V | tail -1)
VERSE_LATEST=$(ls -1 world/agents/002/cycle_*_response.md 2>/dev/null | sort -V | tail -1)

if [ -n "$KIRA_LATEST" ]; then
    KIRA_CYCLE=$(echo "$KIRA_LATEST" | grep -o 'cycle_[0-9]*' | grep -o '[0-9]*')
    if [ "$KIRA_CYCLE" == "$CYCLE" ]; then
        echo "OK: Kira has response for cycle $CYCLE"
    else
        echo "WARNING: Kira latest response is cycle $KIRA_CYCLE, state shows $CYCLE"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "ERROR: No Kira responses found"
    ERRORS=$((ERRORS + 1))
fi

if [ -n "$VERSE_LATEST" ]; then
    VERSE_CYCLE=$(echo "$VERSE_LATEST" | grep -o 'cycle_[0-9]*' | grep -o '[0-9]*')
    if [ "$VERSE_CYCLE" == "$CYCLE" ]; then
        echo "OK: Verse has response for cycle $CYCLE"
    else
        echo "WARNING: Verse latest response is cycle $VERSE_CYCLE, state shows $CYCLE"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "ERROR: No Verse responses found"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "--- GIT STATUS CHECKS ---"

# Check for untracked files
UNTRACKED=$(git status --porcelain 2>/dev/null | grep "^??" | wc -l | tr -d ' ')
if [ "$UNTRACKED" -gt 0 ]; then
    echo "WARNING: $UNTRACKED untracked file(s)"
    git status --porcelain | grep "^??" | head -5
    if [ "$UNTRACKED" -gt 5 ]; then
        echo "  ... and $((UNTRACKED - 5)) more"
    fi
    WARNINGS=$((WARNINGS + 1))
else
    echo "OK: No untracked files"
fi

# Check for uncommitted changes
MODIFIED=$(git status --porcelain 2>/dev/null | grep -v "^??" | wc -l | tr -d ' ')
if [ "$MODIFIED" -gt 0 ]; then
    echo "INFO: $MODIFIED file(s) with uncommitted changes"
    git status --porcelain | grep -v "^??" | head -5
fi

echo ""
echo "--- ARCHITECT.MD CHECK ---"

# Check ARCHITECT.md last update
ARCH_CYCLE=$(grep "Last Updated.*Cycle" ARCHITECT.md | grep -o "Cycle [0-9]*" | grep -o '[0-9]*')
if [ -n "$ARCH_CYCLE" ]; then
    if [ "$ARCH_CYCLE" != "$CYCLE" ]; then
        echo "WARNING: ARCHITECT.md shows Cycle $ARCH_CYCLE, state shows $CYCLE"
        WARNINGS=$((WARNINGS + 1))
    else
        echo "OK: ARCHITECT.md is up to date"
    fi
else
    echo "WARNING: Could not parse ARCHITECT.md cycle"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "=========================================="
echo "SUMMARY"
echo "=========================================="
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [ "$ERRORS" -gt 0 ]; then
    echo "FAILED: Fix $ERRORS error(s) before proceeding"
    echo ""
    echo "Quick fix: Run 'python system/update_website.py' to sync HTML files"
    exit 1
elif [ "$WARNINGS" -gt 0 ]; then
    echo "PASSED with warnings: Review $WARNINGS warning(s)"
    echo ""
    echo "To auto-fix HTML sync issues: python system/update_website.py"
    exit 0
else
    echo "ALL CHECKS PASSED"
    exit 0
fi
