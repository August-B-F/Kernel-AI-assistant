from components.Constants import *
import interception
import time 
import random
from interception import Interception, FilterKeyState, KeyStroke, KeyState

def press_key(key_code, context, stroke, device):
    stroke.code = int(key_code)
    stroke.state = KeyState.KEY_DOWN
    context.send(device, stroke)
    time.sleep(random.randint(1, 10)/100)
    stroke.state = KeyState.KEY_UP
    context.send(device, stroke)

def fake_write(message, context):
    time.sleep(0.5)
    pause = False
    
    for char in message:
        try: 
            device = context.wait()
            stroke = context.receive(device)
            if context.is_keyboard(device):
                if stroke.code == 1:
                    break
                
                if stroke.code == 15:
                    if pause:
                        pause = False
                    else:
                        pause = True
                    continue

                if pause:
                    while pause:
                        device = context.wait()
                        stroke = context.receive(device)
                        if stroke.code == 15:
                            print("1")
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
                            print("2")
                            pause = False
                            break

                        else:
                            context.send(device, stroke)
                            continue
                    continue
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

def paste_text(message, context):
    time.sleep(0.5)
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
            continue
