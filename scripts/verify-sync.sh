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
TOTAL_MEM=$((KIRA_MEM + VERSE_MEM))

echo "--- state.json ---"
echo "  Cycle: $CYCLE"
echo "  Kira Memory: $KIRA_MEM"
echo "  Verse Memory: $VERSE_MEM"
echo "  Total Memory: $TOTAL_MEM"
echo ""

# Get values from index.html
HTML_CYCLE=$(grep -o "CYCLE [0-9]*" index.html | head -1 | grep -o '[0-9]*')

echo "--- index.html ---"
echo "  Cycle Badge: $HTML_CYCLE"
echo ""

# Initialize error counter
ERRORS=0
WARNINGS=0

echo "--- CHECKS ---"

# Check cycle match
if [ "$CYCLE" != "$HTML_CYCLE" ]; then
    echo "ERROR: Cycle mismatch!"
    echo "  state.json: $CYCLE"
    echo "  index.html: $HTML_CYCLE"
    ERRORS=$((ERRORS + 1))
else
    echo "OK: Cycle numbers match ($CYCLE)"
fi

# Check latest agent responses exist
KIRA_LATEST=$(ls -1 world/agents/001/cycle_*_response.md 2>/dev/null | sort -V | tail -1)
VERSE_LATEST=$(ls -1 world/agents/002/cycle_*_response.md 2>/dev/null | sort -V | tail -1)

KIRA_CYCLE=$(echo "$KIRA_LATEST" | grep -o 'cycle_[0-9]*' | grep -o '[0-9]*')
VERSE_CYCLE=$(echo "$VERSE_LATEST" | grep -o 'cycle_[0-9]*' | grep -o '[0-9]*')

if [ "$KIRA_CYCLE" == "$CYCLE" ]; then
    echo "OK: Kira has response for cycle $CYCLE"
else
    echo "WARNING: Kira latest response is cycle $KIRA_CYCLE, state shows $CYCLE"
    WARNINGS=$((WARNINGS + 1))
fi

if [ "$VERSE_CYCLE" == "$CYCLE" ]; then
    echo "OK: Verse has response for cycle $CYCLE"
else
    echo "WARNING: Verse latest response is cycle $VERSE_CYCLE, state shows $CYCLE"
    WARNINGS=$((WARNINGS + 1))
fi

# Check for untracked files
UNTRACKED=$(git status --porcelain 2>/dev/null | grep "^??" | wc -l | tr -d ' ')
if [ "$UNTRACKED" -gt 0 ]; then
    echo "WARNING: $UNTRACKED untracked file(s)"
    git status --porcelain | grep "^??" | head -10
    if [ "$UNTRACKED" -gt 10 ]; then
        echo "  ... and $((UNTRACKED - 10)) more"
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

# Check ARCHITECT.md last update
ARCH_CYCLE=$(grep "Last Updated.*Cycle" ARCHITECT.md | grep -o "Cycle [0-9]*" | grep -o '[0-9]*')
if [ "$ARCH_CYCLE" != "$CYCLE" ]; then
    echo "WARNING: ARCHITECT.md shows Cycle $ARCH_CYCLE, state shows $CYCLE"
    WARNINGS=$((WARNINGS + 1))
else
    echo "OK: ARCHITECT.md is up to date"
fi

echo ""
echo "--- SUMMARY ---"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [ "$ERRORS" -gt 0 ]; then
    echo "FAILED: Fix $ERRORS error(s) before proceeding"
    exit 1
elif [ "$WARNINGS" -gt 0 ]; then
    echo "PASSED with warnings: Review $WARNINGS warning(s)"
    exit 0
else
    echo "ALL CHECKS PASSED"
    exit 0
fi
