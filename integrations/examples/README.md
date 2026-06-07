# Integration Code Examples

These examples show how to connect TrendPilot AI records to external services.

They are intentionally optional and require your own API keys or service account credentials.
No keys are included in this repository.

## Firecrawl URL fetch example

```bash
export FIRECRAWL_API_KEY="fc-YOUR_KEY"
python integrations/examples/firecrawl_fetch.py \
  --url https://example.com \
  --output data/firecrawl-example.json
```

This calls Firecrawl's API and saves the response JSON locally.

## Google Sheets append example

Install optional dependencies:

```bash
python -m pip install -r requirements-integrations.txt
```

Then run:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
python integrations/examples/google_sheets_append.py \
  --spreadsheet-id YOUR_SHEET_ID \
  --worksheet SourceLog \
  --input examples/sample-source-log.csv
```

The Google Sheets script appends source-log rows to an existing sheet. It does not create campaigns, send messages, or collect private data.
