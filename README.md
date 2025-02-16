Here’s a **README.md** file for your GitHub project. This document explains how your **auto-clicker** works, how to customize it for different colors and sizes, and how to run it.  

---

### **📜 README.md - Auto-Clicker for Color Detection**  

# **🎯 Auto-Clicker for Game Squares**
This is a **Python-based auto-clicker** that detects and clicks on specific colored objects in a game using **computer vision (OpenCV)** and **screen capture (MSS)**.  

By default, it detects **purple squares (RGB: 255, 0, 254) and clicks on them automatically**. You can **customize it** to detect and click on **objects of different colors and sizes**.

---

## **🛠️ Features**
✅ Detects **specific colored objects** on the screen  
✅ Clicks on both **small and large objects**  
✅ Runs on **multiple monitors** (selects the correct one)  
✅ Optimized for **speed and accuracy**  
✅ Customizable for **any color and object size**

---

## **🚀 Installation & Requirements**
### **1️⃣ Install Dependencies**
This script requires **Python 3** and the following libraries:
```bash
pip install opencv-python pyautogui numpy mss
```
### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/auto-clicker.git
cd auto-clicker
```

### **3️⃣ Run the Auto-Clicker**
```bash
python auto_clicker.py
```
💡 **Switch to the game window within 3 seconds** after starting the script.

---

## **🔧 Customization Guide**
You can **modify the script** to detect **different colors, object sizes, and monitor settings**.

### **1️⃣ Change the Detected Color**
By default, the script detects **purple (RGB: 255, 0, 254)**, which translates to this **HSV range**:
```python
lower_purple = np.array([148, 90, 90])  
upper_purple = np.array([152, 255, 255])
```
To detect a **different color**:
1. Use a tool like [RapidTables](https://www.rapidtables.com/convert/color/rgb-to-hsv.html) to **convert RGB to HSV**.
2. Replace `lower_purple` and `upper_purple` with the **new HSV range**.

Example:  
For **red objects (RGB: 255, 0, 0)**:
```python
lower_red = np.array([0, 100, 100])  
upper_red = np.array([10, 255, 255])
```
For **green objects (RGB: 0, 255, 0)**:
```python
lower_green = np.array([50, 100, 100])  
upper_green = np.array([70, 255, 255])
```

---

### **2️⃣ Change the Detected Object Size**
The script **ignores very small detections** to avoid clicking noise.
```python
if w > 5 and h > 5:  # Minimum size filter
```
To detect **larger objects only**, increase the values:
```python
if w > 20 and h > 20:
```
To detect **smaller objects**, decrease the values:
```python
if w > 3 and h > 3:
```

---

### **3️⃣ Select a Different Monitor**
If you're using **multiple monitors**, change this line:
```python
MONITOR_INDEX = 1  # Set to the correct monitor number
```
To **find your monitor index**, run:
```python
import mss
with mss.mss() as sct:
    for i, monitor in enumerate(sct.monitors):
        print(f"Monitor {i}: {monitor}")
```
Then update **`MONITOR_INDEX`** in `auto_clicker.py`.

---

## **🖥️ Full Auto-Clicker Script**
```python
import cv2
import numpy as np
import pyautogui
import mss
import time

# Select the correct monitor
MONITOR_INDEX = 1  

# Define the color range (default: purple)
lower_purple = np.array([148, 90, 90])  
upper_purple = np.array([152, 255, 255])  

def find_squares():
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(sct.monitors[MONITOR_INDEX]))  # Capture screen
        hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)  # Convert to HSV
        mask = cv2.inRange(hsv, lower_purple, upper_purple)

        # Find contours (detected squares)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        positions = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 5 and h > 5:  # Adjust min size if needed
                positions.append((x + w // 2, y + h // 2))  # Get center

        return positions

def auto_click():
    print("Auto-clicker starts in 3 seconds... Switch to the game window!")
    time.sleep(3)  

    while True:
        positions = find_squares()

        if positions:
            for pos in positions:
                pyautogui.moveTo(pos[0], pos[1], duration=0.01)  # Move quickly
                pyautogui.click()
        
        time.sleep(0.01)  # Fast clicking

# Start auto-clicking
auto_click()
```

---

## **📜 License**
This project is **open-source** and released under the **MIT License**. Feel free to modify and distribute.

---

## **💡 Future Improvements**
- Add **support for clicking multiple colors**.
- Add a **GUI** to adjust color detection dynamically.
- Improve performance for **faster object tracking**.

---


🔥 **Your GitHub project is now documented and ready to go!** Let me know if you need any refinements! 🚀🔥
