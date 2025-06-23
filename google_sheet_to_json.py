import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets settings
SHEET_ID = os.environ.get("SHEET_ID")  # e.g., '1Ybm5OiBXGlo8gOOcfJzAxHddytnRJH5LrCnkaew1eq4'
SHEET_NAME = os.environ.get("SHEET_NAME") or "Sheet1"

# Auth
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_path = "creds.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
client = gspread.authorize(creds)

# Load Sheet
doc = client.open_by_key(SHEET_ID)
sheet = doc.worksheet(SHEET_NAME)
data = sheet.get_all_records()

# Output JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Exported {len(data)} rows to data.json")
