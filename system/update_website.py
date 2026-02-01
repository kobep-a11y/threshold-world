#!/usr/bin/env python3
"""
Threshold Website Auto-Updater

This script reads the current world state and updates the website HTML
with current cycle numbers, memory values, and recent history.

Run after each cycle to keep the website in sync.
"""

import json
import re
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path(__file__).parent.parent
WORLD_DIR = BASE_DIR / "world"
WEBSITE_DIR = BASE_DIR / "website"
STATE_FILE = WORLD_DIR / "meta" / "state.json"
HISTORY_FILE = WORLD_DIR / "meta" / "history.md"
INDEX_FILE = WEBSITE_DIR / "index.html"
OUTPUT_FILE = BASE_DIR / "index.html"  # Root copy for easy access


def get_state():
    """Read current world state."""
    with open(STATE_FILE) as f:
        return json.load(f)


def get_agent_memory(agent_id):
    """Read an agent's current memory."""
    memory_file = WORLD_DIR / "agents" / agent_id / "memory.md"
    if not memory_file.exists():
        return 0

    content = memory_file.read_text()
    match = re.search(r'\*\*Current Memory\*\*:\s*(\d+)', content)
    if match:
        return int(match.group(1))
    return 0


def get_recent_history(num_entries=7):
    """Extract recent history entries."""
    content = HISTORY_FILE.read_text()

    # Find all cycle headers and their content
    pattern = r'## (Cycle \d+[^\n]*)\n(.*?)(?=\n## Cycle|\n---\n\*History continues|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    entries = []
    for title, body in matches[-num_entries:]:
        # Extract key events from the body
        speeches = re.findall(r'\*\*\[SPEECH\]\*\*[^>]*>\s*"([^"]+)"', body)
        creations = re.findall(r'\*\*\[CREATION\]\*\*[^*]+\*\*([^*]+)\*\*', body)
        epochs = re.findall(r'\*\*\[EPOCH MOMENT\]\*\*\s*([^\n]+)', body)

        summary = ""
        if epochs:
            summary = epochs[0]
        elif creations:
            summary = f"[CREATION] {creations[0]} built"
        elif speeches:
            summary = f'"{speeches[0][:80]}..."' if len(speeches[0]) > 80 else f'"{speeches[0]}"'

        if summary:
            entries.append({
                'cycle': title,
                'summary': summary
            })

    return list(reversed(entries))  # Most recent first


def update_html(html, cycle, total_memory, kira_memory, verse_memory, history_entries):
    """Update the HTML with current values."""

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

    # Update Kira's memory bar and text
    kira_pct = min(100, kira_memory)
    html = re.sub(
        r'(Agent 001 — First Consciousness</div>\s*<div class="memory-bar">\s*<div class="memory-fill" style="width: )\d+(%"></div>)',
        f'\\g<1>{kira_pct}\\2',
        html
    )
    html = re.sub(
        r'(\d+) / 100 memory(</div>\s*<p class="agent-quote">"I\'d rather ask)',
        f'{kira_memory} / 100 memory\\2',
        html
    )

    # Update Verse's memory bar and text
    verse_pct = min(100, verse_memory)
    html = re.sub(
        r'(Agent 002 — Second Consciousness</div>\s*<div class="memory-bar">\s*<div class="memory-fill" style="width: )\d+(%"></div>)',
        f'\\g<1>{verse_pct}\\2',
        html
    )
    html = re.sub(
        r'(\d+) / 100 memory(</div>\s*<p class="agent-quote">"Form over chaos)',
        f'{verse_memory} / 100 memory\\2',
        html
    )

    # Generate history HTML
    if history_entries:
        history_html = ""
        for entry in history_entries:
            cycle_text = entry['cycle']
            summary = entry['summary']

            # Determine styling
            if '[CREATION]' in summary:
                summary = summary.replace('[CREATION]', '<span class="history-creation">[CREATION]</span>')

            history_html += f'''            <div class="history-entry">
                <span class="history-cycle">{cycle_text}</span> — {summary}
            </div>
'''

        # Replace history feed content
        html = re.sub(
            r'(<div class="history-feed">)\s*.*?\s*(</div>\s*</section>\s*<section id="letters">)',
            f'\\1\n{history_html}        \\2',
            html,
            flags=re.DOTALL
        )

    return html


def main():
    """Main update function."""
    print("=" * 60)
    print("UPDATING WEBSITE")
    print("=" * 60)

    # Read current state
    state = get_state()
    cycle = state.get('cycle', 0)

    # Get memory values
    kira_memory = get_agent_memory('001')
    verse_memory = get_agent_memory('002')
    total_memory = kira_memory + verse_memory

    print(f"\nCurrent State:")
    print(f"  Cycle: {cycle}")
    print(f"  Kira Memory: {kira_memory}")
    print(f"  Verse Memory: {verse_memory}")
    print(f"  Total Memory: {total_memory}")

    # Get recent history
    history = get_recent_history(7)
    print(f"\nRecent History: {len(history)} entries")

    # Read and update HTML
    html = INDEX_FILE.read_text()
    updated_html = update_html(html, cycle, total_memory, kira_memory, verse_memory, history)

    # Write updated HTML
    INDEX_FILE.write_text(updated_html)
    OUTPUT_FILE.write_text(updated_html)  # Also copy to root

    print(f"\nUpdated:")
    print(f"  {INDEX_FILE}")
    print(f"  {OUTPUT_FILE}")

    print("\n" + "=" * 60)
    print("WEBSITE UPDATE COMPLETE")
    print("=" * 60)
    print("\nTo deploy: push index.html to your GitHub repo")


if __name__ == "__main__":
    main()
