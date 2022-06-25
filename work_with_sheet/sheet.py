import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from work_with_sheet.dollar import cur_doollar

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Pc1ZpND8yN1R0RgM2mUJBXOGPQBM-HWY4xpmtEU1AuI'
SAMPLE_RANGE_NAME = 'Лист1'


service = build('sheets', 'v4', credentials=credentials)

def sheet_func():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    values[0].insert(3, 'стоимость,Р')
    for value in values[1:]:
        new = cur_doollar * float(value[2])
        value.insert(3, int(new))
    return values