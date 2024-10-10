import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox
from ttkthemes import ThemedTk
import ctypes, sys
import subprocess
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_exe():
    exe_path = os.path.join(sys._MEIPASS, "install-interception.exe")
    if not os.path.exists(exe_path):
        mbox.showerror("Error", f"{exe_path} does not exist.")
        return
    params = "/install"
    command = f"{exe_path} {params}"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.stdout, process.stderr
    last_paragraph = stdout.decode().split('\n\n')[-1]
    mbox.showinfo("Program Response", last_paragraph)

    restart_label = ttk.Label(frame, text="Please restart your computer for the changes to take effect.")
    restart_label.pack()

if is_admin():
    root = ThemedTk(theme="arc")
    root.title("Run EXE in Admin Mode")

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = ttk.Label(frame, text="Click the button below to run install-interception.exe with /install parameter")
    label.pack(side=tk.TOP, pady=10)

    run_button = ttk.Button(frame, text="Run install-interception.exe", command=run_exe)
    run_button.pack(side=tk.BOTTOM)

    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)