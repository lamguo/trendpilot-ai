#!/usr/bin/env python3
"""Minimal Firecrawl API example.

This script demonstrates a real API call shape without embedding any API key.
It requires FIRECRAWL_API_KEY in the environment.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch a public URL with Firecrawl and save the JSON response.")
    parser.add_argument("--url", required=True, help="Public URL to fetch")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--api-url", default="https://api.firecrawl.dev/v1/scrape")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        raise SystemExit("FIRECRAWL_API_KEY is required. Do not hard-code keys in source files.")

    payload = json.dumps({"url": args.url, "formats": ["markdown"]}).encode("utf-8")
    request = urllib.request.Request(
        args.api_url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Firecrawl request failed: HTTP {exc.code}\n{detail}") from exc

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Saved Firecrawl response to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
