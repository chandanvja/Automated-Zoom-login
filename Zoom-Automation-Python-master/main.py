import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    #use \\ in windows to avoid the unicode error
    subprocess.call("")

    time.sleep(10)
    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the meeting ID
    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)



    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)
    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%A,%H:%M")
    print(now)

    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)
       print('signed in')
