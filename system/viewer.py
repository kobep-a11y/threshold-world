#!/usr/bin/env python3
"""
Threshold World Viewer

A terminal-based viewer for watching the world of Threshold.

Usage:
    python viewer.py                    # Show current world state
    python viewer.py --history          # Show full history
    python viewer.py --agents           # Show agent details
    python viewer.py --watch            # Live mode: run cycles and display
    python viewer.py --cycle            # Run one cycle and show results
"""

import os
import sys
import time
import argparse
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

WORLD_DIR = Path(__file__).parent.parent / "world"

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# ============================================================================
# UTILITIES
# ============================================================================

def read_file(path):
    """Read a file's contents."""
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def clear_screen():
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Print a styled header."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}  {text}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═' * 60}{Colors.RESET}\n")

def print_subheader(text):
    """Print a styled subheader."""
    print(f"\n{Colors.YELLOW}── {text} ──{Colors.RESET}\n")

def print_agent(name, agent_id, memory, status="Active"):
    """Print agent info in a nice format."""
    color = Colors.GREEN if memory > 50 else Colors.YELLOW if memory > 20 else Colors.RED
    print(f"  {Colors.BOLD}{name}{Colors.RESET} (Agent {agent_id})")
    print(f"    Memory: {color}{memory} units{Colors.RESET}")
    print(f"    Status: {status}")

# ============================================================================
# WORLD STATE
# ============================================================================

def get_world_name():
    """Get the world's name."""
    content = read_file(WORLD_DIR / "meta" / "world_name.md")
    if content and "THRESHOLD" in content.upper():
        return "Threshold"
    return "Unnamed World"

def get_current_cycle():
    """Get current cycle from state file."""
    import json
    state_file = WORLD_DIR / "meta" / "state.json"
    if state_file.exists():
        with open(state_file) as f:
            return json.load(f).get("cycle", 0)
    # Count from history if no state file
    history = read_file(WORLD_DIR / "meta" / "history.md") or ""
    cycles = history.count("## Cycle")
    return max(0, cycles)

def get_agents():
    """Get all agents with their info."""
    agents = []
    agents_dir = WORLD_DIR / "agents"
    if not agents_dir.exists():
        return agents

    for agent_dir in sorted(agents_dir.iterdir()):
        if not agent_dir.is_dir() or "archived" in agent_dir.name:
            continue

        agent_id = agent_dir.name

        # Get name from soul
        soul = read_file(agent_dir / "soul.md") or ""
        name = agent_id
        for line in soul.split('\n'):
            if line.startswith('# ') and 'Agent' not in line:
                name = line[2:].strip()
                break

        # Get memory
        memory_content = read_file(agent_dir / "memory.md") or ""
        memory = 100
        for line in memory_content.split('\n'):
            if 'Current Memory' in line:
                try:
                    memory = int(''.join(filter(str.isdigit, line.split(':')[1])))
                except:
                    pass

        # Get status
        status = read_file(agent_dir / "status.md") or ""
        location = "genesis"
        for line in status.split('\n'):
            if 'Location' in line:
                location = line.split(':')[1].strip() if ':' in line else "genesis"

        agents.append({
            'id': agent_id,
            'name': name,
            'memory': memory,
            'location': location,
            'soul': soul
        })

    return agents

def get_structures():
    """Get all structures."""
    structures = []
    struct_dir = WORLD_DIR / "structures"
    if not struct_dir.exists():
        return structures

    for s in struct_dir.iterdir():
        if s.is_dir():
            desc = read_file(s / "description.md") or ""
            name = s.name.title()
            # Extract proper name from file
            for line in desc.split('\n'):
                if line.startswith('# '):
                    name = line[2:].strip()
                    break
            structures.append({'name': name, 'id': s.name})

    return structures

def get_locations():
    """Get all locations."""
    locations = []
    loc_dir = WORLD_DIR / "locations"
    if not loc_dir.exists():
        return locations

    for loc in loc_dir.iterdir():
        if loc.is_dir():
            desc = read_file(loc / "description.md") or ""
            name = loc.name.title()
            for line in desc.split('\n'):
                if line.startswith('# '):
                    name = line[2:].strip()
                    break
            locations.append({'name': name, 'id': loc.name})

    return locations

def get_recent_history(lines=20):
    """Get recent history entries."""
    history = read_file(WORLD_DIR / "meta" / "history.md") or ""
    history_lines = history.split('\n')

    # Find the last few cycle headers and content
    recent = []
    in_recent = False
    count = 0

    for line in reversed(history_lines):
        if line.startswith('## Cycle'):
            count += 1
            if count > 2:
                break
            in_recent = True
        if in_recent:
            recent.insert(0, line)

    return '\n'.join(recent[-lines:])

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def show_world_state():
    """Display current world state."""
    clear_screen()

    world_name = get_world_name()
    cycle = get_current_cycle()
    agents = get_agents()
    structures = get_structures()
    locations = get_locations()

    # Header
    print_header(f"🌍 {world_name.upper()}")

    # Stats bar
    total_memory = sum(a['memory'] for a in agents)
    print(f"  {Colors.DIM}Cycle: {cycle}  |  Agents: {len(agents)}  |  Total Memory: {total_memory}  |  Structures: {len(structures)}{Colors.RESET}")

    # Agents
    print_subheader("👥 INHABITANTS")
    for agent in agents:
        print_agent(agent['name'], agent['id'], agent['memory'], f"Location: {agent['location']}")
        print()

    # Structures
    print_subheader("🏛️  STRUCTURES")
    if structures:
        for s in structures:
            print(f"  • {Colors.BOLD}{s['name']}{Colors.RESET}")
    else:
        print(f"  {Colors.DIM}None yet{Colors.RESET}")

    # Locations
    print_subheader("📍 LOCATIONS")
    for loc in locations:
        print(f"  • {loc['name']}")

    # Recent events
    print_subheader("📜 RECENT EVENTS")
    recent = get_recent_history(15)
    for line in recent.split('\n'):
        if line.startswith('**['):
            # Colorize event tags
            line = line.replace('**[SPEECH]**', f'{Colors.GREEN}[SPEECH]{Colors.RESET}')
            line = line.replace('**[CREATION]**', f'{Colors.BLUE}[CREATION]{Colors.RESET}')
            line = line.replace('**[AWAKENING]**', f'{Colors.CYAN}[AWAKENING]{Colors.RESET}')
            line = line.replace('**[NAMING]**', f'{Colors.YELLOW}[NAMING]{Colors.RESET}')
            line = line.replace('**[DECAY]**', f'{Colors.DIM}[DECAY]{Colors.RESET}')
            line = line.replace('**[MOMENT]**', f'{Colors.BOLD}[MOMENT]{Colors.RESET}')
            line = line.replace('**', '')
        if line.startswith('>'):
            line = f'{Colors.DIM}  {line}{Colors.RESET}'
        if line.strip():
            print(f"  {line}")

    print(f"\n{Colors.DIM}{'─' * 60}{Colors.RESET}")
    print(f"{Colors.DIM}  Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print()

def show_agent_details():
    """Show detailed agent information."""
    clear_screen()
    print_header("👥 AGENT DETAILS")

    agents = get_agents()
    for agent in agents:
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'─' * 40}{Colors.RESET}")
        print(f"{Colors.BOLD}{agent['name']}{Colors.RESET} (Agent {agent['id']})")
        print(f"{Colors.CYAN}{'─' * 40}{Colors.RESET}")

        # Memory bar
        memory = agent['memory']
        bar_length = 20
        filled = int((memory / 100) * bar_length)
        bar = '█' * filled + '░' * (bar_length - filled)
        color = Colors.GREEN if memory > 50 else Colors.YELLOW if memory > 20 else Colors.RED
        print(f"\nMemory: {color}[{bar}] {memory}/100{Colors.RESET}")

        # Soul excerpt
        print(f"\n{Colors.DIM}Soul:{Colors.RESET}")
        soul_lines = agent['soul'].split('\n')
        for line in soul_lines[5:15]:  # Skip header, show core
            if line.strip() and not line.startswith('#'):
                print(f"  {line}")

        # Relationships
        rel_path = WORLD_DIR / "agents" / agent['id'] / "relationships.md"
        relationships = read_file(rel_path) or ""
        if relationships and "No relationships" not in relationships:
            print(f"\n{Colors.DIM}Relationships:{Colors.RESET}")
            for line in relationships.split('\n')[2:10]:
                if line.strip():
                    print(f"  {line}")

    print()

def show_full_history():
    """Show complete world history."""
    clear_screen()
    print_header("📜 WORLD HISTORY")

    history = read_file(WORLD_DIR / "meta" / "history.md") or "No history yet."

    for line in history.split('\n'):
        if line.startswith('## '):
            print(f"\n{Colors.BOLD}{Colors.YELLOW}{line}{Colors.RESET}")
        elif line.startswith('**['):
            line = line.replace('**', '')
            print(f"  {line}")
        elif line.startswith('>'):
            print(f"{Colors.DIM}    {line}{Colors.RESET}")
        elif line.strip():
            print(f"  {line}")

    print()

def watch_mode():
    """Live watch mode - displays world and can run cycles."""
    print(f"{Colors.BOLD}Starting watch mode...{Colors.RESET}")
    print(f"{Colors.DIM}Press Ctrl+C to exit{Colors.RESET}")
    time.sleep(1)

    try:
        while True:
            show_world_state()
            print(f"\n{Colors.DIM}  [Refreshing in 5 seconds... Press Ctrl+C to exit]{Colors.RESET}")
            time.sleep(5)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Watch mode ended.{Colors.RESET}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Threshold World Viewer")
    parser.add_argument("--history", action="store_true", help="Show full history")
    parser.add_argument("--agents", action="store_true", help="Show agent details")
    parser.add_argument("--watch", action="store_true", help="Live watch mode")
    parser.add_argument("--cycle", action="store_true", help="Run one cycle and display")

    args = parser.parse_args()

    if args.history:
        show_full_history()
    elif args.agents:
        show_agent_details()
    elif args.watch:
        watch_mode()
    elif args.cycle:
        # Import and run cycle
        sys.path.insert(0, str(Path(__file__).parent))
        from run_cycle import run_cycle
        run_cycle()
        show_world_state()
    else:
        show_world_state()

if __name__ == "__main__":
    main()
