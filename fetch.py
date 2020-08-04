
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ABC1.json', scope)
client = gspread.authorize(creds)

sheet = client.open('meet_cheat').sheet1

data = sheet.get_all_records()

#print(type(data))

url = sheet.cell(2, 1).value
#print(type(url))

print(url)