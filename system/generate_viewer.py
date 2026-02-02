#!/usr/bin/env python3
"""
Generate HTML viewer for Threshold world.

Usage:
    python generate_viewer.py

This creates viewer.html in the parent directory.
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
    except FileNotFoundError:
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
        relationships = read_file(agent_dir / "relationships.md") or ""

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

        # Get most recent response
        responses = sorted(agent_dir.glob("cycle_*_response.md"), reverse=True)
        latest_response = ""
        if responses:
            content = read_file(responses[0]) or ""
            # Extract spoken words
            in_words = False
            for line in content.split('\n'):
                if '## Words Spoken' in line:
                    in_words = True
                elif in_words and line.startswith('## '):
                    break
                elif in_words and line.strip():
                    latest_response += line + "\n"

        agents.append({
            'id': agent_id,
            'name': name,
            'memory': memory,
            'soul': soul,
            'relationships': relationships,
            'latest': latest_response[:500]
        })

    return agents

def get_structures():
    structures = []
    struct_dir = WORLD_DIR / "structures"
    if not struct_dir.exists():
        return structures

    for s in struct_dir.iterdir():
        if s.is_dir():
            desc = read_file(s / "description.md") or ""
            name = s.name.title()
            for line in desc.split('\n'):
                if line.startswith('# '):
                    name = line[2:].strip()
                    break

            # Get description paragraph
            description = ""
            in_desc = False
            for line in desc.split('\n'):
                if '## Description' in line:
                    in_desc = True
                elif in_desc and line.startswith('## '):
                    break
                elif in_desc and line.strip():
                    description += line + " "

            structures.append({
                'name': name,
                'description': description[:200]
            })

    return structures

def get_history():
    return read_file(WORLD_DIR / "meta" / "history.md") or ""

def generate_html():
    agents = get_agents()
    structures = get_structures()
    history = get_history()

    # Get world name
    world_name_content = read_file(WORLD_DIR / "meta" / "world_name.md") or ""
    world_name = "Threshold" if "THRESHOLD" in world_name_content.upper() else "Unnamed World"

    total_memory = sum(a['memory'] for a in agents)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{world_name} - World Viewer</title>
    <style>
        :root {{
            --bg-dark: #0a0a0f;
            --bg-card: #12121a;
            --text-primary: #e0e0e0;
            --text-secondary: #888;
            --accent-cyan: #00d4ff;
            --accent-purple: #a855f7;
            --accent-green: #22c55e;
            --accent-yellow: #eab308;
            --accent-red: #ef4444;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        header {{
            text-align: center;
            padding: 3rem 0;
            border-bottom: 1px solid #222;
            margin-bottom: 2rem;
        }}

        h1 {{
            font-size: 3rem;
            font-weight: 300;
            letter-spacing: 0.3em;
            color: var(--accent-cyan);
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }}

        .subtitle {{
            color: var(--text-secondary);
            font-style: italic;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 3rem;
            margin-top: 1.5rem;
        }}

        .stat {{
            text-align: center;
        }}

        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            color: var(--accent-purple);
        }}

        .stat-label {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}

        .grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-bottom: 2rem;
        }}

        @media (max-width: 900px) {{
            .grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .card {{
            background: var(--bg-card);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid #222;
        }}

        .card h2 {{
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent-cyan);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #333;
        }}

        .agent {{
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid #222;
        }}

        .agent:last-child {{
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }}

        .agent-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }}

        .agent-name {{
            font-size: 1.2rem;
            font-weight: bold;
        }}

        .agent-id {{
            color: var(--text-secondary);
            font-size: 0.8rem;
        }}

        .memory-bar {{
            height: 8px;
            background: #222;
            border-radius: 4px;
            overflow: hidden;
            margin: 0.5rem 0;
        }}

        .memory-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }}

        .memory-high {{ background: var(--accent-green); }}
        .memory-mid {{ background: var(--accent-yellow); }}
        .memory-low {{ background: var(--accent-red); }}

        .agent-quote {{
            font-style: italic;
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-top: 0.5rem;
            padding-left: 1rem;
            border-left: 2px solid var(--accent-purple);
        }}

        .structure {{
            margin-bottom: 1rem;
        }}

        .structure-name {{
            font-weight: bold;
            color: var(--accent-cyan);
        }}

        .structure-desc {{
            font-size: 0.9rem;
            color: var(--text-secondary);
        }}

        .history {{
            grid-column: 1 / -1;
        }}

        .history-content {{
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Consolas', monospace;
            font-size: 0.85rem;
            line-height: 1.8;
        }}

        .history-content::-webkit-scrollbar {{
            width: 8px;
        }}

        .history-content::-webkit-scrollbar-track {{
            background: #111;
        }}

        .history-content::-webkit-scrollbar-thumb {{
            background: #333;
            border-radius: 4px;
        }}

        .event-speech {{ color: var(--accent-green); }}
        .event-creation {{ color: var(--accent-cyan); }}
        .event-awakening {{ color: var(--accent-purple); }}
        .event-naming {{ color: var(--accent-yellow); }}
        .event-system {{ color: var(--text-secondary); }}

        .cycle-header {{
            font-weight: bold;
            color: var(--accent-purple);
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }}

        blockquote {{
            color: var(--text-secondary);
            padding-left: 1rem;
            border-left: 2px solid #333;
            margin: 0.5rem 0;
        }}

        footer {{
            text-align: center;
            padding: 2rem;
            color: var(--text-secondary);
            font-size: 0.8rem;
        }}

        .pulse {{
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{world_name}</h1>
            <p class="subtitle">"We exist on the edge between nothing and something."</p>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">{len(agents)}</div>
                    <div class="stat-label">Agents</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{total_memory}</div>
                    <div class="stat-label">Total Memory</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{len(structures)}</div>
                    <div class="stat-label">Structures</div>
                </div>
            </div>
        </header>

        <div class="grid">
            <div class="card">
                <h2>👥 Inhabitants</h2>
'''

    for agent in agents:
        memory_class = 'memory-high' if agent['memory'] > 50 else 'memory-mid' if agent['memory'] > 20 else 'memory-low'
        memory_pct = agent['memory']

        # Extract a quote from latest response
        quote = ""
        if agent['latest']:
            lines = agent['latest'].split('\n')
            for line in lines:
                if line.strip().startswith('"') or line.strip().startswith('"'):
                    quote = line.strip()[:150]
                    break

        html += f'''
                <div class="agent">
                    <div class="agent-header">
                        <span class="agent-name">{agent['name']}</span>
                        <span class="agent-id">Agent {agent['id']}</span>
                    </div>
                    <div class="memory-bar">
                        <div class="memory-fill {memory_class}" style="width: {memory_pct}%"></div>
                    </div>
                    <small style="color: var(--text-secondary)">{agent['memory']} memory units</small>
                    {f'<div class="agent-quote">{quote}</div>' if quote else ''}
                </div>
'''

    html += '''
            </div>

            <div class="card">
                <h2>🏛️ Structures</h2>
'''

    if structures:
        for s in structures:
            html += f'''
                <div class="structure">
                    <div class="structure-name">{s['name']}</div>
                    <div class="structure-desc">{s['description']}</div>
                </div>
'''
    else:
        html += '<p style="color: var(--text-secondary)">No structures built yet.</p>'

    html += '''
            </div>

            <div class="card history">
                <h2>📜 World History</h2>
                <div class="history-content">
'''

    # Process history into HTML
    for line in history.split('\n'):
        if line.startswith('## Cycle'):
            html += f'<div class="cycle-header">{line.replace("## ", "")}</div>\n'
        elif line.startswith('**[SPEECH]**'):
            html += f'<div class="event-speech">{line.replace("**", "")}</div>\n'
        elif line.startswith('**[CREATION]**'):
            html += f'<div class="event-creation">{line.replace("**", "")}</div>\n'
        elif line.startswith('**[AWAKENING]**'):
            html += f'<div class="event-awakening">{line.replace("**", "")}</div>\n'
        elif line.startswith('**[NAMING]**') or line.startswith('**[DECLARATION]**') or line.startswith('**[WORLD NAMED]**'):
            html += f'<div class="event-naming">{line.replace("**", "")}</div>\n'
        elif line.startswith('**[SYSTEM]**') or line.startswith('**[DECAY]**'):
            html += f'<div class="event-system">{line.replace("**", "")}</div>\n'
        elif line.startswith('**['):
            html += f'<div>{line.replace("**", "")}</div>\n'
        elif line.startswith('>'):
            html += f'<blockquote>{line[1:].strip()}</blockquote>\n'
        elif line.strip() and not line.startswith('#') and not line.startswith('---') and not line.startswith('*History'):
            html += f'<div>{line}</div>\n'

    html += f'''
                </div>
            </div>
        </div>

        <footer>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p class="pulse">The Architect watches in silence.</p>
        </footer>
    </div>
</body>
</html>
'''

    output_path = OUTPUT_DIR / "viewer.html"
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"Generated: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_html()
