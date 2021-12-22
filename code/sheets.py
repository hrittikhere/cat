# This code fetches data from RSS Store on Google Sheet


from googleapiclient.discovery import build
from google.oauth2 import service_account



SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


CREDS = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = ''
SPREADSHEET_RANGE = 'feed!A1:G2561'
service = build('sheets', 'v4', credentials=CREDS)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=SPREADSHEET_RANGE).execute()
#values = result.get('values', [])

print(result)
