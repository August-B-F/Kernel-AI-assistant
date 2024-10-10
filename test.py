from components.KeyIntercept import *
from components.Constants import * 
from components.UI import *
from components.AI import *
from components.ProgramTray import *

def process_command(command):
    global selecting, pasting, can_type, message

    if command == "/te":
        time.sleep(1)
        for char in "Hello world!":
            interception.press(char.lower())
            time.sleep(random.randint(1, 10) / speed)
        pyperclip.copy("")

    elif command == "/select":
        selecting = True

    elif selecting and command != "/select":
        message = command
        selecting = False
        pyperclip.copy("selected")

    elif command.startswith("/essay"):
        pasting = True
        essay = command.split("/essay")[1].replace("\\", "")
        pyperclip.copy("loading...")
        time.sleep(0.2)
        message = send_text(OPENAI_API_KEY, essay, "gpt-4", None)
        pyperclip.copy(message)
        pasting = False

    elif command == "/h":
        pyperclip.copy("/'te, /'essay, /'h, /'select, /'answer, remove '")

    elif command == "/fw":
        pyperclip.copy("")
        can_type = False
        fake_write(message)
        can_type = True

    elif command.startswith("/answer"):
        pasting = True
        essay = command.split("/answer")[1]
        pyperclip.copy("loading...")
        time.sleep(0.2)
        message = send_text(OPENAI_API_KEY, essay, "gpt3", None)
        pyperclip.copy(message)
        pasting = False

create_tray_icon()

while running:
    if not screen_hidden:
        screen.fill(LIGHT_GREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                handle_window_hide()

            if tab.name == "File": 
                files.update(event)

                if files.mode == "manual" or files.mode == "edit":
                    files.text_box.handle_event(event)      

        update_UI()

        pygame.display.flip()
        clock.tick(60)

    if tab.SYNC:
        try:  
            command = pyperclip.paste()
            if command:
                process_command(command)

        except Exception as e:
                print(e)
                pyperclip.copy(str(e))
                can = True
                
    if tab.load_process: 
        tab.load_process = False
        tab.SYNC = True 
    
    win32gui.PumpWaitingMessages()

# Clean up the system tray icon
win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, (tray_icon_hwnd, 0))