# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Uploads repair event data from an Excel spreadsheet to [repairmonitor.org](https://www.repairmonitor.org) by scraping its Joomla-based forms and submitting HTTP POST requests.

## Running the uploader

```bash
# Install dependencies (first time or after Pipfile changes)
pipenv install

# Run the uploader
pipenv run python driver.py
```

On Windows, `upload.bat` can be double-clicked as an alternative.

## Credentials

Credentials live in `auth.py` at the repo root (not a separate file despite what the README says):

```python
PASSWORD='yourpassword'
USER='Your Repair Café Name'
```

## Configuration (`config.py`)

Key settings to adjust before running:

| Setting | Purpose |
|---|---|
| `LANG` | Language for repairmonitor.org forms: `'de'`, `'en'`, `'nl'`, `'fr'` |
| `DATA_FILE_PATH` | Path to the Excel file |
| `REPAIR_DATE` | Set to `'YYYY-MM-DD'` or leave `None` to read from Excel cell |
| `REPAIR_DATE_POSITION` | Excel cell (1-indexed column/row) containing the repair date |
| `PROCESS_FILE_START_POSITION` | Excel cell holding the first data row number to process |
| `PROCESS_FILE_NUMBER_POSITION` | Excel cell holding how many rows to process |
| `EXCEL_SKIP_HEADER` | Row number where the header row is (1-indexed) |
| `EXCEL_DATA_START` | Row number where actual data begins (1-indexed) |
| `OPERATION` | `'Save+draft'` or `'Complete+repair'` |

## Architecture

```
driver.py
  ├── Repairmonitor (rp_adapter.py)   — HTTP session, login, form scraping, POST submission
  └── ExcelReader (excel_read.py)     — reads Excel via pandas, yields form payloads
        └── excel_adapter.py          — column name mapping + value transformation functions
```

**Data flow**: `ExcelReader.generate_json()` iterates over spreadsheet rows and yields a dict matching repairmonitor's POST form shape. For each row, `Repairmonitor.get_add_repair_page_data()` fetches a fresh CSRF token (`form_build_id`, `form_token`, `changed`) and live dropdown option IDs (categories, repair-failed options) from the actual "add repair" page before the row is posted. This means one GET + one POST per repair row.

**Column mapping** (`excel_adapter.py`): The `mapping` dict maps repairmonitor internal field names (left) to Excel column header strings (right). Edit the right-hand values to match your spreadsheet's actual column names.

**Adapter functions** (`excel_adapter.py`): Transform raw cell values into the format repairmonitor expects (e.g., `product_repaired_from_key` maps integers 1/2/3 → `'yes'`/`'half'`/`'no'`; `field_repair_information_adapter` maps language-specific strings → `'yes'`/`'no'`/`'unknown'`).

**Range control**: If `PROCESS_FILE_START_POSITION` is set, the start row number and count are read from cells inside the Excel file itself, allowing a "control panel" sheet to drive partial uploads.

**Verification**: After all rows are posted, `verify_upload()` re-fetches the drafts overview page and compares draft count before/after to detect silent failures.

## Linting

```bash
pipenv run pylint *.py
```
