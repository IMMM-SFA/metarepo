#!/usr/bin/env python3
"""
MetaRepo QC Bot - Automated checklist generation for PRs using AI.
"""

import os
import sys
from pathlib import Path

import requests
import yaml

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
PR_NUMBER = os.getenv("PR_NUMBER")
AI_API_KEY = os.getenv("AI_API_KEY")
AI_MODEL_ENDPOINT = os.getenv("AI_MODEL_ENDPOINT") or "https://api.openai.com/v1/chat/completions"
PR_TITLE = os.getenv("PR_TITLE", "")
PR_BODY = os.getenv("PR_BODY", "")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() in {"1", "true", "yes"}
CONFIG_PATH = Path(__file__).parent / "qc_config.yaml"


def load_config():
    """Load bot configuration from qc_config.yaml."""
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_pr_files():
    """Fetch list of files changed in the PR."""
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}/files"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def generate_checklist():
    """Generate QC checklist using AI."""
    if DRY_RUN:
        return get_default_checklist()

    if not AI_API_KEY:
        return get_default_checklist()

    config = load_config()
    ai_cfg = config.get("ai", {})

    files = get_pr_files()
    files_summary = "\n".join([f"- {f['filename']}" for f in files[:5]])

    prompt = f"""You are a QC reviewer for a scientific meta-repository. Generate a brief checklist for this PR:

Title: {PR_TITLE}
Description: {PR_BODY or "(none)"}

Files changed: {files_summary}

Generate a checklist (5-8 items max) in this exact format:
- [ ] Item description

Focus on: releases, tracking IDs, documentation, data references, credentials, file structure.
Include a brief tip for each item if needed."""

    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": ai_cfg.get("model", "gpt-4o-mini"),
        "messages": [{"role": "user", "content": prompt}],
        "temperature": ai_cfg.get("temperature", 0.7),
        "max_tokens": ai_cfg.get("max_tokens", 800),
    }

    try:
        response = requests.post(AI_MODEL_ENDPOINT, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        checklist = response.json()["choices"][0]["message"]["content"]
        return f"## ✅ QC Checklist\n\n{checklist}"
    except Exception as e:
        print(f"Warning: AI API failed ({e}), using default checklist")
        return get_default_checklist()


def load_checklist_items(config):
    """Load checklist items from qc_config.yaml."""
    return config.get("checklist_items", [])


def get_default_checklist():
    """Fallback checklist built from qc_config.yaml."""
    items = load_checklist_items(load_config())
    lines = "\n".join([f"- [ ] {item}" for item in items])
    return f"## ✅ QC Checklist\n\n{lines}"


def post_comment(body):
    """Post comment to PR."""
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{PR_NUMBER}/comments"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    payload = {"body": body}
    response = requests.post(url, headers=headers, json=payload, timeout=15)
    response.raise_for_status()


def main():
    if not DRY_RUN:
        if not all([GITHUB_TOKEN, REPO_OWNER, REPO_NAME, PR_NUMBER]):
            print("Error: Missing required environment variables")
            sys.exit(1)

        if not str(PR_NUMBER).isdigit():
            print(
                "Error: PR_NUMBER must be a real pull request number (example: 12), "
                "not a placeholder like <open_pr_number>."
            )
            sys.exit(1)

    try:
        checklist = generate_checklist()
        comment = f"""## 🤖 IM3 Metarepo Bot

Hey! 👋 Thanks for submitting. Before this PR gets reviewed, please take a moment to go through the checklist below. These are the things we typically catch during QC — better to check now than after review!

{checklist}

---
*This checklist was posted automatically. Tick off each item once done. Reach out to the team if you have questions!*"""
        if DRY_RUN:
            print("🧪 DRY_RUN enabled: not posting to GitHub. Preview below:\n")
            print(comment)
        else:
            post_comment(comment)
            print("✅ QC checklist posted")
    except requests.HTTPError as e:
        status = e.response.status_code if e.response is not None else "unknown"
        if status == 404:
            print(
                "❌ Error: GitHub returned 404. Check that REPO_OWNER/REPO_NAME/PR_NUMBER are correct "
                "and that your token can access this repository."
            )
        else:
            print(f"❌ HTTP Error ({status}): {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

