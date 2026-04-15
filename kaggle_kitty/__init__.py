import os

_initialized = False


def _init_hf_token():
    global _initialized
    if _initialized:
        return
    _initialized = True

    if os.environ.get("HF_TOKEN") is None:
        try:
            from kaggle_secrets import UserSecretsClient

            user_secrets = UserSecretsClient()
            os.environ["HF_TOKEN"] = user_secrets.get_secret("HF_TOKEN")
        except Exception:
            pass


_init_hf_token()

from kaggle_kitty.discord import send_to_discord

__all__ = ["send_to_discord"]
