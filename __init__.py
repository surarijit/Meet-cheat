import os
from cheatmeet import work

gsheetID = "1eF5vxI7qL7MHKpWIinks4eK3X1KQ6IwDzepgBnOqifU"
sheetName = "Sheet1"
sheet_url ="https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}"

depends = [ "pyautogui",
            "webbrowser"
            "pandas",
]
def installs():
    for i in depends:
        os.system("pip3 install "+ i)


if __name__ == "__main__":
    installs()
    work(gsheetID,sheetName,sheet_url)