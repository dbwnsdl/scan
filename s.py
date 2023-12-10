from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import tkinter as tk

def run(text):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    dv = dv = webdriver.Chrome(options=chrome_options)
    dv.get("https://www.naver.com")

    elem = dv.find_element("name", "query")
    elem.send_keys("맞춤법 검사기")
    elem.send_keys(Keys.RETURN)

    sleep(0.5)

    elem = dv.find_element("xpath", "//*[@class='txt_gray']")
    elem.send_keys(text)


    elem = dv.find_element("xpath", "//*[@class='btn_check']")
    elem.click()

    sleep(0.5)

    soup = BeautifulSoup(dv.page_source, 'html.parser')
    return soup.select("p._result_text.stand_txt")[0].text

def r():
    try:
        result = run(input_entry.get())
        label.config(text=result)
    except Exception as e:
        label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("맞춤법 검사기")
root.resizable(False, False)
root.config(padx=10, pady=10, bg="#F8FBEF")

input_entry = tk.Entry(root, width=30, font=("Arial", 20), bg="#FBF5EF")
input_entry.grid(column=0, row=0)
input_entry.focus()

check_button = tk.Button(root, text="검사", width=8, font=("Arial", 15), bg="#FA5858", command=r)
check_button.grid(row=1, column=0)

label = tk.Label(root, text="", width=20, font=("Arial", 30), bg="#F8FBEF")
label.grid(column=0, row=2)

root.mainloop()
