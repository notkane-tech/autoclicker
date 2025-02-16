import cv2
import numpy as np
import mss

# Define the correct monitor (update this based on your result)
MONITOR_INDEX = 1  # Change this to actual screen 

# HSV values for purple squares (adjust as needed)
lower_purple = np.array([255, 0, 255])  
upper_purple = np.array([240, 0, 240])  

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
            if w > 10 and h > 10:
                positions.append((x + w // 2, y + h // 2))  # Get center

        print(f"Detected squares: {positions[:10]}")
        return positions

find_purple_squares()
