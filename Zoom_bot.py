import pyautogui
import subprocess
import os
import pandas as pd
import time
from datetime import datetime

def join(id):
    subprocess.call("C:\\Users\\arnava\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(15)

    joinbtn = pyautogui.locateCenterOnScreen("join1.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()

    meetingidbtn = pyautogui.locateCenterOnScreen("join2.png")
    pyautogui.moveTo(meetingidbtn)
    pyautogui.click()
    pyautogui.write(id)

    videobtn = pyautogui.locateCenterOnScreen("join4.png")
    pyautogui.moveTo(videobtn)
    pyautogui.click()

    audiobtn = pyautogui.locateCenterOnScreen("join5.png")
    pyautogui.moveTo(audiobtn)
    pyautogui.click()

    join2btn = pyautogui.locateCenterOnScreen("join3.png")
    pyautogui.moveTo(join2btn)
    pyautogui.click()


running = True

df = pd.read_csv('timings.csv')

while running:
    now = datetime.now().strftime("%H:%M") 
    if now in str(df['timings']):
        
        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0, 1])

        join(m_id)
        time.sleep(20)
        print("Joined")

    
    



