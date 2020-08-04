#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import pprint


# In[4]:


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ABC1.json', scope)
client = gspread.authorize(creds)

sheet = client.open('meet_cheat').sheet1

data = sheet.get_all_records()

l=1+len(data)
print(l)


# In[6]:


url = sheet.cell(l, 1).value
print(url)

