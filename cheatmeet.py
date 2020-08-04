import pandas as pd
import webbrowser as wb
import pyautogui as pag
from time import sleep
import cv2

class work:
    def __init__(self):
        #self.timer()
        self.gsheetID = "1eF5vxI7qL7MHKpWIinks4eK3X1KQ6IwDzepgBnOqifU"
        self.sheetName = "Sheet1"
        self.sheet_url ="https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(self.gsheetID, self.sheetName)
        self.len = self.length_of_sheet()
        self.data = self.read_sheet()
        self.go_into_meeting()

    def timer(self):
        print("The program begins in")
        for i in range(4):
            print(4-i)
            sleep(1)

    def read_sheet(self):
        df = pd.read_csv(self.sheet_url)
        return df

    def length_of_sheet(self):
        df=self.read_sheet()
        l=len(df["Meeting Link"])
        return l

    def fetch_url(self):
        df = self.read_sheet()
        l=len(df["Meeting Link"])
        url = df['Meeting Link'][l-1]
        return url

    def open_meet(self):
        print("Your screen resolution is")
        print(pag.size())
        wb.open_new_tab(self.fetch_url())

    def locate(self,image,confidence):
        return pag.locateCenterOnScreen(image,confidence=confidence)

    def locate_join(self):
        print("Start locating")
        sleep(10)
        loc = self.locate('./images/join.png',0.8)
        if loc==None:
            loc = self.locate('./images/ask_to_join.png',0.8)
        if loc==None:
            loc = self.locate('./images/join_now.png',0.8)
        return loc
    
    def enter_meeting(self):
        loc = self.locate_join()
        pag.moveTo(loc)
        sleep(1.3)
        pag.click(loc)
        print(loc)

    def go_into_meeting(self):
        self.open_meet()
        self.enter_meeting()