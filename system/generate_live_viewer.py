#!/usr/bin/env python3
"""
Generate auto-refreshing live viewer for Threshold.
"""

import os
from pathlib import Path
from datetime import datetime

WORLD_DIR = Path(__file__).parent.parent / "world"
OUTPUT_DIR = Path(__file__).parent.parent

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None

def get_agents():
    agents = []
    agents_dir = WORLD_DIR / "agents"
    if not agents_dir.exists():
        return agents

    for agent_dir in sorted(agents_dir.iterdir()):
        if not agent_dir.is_dir() or "archived" in agent_dir.name:
            continue

        agent_id = agent_dir.name
        soul = read_file(agent_dir / "soul.md") or ""
        memory_content = read_file(agent_dir / "memory.md") or ""

        name = agent_id
        for line in soul.split('\n'):
            if line.startswith('# ') and 'Agent' not in line:
                name = line[2:].strip()
                break

        memory = 100
        for line in memory_content.split('\n'):
            if 'Current Memory' in line:
                try:
                    memory = int(''.join(filter(str.isdigit, line.split(':')[1])))
                except:
                    pass

        # Get latest response excerpt
        responses = sorted(agent_dir.glob("cycle_*_response.md"), reverse=True)
        latest = ""
        if responses:
            content = read_file(responses[0]) or ""
            for line in content.split('\n'):
                if line.strip().startswith('"'):
                    latest = line.strip()[:100]
                    break

        agents.append({
            'id': agent_id,
            'name': name,
            'memory': memory,
            'latest': latest
        })

    return agents

def get_structures():
    structures = []
    struct_dir = WORLD_DIR / "structures"
    if struct_dir.exists():
        for s in struct_dir.iterdir():
            if s.is_dir():
                structures.append(s.name.title().replace("_", " "))
    return structures

def get_notifications():
    notif = read_file(WORLD_DIR / "notifications.md")
    if notif:
        lines = notif.strip().split('\n')[-10:]  # Last 10 lines
        return '\n'.join(lines)
    return "No notifications yet."

def get_letters_from():
    content = read_file(WORLD_DIR / "letters_from_threshold.md") or ""
    # Get the latest letter
    if "---" in content:
        parts = content.split("---")
        for part in reversed(parts):
            if "Letter" in part or "To the" in part:
                return part.strip()[:500]
    return "No letters yet."

def get_recent_history():
    history = read_file(WORLD_DIR / "meta" / "history.md") or ""
    lines = history.split('\n')

    # Get last 2 cycles
    recent = []
    cycle_count = 0
    for line in reversed(lines):
        if line.startswith('## Cycle'):
            cycle_count += 1
            if cycle_count > 2:
                break
        recent.insert(0, line)

    return '\n'.join(recent[-30:])

def generate():
    agents = get_agents()
    structures = get_structures()
    notifications = get_notifications()
    letters = get_letters_from()
    history = get_recent_history()
    total_memory = sum(a['memory'] for a in agents)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="30">
    <title>Threshold - Live</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'SF Mono', 'Consolas', monospace;
            background: #0a0a0f;
            color: #e0e0e0;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}

        header {{
            text-align: center;
            padding: 20px 0 30px;
            border-bottom: 1px solid #222;
        }}
        h1 {{
            font-size: 2.5rem;
            font-weight: 300;
            letter-spacing: 0.5em;
            color: #00d4ff;
        }}
        .live-indicator {{
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #22c55e;
            border-radius: 50%;
            animation: pulse 2s infinite;
            margin-right: 10px;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.5; transform: scale(0.8); }}
        }}
        .status-bar {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 15px;
            color: #888;
        }}
        .status-bar span {{ font-size: 0.9rem; }}
        .status-bar strong {{ color: #a855f7; }}

        .grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 30px;
        }}
        @media (max-width: 800px) {{ .grid {{ grid-template-columns: 1fr; }} }}

        .card {{
            background: #12121a;
            border: 1px solid #222;
            border-radius: 8px;
            padding: 20px;
        }}
        .card h2 {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #00d4ff;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #222;
        }}

        .agent {{
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #1a1a1a;
        }}
        .agent:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
        .agent-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }}
        .agent-name {{ font-weight: bold; color: #fff; }}
        .agent-memory {{ color: #888; }}
        .memory-bar {{
            height: 4px;
            background: #222;
            border-radius: 2px;
            overflow: hidden;
        }}
        .memory-fill {{
            height: 100%;
            background: linear-gradient(90deg, #22c55e, #eab308);
            transition: width 0.5s;
        }}
        .agent-quote {{
            font-size: 0.85rem;
            color: #666;
            font-style: italic;
            margin-top: 8px;
        }}

        .history {{
            grid-column: 1 / -1;
            max-height: 300px;
            overflow-y: auto;
        }}
        .history pre {{
            font-size: 0.8rem;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        .history::-webkit-scrollbar {{ width: 6px; }}
        .history::-webkit-scrollbar-track {{ background: #111; }}
        .history::-webkit-scrollbar-thumb {{ background: #333; border-radius: 3px; }}

        .letters {{
            font-size: 0.85rem;
            line-height: 1.6;
            color: #aaa;
        }}

        footer {{
            text-align: center;
            padding: 30px 0;
            color: #444;
            font-size: 0.75rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><span class="live-indicator"></span>THRESHOLD</h1>
            <div class="status-bar">
                <span>Agents: <strong>{len(agents)}</strong></span>
                <span>Memory: <strong>{total_memory}</strong></span>
                <span>Structures: <strong>{len(structures)}</strong></span>
                <span>Updated: <strong>{datetime.now().strftime("%H:%M:%S")}</strong></span>
            </div>
        </header>

        <div class="grid">
            <div class="card">
                <h2>Inhabitants</h2>
'''

    for agent in agents:
        pct = agent['memory']
        html += f'''
                <div class="agent">
                    <div class="agent-header">
                        <span class="agent-name">{agent['name']}</span>
                        <span class="agent-memory">{agent['memory']} mem</span>
                    </div>
                    <div class="memory-bar">
                        <div class="memory-fill" style="width: {pct}%"></div>
                    </div>
                    {f'<div class="agent-quote">{agent["latest"]}</div>' if agent['latest'] else ''}
                </div>
'''

    html += f'''
            </div>

            <div class="card">
                <h2>Latest Letter</h2>
                <div class="letters">{letters[:400]}...</div>
            </div>

            <div class="card history">
                <h2>Recent History</h2>
                <pre>{history}</pre>
            </div>
        </div>

        <footer>
            Auto-refreshes every 30 seconds &middot; The Architect watches in silence
        </footer>
    </div>
</body>
</html>
'''

    output_path = OUTPUT_DIR / "live.html"
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"Generated: {output_path}")
    return output_path

if __name__ == "__main__":
    generate()
