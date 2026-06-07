#!/usr/bin/env python3
"""Append TrendPilot AI source-log rows to Google Sheets.

Requires optional dependencies from requirements-integrations.txt and a service
account JSON file configured through GOOGLE_APPLICATION_CREDENTIALS.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from trendpilot.fields import SOURCE_LOG_FIELDS
from trendpilot.records import read_source_log, validate_source_log_records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append source-log CSV rows to Google Sheets.")
    parser.add_argument("--spreadsheet-id", required=True)
    parser.add_argument("--worksheet", default="SourceLog")
    parser.add_argument("--input", required=True, help="Path to source-log CSV")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        raise SystemExit("GOOGLE_APPLICATION_CREDENTIALS must point to a service account JSON file.")

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SystemExit("Install optional dependencies first: python -m pip install -r requirements-integrations.txt") from exc

    records = read_source_log(Path(args.input))
    errors = validate_source_log_records(records)
    if errors:
        raise SystemExit("Validation failed:\n" + "\n".join(f"- {error}" for error in errors))

    credentials = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    service = build("sheets", "v4", credentials=credentials)
    values = [[record.get(field, "") for field in SOURCE_LOG_FIELDS] for record in records]

    service.spreadsheets().values().append(
        spreadsheetId=args.spreadsheet_id,
        range=f"{args.worksheet}!A1",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": values},
    ).execute()

    print(f"Appended {len(values)} row(s) to {args.worksheet}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
