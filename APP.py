import pyautogui
import time
while True:
    user = input('enter app name ')
    
    if  user.strip().lower() == 'exit':
        print("Stopping programm execution ")
        break


   
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write(user , interval=0.1)
    
    pyautogui.press('enter')