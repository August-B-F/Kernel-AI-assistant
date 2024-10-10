import win32gui
import win32api

# Get the device context for the screen
dc = win32gui.GetDC(0)

# Define a color (red in this case)
red = win32api.RGB(255, 0, 0)

while True:
    # Set the pixel at position (0,0) to red
    win32gui.SetPixel(dc, 0, 0, red)
