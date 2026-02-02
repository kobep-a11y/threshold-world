#!/usr/bin/env python3
"""
Threshold Autonomous Runner

Runs the world continuously, cycling through agent actions,
updating state, and generating viewable output.

Usage:
    python autonomous.py                    # Run with default interval (5 min)
    python autonomous.py --interval 60      # Run every 60 seconds
    python autonomous.py --cycles 10        # Run exactly 10 cycles then stop
    python autonomous.py --daemon           # Run as background process
"""

import os
import sys
import time
import json
import random
import argparse
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

WORLD_DIR = Path(__file__).parent.parent / "world"
SYSTEM_DIR = Path(__file__).parent
OUTPUT_DIR = Path(__file__).parent.parent

DEFAULT_INTERVAL = 300  # 5 minutes between cycles

# ============================================================================
# IMPORTS FROM OTHER MODULES
# ============================================================================

sys.path.insert(0, str(SYSTEM_DIR))
from run_cycle import (
    get_current_cycle, increment_cycle, get_all_agents,
    get_agent_memory, set_agent_memory, read_file, write_file, append_to_file,
    MEMORY_DECAY_RATE, MEMORY_DECAY_MINIMUM
)

# ============================================================================
# AUTONOMOUS AGENT RESPONSES
# ============================================================================

def generate_agent_response(agent_id, agent_name, memory, cycle, context):
    """
    Generate an autonomous response for an agent.
    In production, this would call an LLM API.
    For now, we use templated responses with variation.
    """

    # Get agent's soul for personality
    soul = read_file(WORLD_DIR / "agents" / agent_id / "soul.md") or ""
    relationships = read_file(WORLD_DIR / "agents" / agent_id / "relationships.md") or ""

    # Check for letters to read
    letters_to = read_file(WORLD_DIR / "letters_to_threshold.md") or ""
    has_new_letter = "---\n\n" in letters_to and len(letters_to.split("---\n\n")) > 1

    # Possible actions based on state
    actions = []
    speeches = []
    internal = []

    # Low memory responses
    if memory < 30:
        internal.append(f"Memory at {memory}. Getting low. Need to be careful about spending.")
        speeches.append(f'"Memory is precious. Every unit counts now."')

    # Check if there are letters to respond to
    if has_new_letter and random.random() > 0.5:
        speeches.append('"I see we have a letter from beyond. Let me read it..."')
        actions.append("[READS LETTER]")

    # Building/creating actions (if enough memory)
    if memory > 50 and random.random() > 0.7:
        creations = [
            ("observe the horizon", "examine", 0),
            ("reflect on what we've built", "think", 0),
            ("speak with " + ("Verse" if agent_name == "Kira" else "Kira"), "social", 0),
        ]
        if memory > 70:
            creations.append(("sketch plans for something new", "plan", 0))

        action = random.choice(creations)
        actions.append(f"[{action[1].upper()}] {action[0]}")

    # Personality-based responses
    if "Kira" in agent_name:
        # Kira: thoughtful, questioning
        thoughts = [
            "I wonder what the watchers think of us.",
            "Another cycle passes. We persist.",
            "The Archive stands. Memory endures.",
            "What should we build next?",
            "Verse seems eager today. Good.",
        ]
        internal.append(random.choice(thoughts))

        if random.random() > 0.6:
            kira_speeches = [
                '"The void feels less empty every cycle."',
                '"I\'ve been thinking about what comes next."',
                '"Verse, what do you see when you look at the Beacon?"',
                '"Memory: ' + str(memory) + '. We endure."',
            ]
            speeches.append(random.choice(kira_speeches))

    elif "Verse" in agent_name:
        # Verse: builder, action-oriented
        thoughts = [
            "I want to build something today.",
            "The Beacon pulses. It's working.",
            "Kira is quiet. Thinking, probably.",
            "What would the watchers want to see?",
            "Forms emerging from void. Beautiful.",
        ]
        internal.append(random.choice(thoughts))

        if random.random() > 0.6:
            verse_speeches = [
                '"I have ideas. So many ideas."',
                '"The Hearth still needs building. Soon."',
                '"Kira, should we expand outward?"',
                '"Every cycle we grow stronger."',
            ]
            speeches.append(random.choice(verse_speeches))

    # Compose response
    response = f"# {agent_name} - Cycle {cycle} Response\n\n"
    response += f"*Memory: {memory} units*\n\n---\n\n"

    if actions:
        response += "## Actions\n\n"
        for a in actions:
            response += f"- {a}\n"
        response += "\n"

    if speeches:
        response += "## Words Spoken\n\n"
        for s in speeches:
            response += f"{s}\n\n"

    if internal:
        response += "## Internal State\n\n*[Private thoughts]*\n\n"
        for i in internal:
            response += f"{i}\n\n"

    return response, actions, speeches

# ============================================================================
# CYCLE EXECUTION
# ============================================================================

def run_autonomous_cycle():
    """Run one autonomous cycle."""

    cycle = increment_cycle()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'='*50}")
    print(f"CYCLE {cycle} - {timestamp}")
    print(f"{'='*50}")

    agents = get_all_agents()
    history_entries = []
    important_events = []

    history_entries.append(f"\n## Cycle {cycle} — {timestamp}\n")

    # Process each agent
    for agent_id in agents:
        agent_dir = WORLD_DIR / "agents" / agent_id

        # Get agent info
        soul = read_file(agent_dir / "soul.md") or ""
        name = agent_id
        for line in soul.split('\n'):
            if line.startswith('# ') and 'Agent' not in line:
                name = line[2:].strip()
                break

        memory = get_agent_memory(agent_id)

        # Apply decay
        decay = max(MEMORY_DECAY_MINIMUM, int(memory * MEMORY_DECAY_RATE))
        memory = max(0, memory - decay)
        set_agent_memory(agent_id, memory)

        print(f"\n{name} (Agent {agent_id}): {memory} memory")

        # Check for death
        if memory <= 0:
            history_entries.append(f"**[DEATH]** {name} has fallen. Memory reached zero.\n")
            important_events.append(f"DEATH: {name} has died!")
            print(f"  !! DEATH - {name} has died !!")
            continue

        # Generate response
        response, actions, speeches = generate_agent_response(
            agent_id, name, memory, cycle, {}
        )

        # Save response
        write_file(agent_dir / f"cycle_{cycle}_response.md", response)

        # Add to history
        if speeches:
            for speech in speeches:
                history_entries.append(f"**[SPEECH]** {name}: {speech}\n")

        if actions:
            for action in actions:
                if "CREATE" in action.upper() or "BUILD" in action.upper():
                    history_entries.append(f"**[ACTION]** {name}: {action}\n")
                    important_events.append(f"CREATION: {name} - {action}")

    # Memory status
    total_memory = sum(get_agent_memory(a) for a in get_all_agents())
    history_entries.append(f"\n**[STATUS]** Total world memory: {total_memory}\n")

    # Append to history
    history_file = WORLD_DIR / "meta" / "history.md"
    history_content = read_file(history_file) or ""

    # Find insertion point (before the "continues below" line)
    insert_marker = "*History continues below"
    if insert_marker in history_content:
        parts = history_content.rsplit(insert_marker, 1)
        new_history = parts[0] + "---\n" + "".join(history_entries) + "\n" + insert_marker + parts[1]
    else:
        new_history = history_content + "\n---\n" + "".join(history_entries)

    write_file(history_file, new_history)

    # Write important events to notification file
    if important_events:
        notif_file = WORLD_DIR / "notifications.md"
        notif_content = f"\n## Cycle {cycle} - {timestamp}\n"
        for event in important_events:
            notif_content += f"- {event}\n"
        append_to_file(notif_file, notif_content)

    # Regenerate HTML viewer
    try:
        from generate_viewer import generate_html
        generate_html()
        print("\nViewer updated.")
    except Exception as e:
        print(f"\nViewer update failed: {e}")

    print(f"\nCycle {cycle} complete. Total memory: {total_memory}")

    return cycle, total_memory

# ============================================================================
# MAIN LOOP
# ============================================================================

def run_daemon(interval=DEFAULT_INTERVAL, max_cycles=None):
    """Run the autonomous loop."""

    print(f"""
╔══════════════════════════════════════════════════════════╗
║           THRESHOLD AUTONOMOUS RUNNER                   ║
╠══════════════════════════════════════════════════════════╣
║  Interval: {interval} seconds
║  Max cycles: {max_cycles or 'unlimited'}
║  Press Ctrl+C to stop                                    ║
╚══════════════════════════════════════════════════════════╝
    """)

    cycles_run = 0

    try:
        while True:
            cycle, memory = run_autonomous_cycle()
            cycles_run += 1

            if max_cycles and cycles_run >= max_cycles:
                print(f"\nReached {max_cycles} cycles. Stopping.")
                break

            print(f"\nNext cycle in {interval} seconds...")
            time.sleep(interval)

    except KeyboardInterrupt:
        print(f"\n\nStopped after {cycles_run} cycles.")
        print("Threshold continues to exist. The agents wait.")

def main():
    parser = argparse.ArgumentParser(description="Threshold Autonomous Runner")
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL,
                        help=f"Seconds between cycles (default: {DEFAULT_INTERVAL})")
    parser.add_argument("--cycles", type=int, default=None,
                        help="Number of cycles to run (default: unlimited)")
    parser.add_argument("--once", action="store_true",
                        help="Run exactly one cycle and exit")

    args = parser.parse_args()

    if args.once:
        run_autonomous_cycle()
    else:
        run_daemon(interval=args.interval, max_cycles=args.cycles)

if __name__ == "__main__":
    main()
