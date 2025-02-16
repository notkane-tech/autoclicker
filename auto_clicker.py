import cv2
import numpy as np
import pyautogui
import mss
import time


MONITOR_INDEX = 1  

# HSV values for squares. NOT HTML 
lower_purple = np.array([148, 90, 90])  
upper_purple = np.array([152, 255, 255])  

def find_purple_squares():
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(sct.monitors[MONITOR_INDEX]))  
        hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)  
        mask = cv2.inRange(hsv, lower_purple, upper_purple)

      
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        positions = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 3 and h > 3: #square size 
                positions.append((x + w // 2, y + h // 2))  

        return positions

def auto_click():
    print("Auto-clicker starts in 5 seconds... Switch to the game window!")
    time.sleep(5)  # Give time to switch to the game

    while True:
        positions = find_purple_squares()

        if positions:
            for pos in positions:
                pyautogui.moveTo(pos[0], pos[1], duration=0.01)  # Move quickly
                pyautogui.click()
        
        time.sleep(0.01)  # Reduced delay for faster clicking

# Start auto-clicking
auto_click()
