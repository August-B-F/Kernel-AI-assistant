from components.Constants import *
import interception
import time 
import random
from interception import Interception, MouseStroke, Device, KeyState, FilterMouseState

def press_key(key_code, context, stroke, device):
    stroke.code = int(key_code)
    stroke.state = KeyState.KEY_DOWN
    context.send(device, stroke)
    time.sleep(random.randint(1, 10)/100)
    stroke.state = KeyState.KEY_UP
    context.send(device, stroke)

def fake_write(message):
    time.sleep(0.5)
    times_crashed = 0
    saved_value = ""
    pause = False

    context = Interception()
    context.set_filter(context.is_keyboard, FilterKeyState.FILTER_KEY_DOWN)
    
    for char in message:
        try: 
            device = context.wait()
            stroke = context.receive(device)
            if context.is_keyboard(device):
                if stroke.code == 1:
                    context.destroy()
                    break
                
                if stroke.code == 15:
                    if pause:
                        pause = False
                    else:
                        pause = True
                        saved_value = char

                if pause:
                    while pause:
                        device = context.wait()
                        stroke = context.receive(device)
                        if stroke.code == 15:
                            press_key(int(key_codes[saved_value]), context, stroke, device)
                            pause = False
                            break
                        else:
                            context.send(device, stroke)
                else:   
                    if char != " " and char != "\n" and char != "\t" and char.isupper() == False and char not in alt_keys and char not in caps_keys and char in key_codes:
                        key_code = int(key_codes[char])
                        press_key(key_code, context, stroke, device)

                    elif char.isupper() or char in caps_keys:
                        stroke.code = int(key_codes["shift"])
                        stroke.state = KeyState.KEY_DOWN
                        context.send(device, stroke)

                        time.sleep(random.randint(1, 10)/speed)

                        if char in caps_keys:
                            key_code = int(caps_keys[char])
                            press_key(key_code, context, stroke, device)
                        else:
                            key_code = int(key_codes[char.lower()])
                            press_key(key_code, context, stroke, device)

                        time.sleep(random.randint(1, 10)/speed)

                        stroke.code = int(key_codes["shift"])
                        stroke.state = KeyState.KEY_UP
                        context.send(device, stroke)


                    elif char == " ":
                        key_code = int(key_codes["space"])
                        press_key(key_code, context, stroke, device)
                        
                    elif char == "\n":
                        key_code = int(key_codes["enter"])
                        press_key(key_code, context, stroke, device)

                    elif char in alt_keys: 
                        stroke.code = int(key_codes["alt"])
                        stroke.state = KeyState.KEY_DOWN
                        context.send(device, stroke)

                        time.sleep(random.randint(1, 10)/speed)

                        stroke.code = int(key_codes["ctrl"])
                        stroke.state = KeyState.KEY_DOWN
                        context.send(device, stroke)

                        time.sleep(random.randint(1, 10)/speed)

                        key_code = int(alt_keys[char])
                        press_key(key_code, context, stroke, device)

                        time.sleep(random.randint(1, 10)/speed)

                        stroke.code = int(key_codes["alt"])
                        stroke.state = KeyState.KEY_UP
                        context.send(device, stroke)

                        time.sleep(random.randint(1, 10)/speed)

                        stroke.code = int(key_codes["ctrl"])
                        stroke.state = KeyState.KEY_UP
                        context.send(device, stroke)
                    
            else:
                print("Key not found:", char)

        except Exception as e:
            print("ERROR", e)
            times_crashed += 1
            if times_crashed > 10:
                break
            continue

    context.destroy()

def paste_text(message, context, write_speed=0.5):
    time.sleep(write_speed)
    times_crashed = 0   
    stroke = context.receive(device)

    for char in message:
     
        try: 
            time.sleep(random.randint(1, 10)/speed)

            if char != " " and char != "\n" and char != "\t" and char.isupper() == False and char not in alt_keys and char not in caps_keys and char in key_codes:
                key_code = int(key_codes[char])
                press_key(key_code, context, stroke, device)

            elif char.isupper() or char in caps_keys:
                stroke.code = int(key_codes["shift"])
                stroke.state = KeyState.KEY_DOWN
                context.send(device, stroke)

                time.sleep(random.randint(1, 10)/speed)

                if char in caps_keys:
                    key_code = int(caps_keys[char])
                    press_key(key_code, context, stroke, device)
                else:
                    key_code = int(key_codes[char.lower()])
                    press_key(key_code, context, stroke, device)

                time.sleep(random.randint(1, 10)/speed)

                stroke.code = int(key_codes["shift"])
                stroke.state = KeyState.KEY_UP
                context.send(device, stroke)


            elif char == " ":
                key_code = int(key_codes["space"])
                press_key(key_code, context, stroke, device)
                
            elif char == "\n":
                key_code = int(key_codes["enter"])
                press_key(key_code, context, stroke, device)

            elif char in alt_keys: 
                stroke.code = int(key_codes["alt"])
                stroke.state = KeyState.KEY_DOWN
                context.send(device, stroke)

                time.sleep(random.randint(1, 10)/speed)

                stroke.code = int(key_codes["ctrl"])
                stroke.state = KeyState.KEY_DOWN
                context.send(device, stroke)

                time.sleep(random.randint(1, 10)/speed)

                key_code = int(alt_keys[char])
                press_key(key_code, context, stroke, device)

                time.sleep(random.randint(1, 10)/speed)

                stroke.code = int(key_codes["alt"])
                stroke.state = KeyState.KEY_UP
                context.send(device, stroke)

                time.sleep(random.randint(1, 10)/speed)

                stroke.code = int(key_codes["ctrl"])
                stroke.state = KeyState.KEY_UP
                context.send(device, stroke)

            else:
                print("Key not found:", char)

        except Exception as e:
            print("ERROR", e)
            times_crashed += 1
            if times_crashed > 10:
                break
            continue
