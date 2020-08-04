import pandas as pd
import webbrowser as wb
import pyautogui as pag
import subprocess
from time import sleep


class work:
    def __init__(self,id1,name1,url1):
        self.gsheetID = id1
        self.sheetName = name1
        self.sheet_url = url1.format(self.gsheetID, self.sheetName)
        self.len = self.length_of_sheet()
        self.data = self.read_sheet()
        self.go_into_meeting()

    def sendmessage(self,message):   
        subprocess.Popen(['notify-send', message])
        self.move_curser()
        self.move_curser()

    def move_curser(self):
        x,y = pag.position()
        pag.moveTo(x-12, y+12)

    def timer(self):
        self.sendmessage("The link would open shortly")
        sleep(0.3)

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

    def screen_resolution(self):
        return pag.size()

    def open_meet(self):
        print("Your screen resolution is ",self.screen_resolution())
        wb.open_new_tab(self.fetch_url())

    def locate(self,image,confidence):
        return pag.locateCenterOnScreen(image,confidence=confidence)

    def locate_join(self):
        print("Start locating")
        self.timer()
        self.move_curser()
        loc = None
        i = 0
        while(loc==None and i<20):
            loc = self.locate('./images/join.png',0.8)
            if loc==None:
                loc = self.locate('./images/ask_to_join.png',0.8)
            if loc==None:
                loc = self.locate('./images/join_now.png',0.8)
            sleep(1)
            i+=1
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
    
