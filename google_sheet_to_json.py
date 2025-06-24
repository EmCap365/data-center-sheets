import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets settings
SHEET_ID = os.environ.get("SHEET_ID")  # Your spreadsheet ID
SHEET_NAME = os.environ.get("SHEET_NAME") or "Sheet1"

# Auth using credentials passed via GitHub Secret
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(os.environ['GSHEET_CREDS'])  # Loaded from GitHub Secret
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Load Sheet
doc = client.open_by_key(SHEET_ID)
sheet = doc.worksheet(SHEET_NAME)
data = sheet.get_all_records()

# Output JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Exported {len(data)} rows to data.json")
