from interception import Interception, MouseStroke, MouseState, MouseFlag, FilterMouseState, FilterKeyState
import interception

def get_trackpad_driver():
    devices = []
    context = Interception()
    for i in range(20):
        device = context.get_HWID(i)
        if device is not None:
            devices.append((i, device))

    for device_id, device_name in devices:
        if "ELAN" in device_name:
            print(f"The trackpad device is: {device_name}")
            return device_id
    
    return None

def main():
    trackpad_device_id = get_trackpad_driver()
    if trackpad_device_id is None:
        print("Trackpad device not found.")
        return

    context = Interception()
    context.set_filter(predicate=lambda device: device.id == trackpad_device_id, filter=FilterMouseState.FILTER_MOUSE_ALL)
    while True:
        device = context.wait()
        stroke = context.receive(device)
        print(f"Trackpad event detected: {stroke}")

if __name__ == "__main__":
    main()