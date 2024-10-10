import os
from io import BytesIO
from PIL import Image
import struct
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pynput import keyboard, mouse
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread
import ctypes
import time

time.sleep(15)

def capture_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    return screenshot

def png_to_cur(png_data):
    png_image = Image.open(BytesIO(png_data))
    png_image = png_image.convert('RGBA')
    width, height = png_image.size
    cur_header = struct.pack('<HHH', 0, 2, 1)
    cur_entry = struct.pack('<BBBBHHII', width % 256, height % 256, 0, 0, 1, 1, len(png_data), 22)
    cur_data = BytesIO()
    cur_data.write(cur_header)
    cur_data.write(cur_entry)
    cur_data.write(png_data)
    cur_bytes = cur_data.getvalue()
    return cur_bytes

def load_cursor_from_file(file_path):
    try:
        cursor_handle = ctypes.windll.user32.LoadImageW(None, file_path, 2, 0, 0, 16)
        if cursor_handle == 0:
            raise ctypes.WinError()
        return cursor_handle
    except Exception as e:
        print(f"Error loading cursor from file: {str(e)}")
        return None

def set_system_cursor(cursor_handle, cursor_id):
    ctypes.windll.user32.SetSystemCursor(cursor_handle, cursor_id)

def restore_cursors():
    ctypes.windll.user32.SystemParametersInfoW(0x57, 0, None, 0)

def set_custom_cursor(file_path):
    cursor_handle = load_cursor_from_file(file_path)
    if cursor_handle is not None:
        cursors = [32512, 32513, 32514, 32515, 32516, 32640, 32641, 32642, 32643, 32644, 32645,
                   32646, 32648, 32649, 32650, 32651]
        for cursor_id in cursors:
            set_system_cursor(cursor_handle, cursor_id)
    else:
        print("Failed to load the custom cursor. Using default system cursors.")

IMAGE_CURSOR = 2
LR_LOADFROMFILE = 16

running = True
mouse_blocked = False
cursor_position = {'x': 0, 'y': 0}

def on_press(key):
    global running
    global driver
    if running:
        if key == keyboard.Key.esc:
            running = False
        else:
            try:
                ActionChains(driver).send_keys(key.char).perform()
            except AttributeError:
                pass

def on_move(x, y):
    global cursor_position
    cursor_position['x'] = x
    cursor_position['y'] = y

def on_click(x, y, button, pressed):
    global driver
    if pressed:
        if button == mouse.Button.left:
            driver.execute_script("document.elementFromPoint(arguments[0], arguments[1]).click();", x, y)
        elif button == mouse.Button.right:
            driver.execute_script("var event = new MouseEvent('contextmenu', {clientX: arguments[0], clientY: arguments[1]}); document.elementFromPoint(arguments[0], arguments[1]).dispatchEvent(event);", x, y)

def on_scroll(x, y, dx, dy):
    global driver
    driver.execute_script(f"window.scrollBy(0, {dy * 100});")

def start_listener():
    with keyboard.Listener(on_press=on_press) as key_listener:
        key_listener.join()

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.rapidtables.com/tools/notepad.html")

listener_thread = Thread(target=start_listener)
listener_thread.daemon = True
listener_thread.start()

# Create a custom cursor element inside the Chrome window
driver.execute_script("""
    var cursorElement = document.createElement('div');
    cursorElement.id = 'customCursor';
    cursorElement.style.position = 'fixed';
    cursorElement.style.zIndex = '9999';
    cursorElement.style.width = '20px';
    cursorElement.style.height = '20px';
    cursorElement.style.backgroundColor = 'red';
    cursorElement.style.borderRadius = '5px';
    cursorElement.style.pointerEvents = 'none';
    document.body.appendChild(cursorElement);
""")

# Create a mouse controller using pynput
mouse_controller = mouse.Controller()

while running:
    png_data = capture_screenshot(driver)
    cur_data = png_to_cur(png_data)
    custom_cursor_path = os.path.join(os.path.dirname(__file__), "custom_cursor.cur")
    with open(custom_cursor_path, 'wb') as file:
        file.write(cur_data)
    if os.path.isfile(custom_cursor_path):
        set_custom_cursor(custom_cursor_path)
    else:
        print("Custom cursor file not found. Using default system cursors.")

    # Move the custom cursor element based on the mouse movement
    driver.execute_script("""
        var cursorElement = document.getElementById('customCursor');
        if (cursorElement) {
            cursorElement.style.left = arguments[0] + 'px';
            cursorElement.style.top = arguments[1] + 'px';
        }
    """, cursor_position['x'], cursor_position['y'])

    # Move the physical mouse cursor to the custom cursor position
    mouse_controller.position = (cursor_position['x'], cursor_position['y'])

restore_cursors()
driver.quit()