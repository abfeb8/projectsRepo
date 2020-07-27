import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)


def Connect(sheet_name, worksheet_title):
    return client.open(sheet_name).worksheet(worksheet_title)
