import pythoncom
import pyWinhook as pyHook
import time

def on_mouse_event(event):
    # Return True to block the event
    return True

# Create a mouse hook manager
hook_manager = pyHook.HookManager()

# Register the mouse event callback
hook_manager.MouseAll = on_mouse_event

# Start the hook
hook_manager.HookMouse()

# Start the message loop
pythoncom.PumpMessages()

time.sleep(5)

# Unhook the mouse
hook_manager.UnhookMouse()

# Exit the program
exit()