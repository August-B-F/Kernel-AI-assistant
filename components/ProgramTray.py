from components.Constants import *

def handle_window_hide():
    global screen_hidden
    screen_hidden = not screen_hidden
    if screen_hidden:
        pygame.display.set_mode((800, 600), flags=pygame.HIDDEN)
    else:
        pygame.display.set_mode((800, 600))

def on_quit_selected(systray):
    global running
    running = False

def on_toggle_window(systray):
    global screen_hidden
    screen_hidden = not screen_hidden
    if screen_hidden:
        pygame.display.set_mode((800, 600), flags=pygame.HIDDEN)
    else:
        pygame.display.set_mode((800, 600))

def on_tray_icon_clicked(hwnd, msg, wparam, lparam):
    if lparam == win32con.WM_LBUTTONUP:
        on_toggle_window(None)
    elif lparam == win32con.WM_RBUTTONUP:
        show_tray_menu(hwnd, msg, wparam, lparam)
    return True

def show_tray_menu(hwnd, msg, wparam, lparam):
    menu = win32gui.CreatePopupMenu()

    win32gui.AppendMenu(menu, win32con.MF_STRING, 1001, "Toggle Window")
    win32gui.AppendMenu(menu, win32con.MF_SEPARATOR, 0, "")
    win32gui.AppendMenu(menu, win32con.MF_STRING, 1002, "Quit")

    pos = win32gui.GetCursorPos()
    win32gui.SetForegroundWindow(tray_icon_hwnd)
    selected_item = win32gui.TrackPopupMenu(menu, win32con.TPM_LEFTALIGN | win32con.TPM_RETURNCMD, pos[0], pos[1], 0, tray_icon_hwnd, None)

    if selected_item == 1001:
        on_toggle_window(None)
    elif selected_item == 1002:
        on_quit_selected(None)

    win32gui.PostMessage(tray_icon_hwnd, win32con.WM_NULL, 0, 0)
    return True

def create_tray_icon():
    global tray_icon_hwnd
    hinst = win32api.GetModuleHandle(None)
    icon_path = os.path.abspath("assets/icon.ico")
    icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
    hicon = win32gui.LoadImage(hinst, icon_path, win32con.IMAGE_ICON, 0, 0, icon_flags)

    wc = win32gui.WNDCLASS()
    wc.hInstance = hinst
    wc.lpszClassName = "TrayIconClass"
    wc.lpfnWndProc = {win32con.WM_USER + 20: on_tray_icon_clicked}
    class_atom = win32gui.RegisterClass(wc)

    tray_icon_hwnd = win32gui.CreateWindow(class_atom, "Tray Icon", win32con.WS_OVERLAPPED | win32con.WS_SYSMENU, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hinst, None)
    win32gui.UpdateWindow(tray_icon_hwnd)

    nid = (tray_icon_hwnd, 0, win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP, win32con.WM_USER + 20, hicon, "DolceLaze")
    win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
