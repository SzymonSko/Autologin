import tkinter as tk
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

username = "tomsmith"
password = "SuperSecretPassword!"

HEIGHT = 300
WIDTH = 500

root = tk.Tk()
root.title("AutoLogin")
background = "blue"
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='skyblue')
frame.place(relx = 0.125, rely = 0.125, relwidth=0.75, relheight=0.75)

def run():
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.CLASS_NAME,"radius").click()
    WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === ' complete'")
    )
    
def callback(url):
    webbrowser.open_new(url)


label_link = tk.Label(frame, text="Do u want to login to page:\n https://the-internet.herokuapp.com/login \n Your login is: {}".format( username), bg = 'skyblue', cursor="hand2")
label_link.place(relx = 0.55, rely = 0.22, relwidth=0.75, relheight=0.6, anchor='n')
label_link.bind("<Button-1>", lambda e: callback("https://the-internet.herokuapp.com/login"))

b1 = tk.Button(frame, text="Login", command=run, bg='gray')
b1.place(relx = 0.4, rely = 0.75, relwidth=0.3, relheight=0.2)



root.mainloop()

    