import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets settings
SHEET_ID = os.environ.get("SHEET_ID")  # From GitHub Actions env
SHEET_NAME = os.environ.get("SHEET_NAME") or "Sheet1"

# Auth via local creds.json file (written by GitHub Actions)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Load Sheet
doc = client.open_by_key(SHEET_ID)
sheet = doc.worksheet(SHEET_NAME)
data = sheet.get_all_records()

# Output JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Exported {len(data)} rows to data.json")
