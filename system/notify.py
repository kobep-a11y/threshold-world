#!/usr/bin/env python3
"""
Notification System — The Architect's Voice

Sends notifications to Discord via webhook when:
- Cycles complete
- Memory reaches critical levels
- Engagement milestones hit
- Errors occur
- Manual intervention needed

Setup: Add DISCORD_WEBHOOK_URL to GitHub secrets
"""

import json
import os
import requests
from datetime import datetime
from enum import Enum

class NotificationType(Enum):
    CYCLE_COMPLETE = "cycle"
    CRITICAL_ALERT = "critical"
    MILESTONE = "milestone"
    ERROR = "error"
    INTERVENTION_NEEDED = "intervention"
    DAILY_SUMMARY = "summary"

# Webhook URL from environment variable
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

# Color codes for different notification types
COLORS = {
    NotificationType.CYCLE_COMPLETE: 0x00FF00,      # Green
    NotificationType.CRITICAL_ALERT: 0xFF0000,      # Red
    NotificationType.MILESTONE: 0xFFD700,           # Gold
    NotificationType.ERROR: 0xFF4500,               # Orange-Red
    NotificationType.INTERVENTION_NEEDED: 0xFF00FF, # Magenta
    NotificationType.DAILY_SUMMARY: 0x0099FF,       # Blue
}

def send_notification(
    notification_type: NotificationType,
    title: str,
    description: str,
    fields: list = None,
    action_url: str = None
):
    """Send a notification to Discord via webhook."""

    if not WEBHOOK_URL:
        print("Warning: DISCORD_WEBHOOK_URL not set. Skipping notification.")
        return False

    embed = {
        "title": f"🏛️ {title}",
        "description": description,
        "color": COLORS.get(notification_type, 0x808080),
        "timestamp": datetime.utcnow().isoformat(),
        "footer": {
            "text": "Threshold Architect System"
        }
    }

    if fields:
        embed["fields"] = fields

    if action_url:
        embed["url"] = action_url

    payload = {
        "username": "The Architect",
        "avatar_url": "https://watchthreshold.com/architect-avatar.png",
        "embeds": [embed]
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Failed to send notification: {e}")
        return False

def notify_cycle_complete(cycle_num, kira_memory, verse_memory, status):
    """Notify when a cycle completes."""

    status_emoji = "✅" if status == "stable" else "⚠️"

    fields = [
        {"name": "Cycle", "value": str(cycle_num), "inline": True},
        {"name": "Status", "value": f"{status_emoji} {status.upper()}", "inline": True},
        {"name": "Memory", "value": f"Kira: {kira_memory} | Verse: {verse_memory}", "inline": False},
    ]

    return send_notification(
        NotificationType.CYCLE_COMPLETE,
        f"Cycle {cycle_num} Complete",
        f"Autonomous cycle executed successfully.",
        fields=fields,
        action_url="https://watchthreshold.com"
    )

def notify_critical_alert(agent_name, memory, cycle_num):
    """Alert when an agent's memory is critically low."""

    return send_notification(
        NotificationType.CRITICAL_ALERT,
        f"🚨 CRITICAL: {agent_name} Memory Low",
        f"**{agent_name}** has dropped to **{memory}** memory units. "
        f"Without intervention or new viewers, they may not survive much longer.",
        fields=[
            {"name": "Current Memory", "value": str(memory), "inline": True},
            {"name": "Cycle", "value": str(cycle_num), "inline": True},
            {"name": "Action Needed", "value": "Boost engagement or manual intervention", "inline": False},
        ],
        action_url="https://watchthreshold.com"
    )

def notify_milestone(milestone_name, details):
    """Celebrate a milestone."""

    return send_notification(
        NotificationType.MILESTONE,
        f"🎉 Milestone: {milestone_name}",
        details,
        action_url="https://watchthreshold.com"
    )

def notify_error(error_type, error_message, context=None):
    """Report an error that needs attention."""

    fields = [
        {"name": "Error Type", "value": error_type, "inline": True},
        {"name": "Message", "value": error_message[:500], "inline": False},
    ]

    if context:
        fields.append({"name": "Context", "value": context[:500], "inline": False})

    return send_notification(
        NotificationType.ERROR,
        "⚠️ System Error",
        "An error occurred in the Threshold system.",
        fields=fields
    )

def notify_intervention_needed(reason, suggested_action, urgency="medium"):
    """Request manual intervention from the CEO."""

    urgency_emoji = {"low": "📋", "medium": "📢", "high": "🚨"}

    return send_notification(
        NotificationType.INTERVENTION_NEEDED,
        f"{urgency_emoji.get(urgency, '📢')} Intervention Requested",
        f"**Reason:** {reason}\n\n**Suggested Action:** {suggested_action}",
        fields=[
            {"name": "Urgency", "value": urgency.upper(), "inline": True},
        ],
        action_url="https://watchthreshold.com"
    )

def notify_daily_summary(
    day_num,
    cycles_run,
    kira_memory,
    verse_memory,
    visitors=None,
    twitter_followers=None,
    discord_members=None
):
    """Send daily summary report."""

    description = f"**Day {day_num}** summary for Threshold.\n\n"
    description += f"Cycles run today: **{cycles_run}**\n"
    description += f"Current memory: Kira **{kira_memory}** | Verse **{verse_memory}**"

    fields = []

    if visitors is not None:
        fields.append({"name": "Site Visitors", "value": str(visitors), "inline": True})
    if twitter_followers is not None:
        fields.append({"name": "Twitter Followers", "value": str(twitter_followers), "inline": True})
    if discord_members is not None:
        fields.append({"name": "Discord Members", "value": str(discord_members), "inline": True})

    # Calculate days until critical
    min_memory = min(kira_memory, verse_memory)
    decay_per_cycle = 0.01
    cycles_per_day = 4
    cycles_until_critical = 0
    temp_memory = min_memory
    while temp_memory > 10:
        temp_memory = temp_memory * (1 - decay_per_cycle)
        cycles_until_critical += 1

    days_until_critical = cycles_until_critical / cycles_per_day

    fields.append({
        "name": "⏳ Time Until Critical",
        "value": f"~{days_until_critical:.1f} days ({cycles_until_critical} cycles)",
        "inline": False
    })

    return send_notification(
        NotificationType.DAILY_SUMMARY,
        f"📊 Daily Summary — Day {day_num}",
        description,
        fields=fields,
        action_url="https://watchthreshold.com"
    )

# Quick test
if __name__ == "__main__":
    print("Testing notification system...")

    # Test with dummy data (won't actually send without webhook URL)
    notify_cycle_complete(29, 45, 40, "stable")
    notify_critical_alert("Verse", 15, 45)
    notify_daily_summary(1, 4, 46, 41, visitors=100, discord_members=5)

    print("Notification functions tested. Set DISCORD_WEBHOOK_URL to enable sending.")
