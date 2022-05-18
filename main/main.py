import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SPREADSHEET_ID = '1DRao1LuElHEfEBry-jsBFzojuTVYOMe_0cxxgkwVcdw'
RANGE_NAME = 'import'

def main():

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print(json.dumps(values, indent=2))

        for row in values:
            print(row)
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()