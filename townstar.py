# from Tools import tools_v000 as tools
import os
from os.path import dirname
import keyboard
from keyboard import KEY_UP, KEY_DOWN, press, press_and_release
import time

# Mouse move
# https://automatetheboringstuff.com/chapter18/
import pyautogui

# -8 for the name of this project TownStar
# save_path = os.path.dirname(os.path.abspath("__file__"))
# propertiesFolder_path = save_path + "/"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'TownStar', 'user_text=')

def GoToTownStar() :
    press_and_release('cmd+tab')
    # Select the truck
    time.sleep(2)
    pyautogui.click(650, 450, button='left')

    # Select the icon to sell 
    time.sleep(2)
    pyautogui.click(750, 750, button='left')

    # Select the "marchandise"
    time.sleep(2)
    pyautogui.click(100, 750, button='left')

    # Select the button to send the truck
    time.sleep(5)
    pyautogui.click(1300, 400, button='left')

GoToTownStar()

for i in range(40):
    time.sleep(1)
    if (i == 100) :
        pyautogui.click(1300, 400, button='left')

    if (i == 200) :
        pyautogui.click(1300, 400, button='left')
        
    if (i == 300) :
        pyautogui.click(1300, 400, button='left')

    if (i == 400) :
        pyautogui.click(1300, 400, button='left')

    if (i == 500) :
        pyautogui.click(1300, 400, button='left')

    if (i == 600) :
        pyautogui.click(1300, 400, button='left')

    if (i == 700) :
        pyautogui.click(1300, 400, button='left')

    if (i == 800) :
        pyautogui.click(1300, 400, button='left')

    if (i == 900) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1000) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1100) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1200) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1300) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1400) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1500) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1600) :
        pyautogui.click(1300, 400, button='left')

    if (i == 1700) :
        pyautogui.click(1300, 400, button='left')

    # if (i == 1800) :
    #     pyautogui.click(1300, 400, button='left')

    # if (i == 1900) :
    #     pyautogui.click(1300, 400, button='left')

    # if (i == 2000) :
    #     pyautogui.click(1300, 400, button='left')

    # if (i == 2100) :
    #     pyautogui.click(1300, 400, button='left')

    # if (i == 2200) :
    #     pyautogui.click(1300, 400, button='left')

    # if (i == 2300) :
    #     pyautogui.click(1300, 400, button='left')

    # if (i == 2400) :
    #     pyautogui.click(1300, 400, button='left')
    print(i)

# Go to the Run button (For testing only)
if (True) :
    # Return to the Visual Studio Code
    time.sleep(2)
    press_and_release('cmd+tab')
    time.sleep(2)
    
    # Click to the run button in Visual Studio Code
    # time.sleep(2)
    # press_and_release('^ + F5')
    # time.sleep(1)
    # press_and_release('^ + F5')
    # pyautogui.click(1330, 70, button='left')
    time.sleep(2)
    pyautogui.click(380, 10, button='left')
    time.sleep(2)
    pyautogui.click(380, 40, button='left')
    time.sleep(2)
    pyautogui.click(800, 500, button='left')