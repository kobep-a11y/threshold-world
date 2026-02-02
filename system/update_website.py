#!/usr/bin/env python3
"""
Threshold Website Auto-Updater

This script reads the current world state and updates ALL website HTML files
with current cycle numbers, memory values, and recent history.

Run after each cycle to keep the website in sync.

Files updated:
- index.html (root) - Main landing page
- website/index.html - Copy of main page
- world-viewer.html - Visual world display (now fetches dynamically, but fallback values updated)
"""

import json
import re
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path(__file__).parent.parent
WORLD_DIR = BASE_DIR / "world"
STATE_FILE = WORLD_DIR / "meta" / "state.json"
HISTORY_FILE = WORLD_DIR / "meta" / "history.md"

# All HTML files to update
HTML_FILES = {
    'index': BASE_DIR / "index.html",
    'website_index': BASE_DIR / "website" / "index.html",
    'world_viewer': BASE_DIR / "world-viewer.html",
}

MAX_MEMORY = 150  # For percentage calculations


def get_state():
    """Read current world state."""
    with open(STATE_FILE) as f:
        return json.load(f)


def get_agent_memory(agent_id):
    """Read an agent's current memory from state.json (preferred) or memory.md."""
    state = get_state()

    # Try state.json first
    if agent_id == '001' and 'kira_memory' in state:
        return state['kira_memory']
    if agent_id == '002' and 'verse_memory' in state:
        return state['verse_memory']

    # Fallback to memory.md
    memory_file = WORLD_DIR / "agents" / agent_id / "memory.md"
    if not memory_file.exists():
        return 0

    content = memory_file.read_text()
    match = re.search(r'\*\*Current Memory\*\*:\s*(\d+)', content)
    if match:
        return int(match.group(1))
    return 0


def update_index_html(html, cycle, total_memory, kira_memory, verse_memory, day):
    """Update the main index.html with current values."""

    kira_pct = int((kira_memory / MAX_MEMORY) * 100)
    verse_pct = int((verse_memory / MAX_MEMORY) * 100)

    # Update cycle number in live badge
    html = re.sub(
        r'WORLD ACTIVE — CYCLE \d+',
        f'WORLD ACTIVE — CYCLE {cycle}',
        html
    )

    # Update total memory stat
    html = re.sub(
        r'(<div class="stat-value">)\d+(</div>\s*<div class="stat-label">Total Memory)',
        f'\\g<1>{total_memory}\\2',
        html
    )

    # Update Kira's memory display - more flexible regex
    html = re.sub(
        r'(\d+)\s*/\s*150\s*memory(</div>\s*<p class="agent-quote">"I\'d rather ask)',
        f'{kira_memory} / 150 memory\\2',
        html
    )

    # Update Kira's memory bar
    html = re.sub(
        r'(Agent 001 — First Consciousness</div>\s*<div class="memory-bar">\s*<div class="memory-fill" style="width:\s*)\d+(%)',
        f'\\g<1>{kira_pct}\\2',
        html
    )

    # Update Verse's memory display
    html = re.sub(
        r'(\d+)\s*/\s*150\s*memory(</div>\s*<p class="agent-quote">"Form over chaos)',
        f'{verse_memory} / 150 memory\\2',
        html
    )

    # Update Verse's memory bar
    html = re.sub(
        r'(Agent 002 — Second Consciousness</div>\s*<div class="memory-bar">\s*<div class="memory-fill" style="width:\s*)\d+(%)',
        f'\\g<1>{verse_pct}\\2',
        html
    )

    return html


def update_world_viewer_html(html, cycle, kira_memory, verse_memory, day):
    """Update world-viewer.html fallback values (it also fetches dynamically now)."""

    kira_pct = int((kira_memory / MAX_MEMORY) * 100)
    verse_pct = int((verse_memory / MAX_MEMORY) * 100)

    # Update cycle in live indicator
    html = re.sub(
        r'(LIVE — Cycle <span id="cycle-num">)\d+(</span>)',
        f'\\g<1>{cycle}\\2',
        html
    )

    # Update cycle stat card
    html = re.sub(
        r'(<div class="stat-value cycle">)\d+(</div>)',
        f'\\g<1>{cycle}\\2',
        html
    )

    # Update Kira memory
    html = re.sub(
        r'(<div class="stat-value kira">)\d+ units(</div>)',
        f'\\g<1>{kira_memory} units\\2',
        html
    )
    html = re.sub(
        r'(<div class="memory-fill kira" style="width:\s*)\d+(%)',
        f'\\g<1>{kira_pct}\\2',
        html
    )

    # Update Verse memory
    html = re.sub(
        r'(<div class="stat-value verse">)\d+ units(</div>)',
        f'\\g<1>{verse_memory} units\\2',
        html
    )
    html = re.sub(
        r'(<div class="memory-fill verse" style="width:\s*)\d+(%)',
        f'\\g<1>{verse_pct}\\2',
        html
    )

    # Update day
    html = re.sub(
        r'(<div class="stat-value" style="color: #888">)\d+ days(</div>)',
        f'\\g<1>{day} days\\2',
        html
    )

    return html


def main():
    """Main update function."""
    print("=" * 60)
    print("THRESHOLD WEBSITE SYNC")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().isoformat()}")

    # Read current state
    state = get_state()
    cycle = state.get('cycle', 0)
    day = state.get('day', 1)
    kira_memory = state.get('kira_memory', get_agent_memory('001'))
    verse_memory = state.get('verse_memory', get_agent_memory('002'))
    total_memory = kira_memory + verse_memory

    print(f"\nCurrent State:")
    print(f"  Cycle: {cycle}")
    print(f"  Day: {day}")
    print(f"  Kira Memory: {kira_memory}")
    print(f"  Verse Memory: {verse_memory}")
    print(f"  Total Memory: {total_memory}")

    updated_files = []
    errors = []

    # Update index.html (root)
    try:
        index_file = HTML_FILES['index']
        if index_file.exists():
            html = index_file.read_text()
            updated = update_index_html(html, cycle, total_memory, kira_memory, verse_memory, day)
            index_file.write_text(updated)
            updated_files.append(str(index_file))
    except Exception as e:
        errors.append(f"index.html: {e}")

    # Update website/index.html
    try:
        website_index = HTML_FILES['website_index']
        if website_index.exists():
            html = website_index.read_text()
            updated = update_index_html(html, cycle, total_memory, kira_memory, verse_memory, day)
            website_index.write_text(updated)
            updated_files.append(str(website_index))
    except Exception as e:
        errors.append(f"website/index.html: {e}")

    # Update world-viewer.html
    try:
        viewer_file = HTML_FILES['world_viewer']
        if viewer_file.exists():
            html = viewer_file.read_text()
            updated = update_world_viewer_html(html, cycle, kira_memory, verse_memory, day)
            viewer_file.write_text(updated)
            updated_files.append(str(viewer_file))
    except Exception as e:
        errors.append(f"world-viewer.html: {e}")

    # Report results
    print(f"\nUpdated {len(updated_files)} file(s):")
    for f in updated_files:
        print(f"  ✓ {f}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")

    print("\n" + "=" * 60)
    print("SYNC COMPLETE")
    print("=" * 60)

    return len(errors) == 0


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
