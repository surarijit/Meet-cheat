#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[24]:


gsheetID = "1eF5vxI7qL7MHKpWIinks4eK3X1KQ6IwDzepgBnOqifU"
sheetName = "Sheet1"

sheet_url ="https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(gsheetID, sheetName)

df=pd.read_csv(sheet_url)

l=len(df["Meeting Link"])
url = df['Meeting Link'][l-1]
print(url)

