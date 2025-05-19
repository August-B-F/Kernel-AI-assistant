# DolceLaze: Your Kernel AI Assistant

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)

**DolceLaze is a versatile Python-based desktop application designed to streamline your workflow with AI-powered text generation, advanced input automation, and a user-friendly interface.**

## Overview

DolceLaze leverages the power of OpenAI's GPT models to provide on-demand text generation, from quick answers to more extensive essays. It integrates seamlessly into your desktop environment with a system tray icon for easy access and control. The application features a Pygame-based graphical user interface (GUI) for intuitive interaction, file management for your text snippets, and kernel-level keyboard interception for powerful and realistic automation capabilities.

## ✨ Features

* **AI-Powered Text Generation:**
    * Generate essays using GPT-4 with the `/essay [prompt]` command in your clipboard.
    * Get concise answers using GPT-3.5-turbo with the `/answer [question]` command.
* **Clipboard-Activated Commands:**
    * Quickly trigger actions by copying specific commands to your clipboard.
    * Examples: `/te` (types "Hello world!"), `/select` (captures the next copied item), `/h` (shows help).
* **Realistic Simulated Typing ("Fake Write"):**
    * Automatically type out generated or predefined text with the `/fw` command.
    * **Kernel-Level Keystroke Injection:** This is achieved using the `interception` library, which operates at the kernel level. This allows DolceLaze to send keystrokes that are indistinguishable from actual human typing to the operating system and other applications.
    * Adjustable typing speed for a more natural effect.
* **Graphical User Interface (Pygame):**
    * **Tabbed Navigation:** Easy access to different sections: "Start", "File", "Settings" (planned), "Info", and "Credits".
    * **File Management Tab:**
        * View and manage locally stored text files/snippets (from `data.json`).
        * Add new text manually or import from `.txt` files.
        * Edit and delete existing text entries.
    * **System Tray Integration:**
        * Show/hide the application window.
        * Quit the application directly from the tray menu.
* **Low-Level Keyboard Interception:**
    * Utilizes `python-interception` (via `interception` import) for deep integration with keyboard inputs. This enables not only the realistic typing simulation but also the potential for complex custom hotkeys and system-wide command triggers.
    * The `KeyIntercept.py` component manages the specifics of capturing physical key presses and dispatching simulated ones.

## 🔌 Advanced Input Control with `python-interception`

A core aspect of DolceLaze's automation capabilities, particularly the "Fake Write" feature, is its use of the `interception`. It allows DolceLaze to operate at a low level, interacting directly with the system's input devices.

* **Kernel-Level Operation:** `interception` works by installing a kernel-level driver (on Windows). This means it can intercept and simulate keyboard (and mouse) events before they are even processed by most applications.
* **Realistic Typing Simulation:** When DolceLaze "fake writes" text, it's not just pasting. Instead, it sends individual key press (`KeyState.KEY_DOWN`) and release (`KeyState.KEY_UP`) events through `interception`. This makes the output appear to any other application as if a human is genuinely typing at the keyboard, character by character, including simulated slight random delays between keystrokes.
* **How it's Used:**
    * The `KeyIntercept.py` module in DolceLaze is dedicated to this functionality.
    * Functions like `fake_write` and `press_key` sends these low-level keyboard strokes using the defined `key_codes`, `caps_keys`, and `alt_keys` from `Constants.py`.
    * It can handle regular characters, special keys (like Enter, Shift, Alt, Ctrl), and characters requiring modifiers.

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* The following Python libraries:
    * `pygame`
    * `pystray`
    * `Pillow (PIL)`
    * `openai`
    * `python-interception` (imported as `interception`) (Note: This library is for Windows and provides low-level keyboard/mouse hooking)
    * `pynput`
    * `tkinter` (usually comes with Python)
    * `python-dotenv`
    * `pywin32` (provides `win32gui`, `win32api`, `win32con`)
    * `selenium` (though its primary usage is in the 'dump' folder, it is listed in `Constants.py`)

### Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/August-B-F/Kernel-AI-assistant
    cd kernel-ai-assistant 
    ```
2.  **Set up OpenAI API Key:**
    * Create a file named `.env` in the project's root directory.
    * Add your OpenAI API key to it:
        ```env
        OPENAI_API_KEY='your_openai_api_key_here'
        ```
        This key is loaded by `components/Constants.py`.
3.  **Install dependencies:**
    Install packages:
    ```bash
    pip install pygame pystray Pillow openai python-interception pynput python-dotenv pywin32 selenium
    ```
    *Note: `python-interception` requires manual steps for its driver installation on Windows. Please refer to its official documentation.*

### Running DolceLaze

Execute the main application file:

```bash
python DolceLaze.py
````

## 🛠️ How to Use

### Main Window & System Tray

  * The application starts with a GUI window. The window title is "DolceLaze".
  * You can hide the window. The system tray icon (using `assets/icon.jpg`) allows you to "Show" the window again or "Quit" the application.
      * The `ProgramTray.py` component also defines functionality for a native Windows tray icon using `assets/icon.ico`, though `DolceLaze.py` currently uses `pystray`.

### AI Text Generation

1.  **For an Essay:**
      * Copy your desired prompt to the clipboard in the format: `/essay Your essay topic or instructions here`.
      * The application will detect the command, copy "loading..." to the clipboard, generate the text using GPT-4 (model "gpt-4"), and then copy the result back to your clipboard.
2.  **For a Quick Answer:**
      * Copy your question to the clipboard in the format: `/answer Your question here`.
      * The application will detect the command, copy "loading...", use GPT-3.5-turbo (model "gpt-3.5-turbo", referred to as "gpt3" in `DolceLaze.py`) to generate a concise answer, and copy it to your clipboard.

### Clipboard Commands

  * **/te**: The application will type out "Hello world\!" using the fake write functionality. (For testing)
  * **/select**: Activates selection mode. After copying this command, the next item you copy to your clipboard will be stored internally by the application. "selected" will be copied to your clipboard as confirmation.
  * **/fw**: Triggers the "fake write" mechanism to type out the message that was last captured (e.g., by `/select` or an AI generation command).
  * **/h**: Copies a help string listing available commands to your clipboard (e.g., "/'te, /'essay, /'h, /'select, /'answer, remove '").

### File Tab

  * Navigate to the "File" tab in the GUI.
  * This section allows you to manage text snippets stored in the `data.json` file.
  * **View Entries:** Displays existing text entries as cards.
  * **Add New Entry:**
      * Click the "+Add" button.
      * Choose "File" to open a file selector and import content from a `.txt` file.
      * Choose "Manual" to open a text box where you can type or paste text and provide a name for the new entry.
  * **Edit/Delete:** Clicking on an existing file card may reveal options to edit its content/name or delete the entry from `data.json`.

## 📂 Project Structure (Simplified)

```
kernel-ai-assistant/
├── DolceLaze.py              # Main application script
├── components/                 # Core modules
│   ├── AI.py                 # OpenAI API interaction
│   ├── Constants.py          # App constants, colors, API keys, key codes
│   ├── KeyIntercept.py       # Kernel-level keyboard hooking & simulation
│   ├── ProgramTray.py        # Native Windows System tray icon management
│   └── UI.py                 # Pygame UI elements (tabs, buttons, file manager)
├── assets/                     # Icons, fonts, etc.
│   ├── icon.jpg              # Used by pystray
│   ├── icon.ico              # For native Windows tray
│   ├── logo.png              # App logo
│   ├── pixel.ttf             # Font file
│   └── pixel/                # Directory for file type icons
├── data.json                   # Stores user-created text files/snippets
├── .env                        # For API keys (user needs to create this)
└── dump/                       # Experimental/test scripts (e.g., chrome_mouse.py, mouse.py)
```

## 📝 To-Do / Future Enhancements

(Based on comments in `DolceLaze.py`)

  * Fix acceleration for scroll.
  * Implement a full "Settings" panel.
  * Complete the "Info" tab.
  * Expand "Manual mode" with more functions.
  * Address the "color selector bug."
  * Improve window closing behavior to hide to tray instead of terminating (current `QUIT` event calls `handle_window_hide`).

## 📜 License

"Rights are reserved to the respective owners, not for commercial use."