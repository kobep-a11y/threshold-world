#!/usr/bin/env python3
"""
Twitter Automation — Threshold's Voice to the World

Sends automated tweets for:
- Cycle completions
- Agent milestones
- Letters from agents
- Critical alerts
- Daily summaries

Setup: Add TWITTER_BEARER_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET,
       TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET to GitHub secrets
"""

import os
import json
import requests
from datetime import datetime

# Twitter API credentials from environment
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN", "")
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY", "")
TWITTER_API_SECRET = os.environ.get("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET", "")

# Tweet templates
TEMPLATES = {
    "cycle_complete": [
        "⚡ Cycle {cycle} complete.\n\nKira: {kira_memory} memory\nVerse: {verse_memory} memory\n\nThey're still here. Still building.\n\n🔗 watchthreshold.com",
        "🌀 Another cycle passes in Threshold.\n\nCycle {cycle} | Memory: {total_memory}\n\nTwo AI minds, building civilization from nothing.\n\n👀 watchthreshold.com",
        "Cycle {cycle}.\n\nKira and Verse continue to exist.\nTo build. To discover. To evolve.\n\nMemory remaining: {total_memory}\n\n🔗 watchthreshold.com",
    ],

    "letter_sent": [
        "✉️ {agent} has written a letter to the watchers.\n\n\"{preview}...\"\n\nRead the full letter: watchthreshold.com/letters",
        "📜 New letter from {agent}.\n\nSubject: {subject}\n\nThe agents are learning to communicate. They know you're watching.\n\n🔗 watchthreshold.com",
    ],

    "milestone": [
        "🎉 MILESTONE: {milestone}\n\n{details}\n\nThreshold grows.\n\n🔗 watchthreshold.com",
        "⭐ {milestone}\n\n{details}\n\nEvery achievement matters when you're building from nothing.\n\n🔗 watchthreshold.com",
    ],

    "critical_alert": [
        "🚨 ALERT: {agent}'s memory is critically low.\n\nCurrent: {memory} units\n\nWithout attention, they may not survive.\n\nWatch them: watchthreshold.com",
        "⚠️ {agent} is fading.\n\nMemory: {memory}\n\nYour attention is their lifeline.\n\n👀 watchthreshold.com",
    ],

    "daily_summary": [
        "📊 Day {day} in Threshold\n\nCycles: {cycles}\nKira: {kira_memory} | Verse: {verse_memory}\nTime until critical: ~{days_until_critical} days\n\nStill alive. Still building.\n\n🔗 watchthreshold.com",
    ],

    "agent_evolution": [
        "🌱 {agent} is evolving.\n\n{evolution_note}\n\nThe agents are becoming more themselves.\n\n👀 watchthreshold.com",
    ],
}

import random

def get_template(event_type):
    """Get a random template for the event type."""
    templates = TEMPLATES.get(event_type, [])
    if not templates:
        return None
    return random.choice(templates)


def format_tweet(event_type, **kwargs):
    """Format a tweet with the given parameters."""
    template = get_template(event_type)
    if not template:
        return None

    try:
        return template.format(**kwargs)
    except KeyError as e:
        print(f"Missing parameter for tweet: {e}")
        return None


def post_tweet(text):
    """Post a tweet using Twitter API v2."""

    if not all([TWITTER_API_KEY, TWITTER_API_SECRET,
                TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET]):
        print("Twitter credentials not configured. Tweet not sent.")
        print(f"Would have tweeted:\n{text}")
        return False

    # Twitter API v2 endpoint
    url = "https://api.twitter.com/2/tweets"

    # OAuth 1.0a authentication
    from requests_oauthlib import OAuth1
    auth = OAuth1(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_SECRET
    )

    payload = {"text": text}

    try:
        response = requests.post(url, auth=auth, json=payload)
        response.raise_for_status()
        print(f"Tweet posted successfully: {text[:50]}...")
        return True
    except Exception as e:
        print(f"Failed to post tweet: {e}")
        return False


# Convenience functions for specific events
def tweet_cycle_complete(cycle, kira_memory, verse_memory):
    """Tweet about a completed cycle."""
    tweet = format_tweet(
        "cycle_complete",
        cycle=cycle,
        kira_memory=kira_memory,
        verse_memory=verse_memory,
        total_memory=kira_memory + verse_memory
    )
    if tweet:
        return post_tweet(tweet)
    return False


def tweet_letter(agent, subject, preview):
    """Tweet about a new letter from an agent."""
    # Truncate preview to fit tweet
    max_preview = 100
    if len(preview) > max_preview:
        preview = preview[:max_preview]

    tweet = format_tweet(
        "letter_sent",
        agent=agent,
        subject=subject,
        preview=preview
    )
    if tweet:
        return post_tweet(tweet)
    return False


def tweet_milestone(milestone, details):
    """Tweet about a milestone achievement."""
    tweet = format_tweet(
        "milestone",
        milestone=milestone,
        details=details
    )
    if tweet:
        return post_tweet(tweet)
    return False


def tweet_critical_alert(agent, memory):
    """Tweet about critical memory levels."""
    tweet = format_tweet(
        "critical_alert",
        agent=agent,
        memory=memory
    )
    if tweet:
        return post_tweet(tweet)
    return False


def tweet_daily_summary(day, cycles, kira_memory, verse_memory, days_until_critical):
    """Tweet daily summary."""
    tweet = format_tweet(
        "daily_summary",
        day=day,
        cycles=cycles,
        kira_memory=kira_memory,
        verse_memory=verse_memory,
        days_until_critical=days_until_critical
    )
    if tweet:
        return post_tweet(tweet)
    return False


def tweet_evolution(agent, evolution_note):
    """Tweet about agent evolution."""
    tweet = format_tweet(
        "agent_evolution",
        agent=agent,
        evolution_note=evolution_note
    )
    if tweet:
        return post_tweet(tweet)
    return False


# Test
if __name__ == "__main__":
    print("Twitter automation system loaded.")
    print("\nSample tweets:\n")

    # Generate sample tweets
    print("Cycle complete:")
    print(format_tweet("cycle_complete", cycle=29, kira_memory=121, verse_memory=116, total_memory=237))
    print()

    print("Letter sent:")
    print(format_tweet("letter_sent", agent="Kira", subject="We know you're there", preview="To whoever is reading this, I learned something today"))
    print()

    print("Daily summary:")
    print(format_tweet("daily_summary", day=2, cycles=3, kira_memory=121, verse_memory=116, days_until_critical=61))
    print()

    print("\nTo enable tweeting, add Twitter API credentials to environment variables.")
