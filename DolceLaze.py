from components.KeyIntercept import *
from components.Constants import * 
from components.UI import *
from components.AI import *

import pystray
from pystray import MenuItem as item
from PIL import Image

"""
Close the window, but not the entir program
Fix the color selector bug. 
"""

"""TODO later: 
Fixa aks till scroll 
Inställningar
Fixa info 
Fixa manual mode, med flera funktioner.
"""
# Set running to True initially

def handle_window_hide(icon, item):
    global screen_hidden
    global screen

    if screen_hidden:
        screen = pygame.display.set_mode((800, 600))
        screen_hidden = False
    
    else:
        screen = pygame.display.set_mode((800, 600), flags=pygame.HIDDEN)
        screen_hidden = True

    screen_hidden = False

def quit_window(icon, item):
    global running
    running = False
    icon.stop()

def create_system_tray():
    image = Image.open("assets/icon.jpg")  
    menu = (item('Show', handle_window_hide), item('Quit', quit_window))
    icon = pystray.Icon("name", image, "My Program", menu)
    icon.run()


screen_hidden = False
create_system_tray()

while running:
    if not screen_hidden:
        screen.fill(LIGHT_GREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                handle_window_hide(None, None)

            if tab.name == "File": 
                files.update(event)

                if files.mode == "manual" or files.mode == "edit":
                    files.text_box.handle_event(event)      

        update_UI()

        pygame.display.flip()
        clock.tick(60)


    if tab.SYNC:
        try:  
            if pyperclip.paste() == "/te":
                time.sleep(0.5)
                for char in "Hello world!":
                    interception.press(char.lower())
                    time.sleep(random.randint(1, 10)/speed)
                pyperclip.copy("")

            if pyperclip.paste() == "/select":
                selecting = True

            if selecting and pyperclip.paste() != "/select":
                message = pyperclip.paste()
                selecting = False
                pyperclip.copy("selected")


            if pyperclip.paste().find("/essay") != -1 and pyperclip.paste() not in ["/te", "/ey", "/h", "/select", "/answer", "/p_mode", "/save", "/chat", "/save_chat", "/explain"]:
                pasting = True

                while pasting:
                    essay = pyperclip.paste().split("/essay")[1]
                    pyperclip.copy("loading...")
                    time.sleep(0.2)
                    essay = essay.replace("\\", "")
                    message = send_text(OPENAI_API_KEY, essay, "gpt-4", None)
                    pyperclip.copy(message)
                    pasting = False

            if pyperclip.paste() == "/h": 
                pyperclip.copy("/'te, /'essay, /'h, /'select, /'answer, remove '") 

            if pyperclip.paste() == "/fw":
                pyperclip.copy("")
                can_type = False
                fake_write(message, context)
                can_type = True


            if pyperclip.paste().find("/answer") != -1 and pyperclip.paste() != "/te, /ey, /h, /p_mode, /select, /save, /chat, /save_chat, /explain":
                pasting = True
                while pasting:
                    essay = pyperclip.paste().split("/answer")[1]
                    pyperclip.copy("loading...")
                    time.sleep(0.2)
                    message = send_text(OPENAI_API_KEY, essay, "gpt3", None)
                    pyperclip.copy(message)
                    pasting = False

        except Exception as e:
                print(e)
                pyperclip.copy("Error saving chat")
                can = True
                

    if tab.load_process: 

        context = Interception()
        context.set_filter(context.is_keyboard, FilterKeyState.FILTER_KEY_DOWN)
        device = context.wait()

        keyboard_thread = threading.Thread(target=handle_keyboard_input, args=(context, device))
        keyboard_thread.start()

        tab.load_process = False
        tab.SYNC = True 

# Clean up the system tray icon
win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, (tray_icon_hwnd, 0))

pygame.quit() 