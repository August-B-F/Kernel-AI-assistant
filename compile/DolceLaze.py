from components.KeyIntercept import *
from components.Constants import * 
from components.UI import *
from components.AI import *

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
running = True

can_type = True 
selecting = False
# Function to stop the program
def kill_switch():
    global running
    running = False

hotkeys = {
    # (key_codes['ctrl'], key_codes['shift'], key_codes['k']): kill_switch,
}

stop_event = threading.Event()

def handle_keyboard_input(context, device):
    global running
    last_key_press_times = {}
    while not stop_event.is_set():  # Check if the stop event is set
        device = context.wait()
        stroke = context.receive(device)
        if context.is_keyboard(device) and can_type:
            key_code = stroke.code
            # Update the last press time for this key
            last_key_press_times[key_code] = datetime.now()
            
            # Check if the current key combination matches any hotkeys
            for hotkey, function in hotkeys.items():
                if all(key in last_key_press_times for key in hotkey):
                    # If all keys in the hotkey were pressed recently, execute the function
                    time_differences = [datetime.now() - last_key_press_times[key] for key in hotkey]
                    if max(time_differences).total_seconds() < 1:  # Change this to the max time allowed between key presses
                        function()

            context.send(device, stroke)

while running:

    screen.fill(LIGHT_GREEN)

    for event in pygame.event.get():
        if event.type == QUIT or pyperclip.paste() == "/exit":
            # Set the stop event to stop the thread
            stop_event.set()
            interception.press("esc")
            if tab.SYNC:
                keyboard_thread.join()

                # send a key that dosent do anything. Use the keyboard library to send a key
                
            running = False
            pygame.quit()  # Ensure pygame is properly quit
            sys.exit()

        if tab.name == "File": 
            files.update(event)

            if files.mode == "manual" or files.mode == "edit":
                files.text_box.handle_event(event)      

    update_UI()

    if selecting and pyperclip.paste() != "/select":
        message = pyperclip.paste()
        selecting = False
        pyperclip.copy("selected")

    if tab.SYNC:
        try:  
            if pyperclip.paste() == "/te":
                message = """Hello world!"""
                time.sleep(1)
                for char in message:
                    interception.press(char.lower())
                    time.sleep(random.randint(1, 10)/speed)
                pyperclip.copy("")

            if pyperclip.paste() == "/select":
                selecting = True

            if pyperclip.paste().find("/essay") != -1 and pyperclip.paste() != "/te, /h, /p_mode, /select, /save, /chat, /save_chat, /answer, /explain":
                pasting = True
                # if mode == "write":
                    # if p_mode: 
                    #     message = pyperclip.paste().split("/ey")[1].split("\n")
                    #     while pasting:
                    #         for essay in range(len(message)):
                    #             pyperclip.copy("loading...")
                    #             time.sleep(0.2)
                    #             message = send_text(OPENAI_API_KEY, essay, model, None)
                    #             await send_message(interceptor_process, message)
                    #             pyperclip.copy("Essay done")
                    #             pasting = False 
                    # else:
                while pasting:
                    essay = pyperclip.paste().split("/essay")[1]
                    pyperclip.copy("loading...")
                    time.sleep(0.2)
                    message = send_text(OPENAI_API_KEY, essay, "gpt-4", None)
                    pyperclip.copy(message)
                    pasting = False
                # else: 
                #     essay = pyperclip.paste().split("/ey")[1]
                #     pyperclip.copy("loading...")
                #     time.sleep(0.2)
                #     message = send_text(OPENAI_API_KEY, essay, model, None)
                #     pyperclip.copy(message)

                #         # wait for 

            if pyperclip.paste() == "/h": 
                # copys all the commands to the clipboard
                pyperclip.copy("/'te, /'essay, /'h, /'select, /'answer, remove '") 

            # if pyperclip.paste() == "/UI":
            #     pyperclip.copy("trying to open ui")
            #     dc = win32gui.GetDC(0)
            #     red = win32api.RGB(255, 0, 0)
            #     #make big red rectangel  
            #     row = 0
            #     cul = 0

            #     while row < 100:
            #         while cul < 100:
            #             win32gui.SetPixel(dc, row, cul, red)
            #             cul += 1
            #         row += 1
            #         cul = 0 

            # if pyperclip.paste() == "/select": 
            #     with open('data.json', 'r') as outfile:
            #         data = json.load(outfile)
                
            #     name = data["Text_files"]

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
                # while pasting:
                #     essay = pyperclip.paste().split("/answer")[1]
                #     pyperclip.copy("loading...")
                #     time.sleep(0.2)
                #     message = send_text(OPENAI_API_KEY, essay, model, None)
                #     pyperclip.copy(message)
                #     pasting = False
         
        except Exception as e:
                print(e)
                pyperclip.copy("Error saving chat")
                can = True
                
        
    pygame.display.flip()
    clock.tick(60)

    if tab.load_process: 

        context = Interception()
        context.set_filter(context.is_keyboard, FilterKeyState.FILTER_KEY_DOWN)
        print("Enter key to start")
        device = context.wait()

        keyboard_thread = threading.Thread(target=handle_keyboard_input, args=(context, device))
        keyboard_thread.start()

        tab.load_process = False
        tab.SYNC = True 

pygame.quit()