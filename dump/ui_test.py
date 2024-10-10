import win32gui
import win32con
import win32api
import time

def draw_red_rectangle(hwnd):
    # Get the dimensions of the window
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    # Calculate the dimensions of the red rectangle
    rect_width = width // 2
    rect_height = height // 2
    rect_left = left + (width - rect_width) // 2
    rect_top = top + (height - rect_height) // 2
    rect_right = rect_left + rect_width
    rect_bottom = rect_top + rect_height
    # Create a device context (DC) for the window
    hdc = win32gui.GetWindowDC(hwnd)
    # Create a pen with red color
    red_pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
    # Select the red pen into the DC
    prev_pen = win32gui.SelectObject(hdc, red_pen)
    # Draw the rectangle
    win32gui.Rectangle(hdc, rect_left, rect_top, rect_right, rect_bottom)
    # Clean up
    win32gui.SelectObject(hdc, prev_pen)
    win32gui.DeleteObject(red_pen)
    win32gui.ReleaseDC(hwnd, hdc)

def get_active_window_handle():
    return win32gui.GetForegroundWindow()

while True:
    # Get the handle of the active window
    window_handle = get_active_window_handle()
    if window_handle:
        # Draw the red rectangle
        draw_red_rectangle(window_handle)
    else:
        print("No active window found.")
    time.sleep(5)