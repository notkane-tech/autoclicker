import cv2
import numpy as np
import pyautogui
import mss
import time

# Define the correct monitor
MONITOR_INDEX = 1  # Update based on your screen

# HSV values for purple squares
lower_purple = np.array([148, 90, 90])  
upper_purple = np.array([152, 255, 255])  

def find_purple_squares():
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(sct.monitors[MONITOR_INDEX]))  # Capture correct screen
        hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)  # Convert to HSV
        mask = cv2.inRange(hsv, lower_purple, upper_purple)

        # Find contours (purple squares)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        positions = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 3 and h > 3:  # Now detects smaller squares too
                positions.append((x + w // 2, y + h // 2))  # Get center

        return positions

def auto_click():
    print("Auto-clicker starts in 3 seconds... Switch to the game window!")
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
