import pyautogui
import time
import random

# Set the duration for the mouse wiggler to run (in seconds)
duration = 600  # 10 minutes

# Set the interval between mouse movements (in seconds)
interval = 10

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Get the current time
start_time = time.time()

print("Mouse wiggler started. Press Ctrl+C to stop.")

try:
    while time.time() - start_time < duration:
        # Generate random x and y coordinates within the screen bounds
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # Move the mouse to the random position
        pyautogui.moveTo(x, y, duration=0.5)

        # Wait for the specified interval before the next movement
        time.sleep(interval)

except KeyboardInterrupt:
    print("Mouse wiggler stopped.")
