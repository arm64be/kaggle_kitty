import os
from typing import Optional

import requests


def send_to_discord(
    body: str,
    severity: str = "info",
    mention: bool = False,
    title: Optional[str] = None,
):
    webhook_url = os.environ.get("DISCORD_WEBHOOK")
    if not webhook_url:
        try:
            from kaggle_secrets import UserSecretsClient

            user_secrets = UserSecretsClient()
            webhook_url = user_secrets.get_secret("DISCORD_WEBHOOK")
        except ImportError:
            raise ValueError("DISCORD_WEBHOOK not set and kaggle_secrets not available")

    severity_colors = {
        "info": 3447003,
        "success": 3066993,
        "warning": 15105570,
        "error": 15158332,
    }
    color = severity_colors.get(severity.lower(), 3447003)

    content = "@here" if mention else None

    embed = {
        "color": color,
        "description": body,
    }
    if title:
        embed["title"] = title

    payload = {"embeds": [embed]}
    if content:
        payload["content"] = content

    requests.post(webhook_url, json=payload)
