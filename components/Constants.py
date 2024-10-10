from interception import Interception, FilterKeyState
from pynput.keyboard import Listener
from tkinter import messagebox
from dotenv import load_dotenv
from datetime import datetime
from pygame.locals import *
from pygame import Rect
import tkinter as tk
import interception 
import subprocess
import threading
import pyperclip
import keyboard
import colorsys
import win32gui
import win32api
import win32con
import asyncio
import pygame 
import random
import openai
import time
import json
import sys
import os

from pygame.locals import QUIT

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

# webdriver_path = "assets/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

data = {
    "Text_files": {
    }
}

prompts = {
    "explain" : "You are an expert teacher. Explain the concept of [insert topic, e.g., quantum physics] in 500 words or less in a way that a 12-year-old can understand.",
}

key_codes = {
    "esc": "1",
    "1": "2",
    "2": "3",
    "3": "4",
    "4": "5",
    "5": "6",
    "6": "7",
    "7": "8",
    "8": "9",
    "9": "10",
    "0": "11",
    "+": "12",
    "´": "13",
    "backspace": "14",
    "tab": "15",
    "q": "16",
    "w": "17",
    "e": "18",
    "r": "19",
    "t": "20",
    "y": "21",
    "u": "22",
    "i": "23",
    "o": "24",
    "p": "25",
    "å": "26",
    "¨": "27",
    "enter": "28",
    "ctrl": "29",
    "a": "30",
    "s": "31",
    "d": "32",
    "f": "33",
    "g": "34",
    "h": "35",
    "j": "36",
    "k": "37",
    "l": "38",
    "ö": "39",
    "ä": "40",
    "§": "41",
    "shift": "42",
    "'": "43",
    "z": "44",
    "x": "45",
    "c": "46",
    "v": "47",
    "b": "48",
    "n": "49",
    "m": "50",
    ",": "51",
    ".": "52",
    "-": "53",
    "right_shift": "54",
    "*": "55",
    "alt": "56",
    "space": "57",
    "caps_lock": "58",
    "f1": "59",
    "f2": "60",
    "f3": "61", 
    "f4": "62",
    "f5": "63",
    "f6": "64",
    "f7": "65",
    "f8": "66",
    "f9": "67",
    "f10": "68",
    "num_lock": "69",
    "scroll_lock": "70",
    "print_screen": "84",
    "<": "86",
    "f11": "87",
    "f12": "88",
    "f13": "100",
    "f14": "101",
    "f15": "102",
    "f16": "103",
    "f17": "104",
    "f18": "105",
    "f19": "106",
    "f20": "107",
    "f21": "108",
    "f22": "109",
    "f23": "110",
    "f24": "111",
}

caps_keys = {
    "!": "2", 
    '"': "3",
    "#": "4",
    "¤": "5",
    "%": "6",
    "&": "7",
    "/": "8",
    "(": "9",
    ")": "10",
    "=": "11",
    "?": "12",
    "`": "13",
    "reverse_tab": "15",
    "^": "27",
    ";": "51",
    ":": "52",
    "_": "53",
    ">": "86",
}

alt_keys = {
    "@": "3", 
    "£": "4",
    "$": "5",
    "{": "8", 
    "[": "9",
    "]": "10",
    "}": "11",
    "\\": "12",
    "~": "27",
    "|": "86",
}

clicked = False
running = True

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

AI_mode = "Free"

root = tk.Tk()
root.withdraw()  

pygame.init()
pygame.font.init()

icon = pygame.image.load('assets/logo.png')
pygame.display.set_caption('DolceLaze')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE + pygame.SCALED)
clock = pygame.time.Clock()

message = "Hello World, this is a test."
time_delay = 0.4
SYNC = False
speed = 80

pasting = False

screen_hidden = False

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

# Constants for colors
LIGHT_GREEN = (150, 158, 123)
DARK_BLUE = (124,135,122)
DARK_RED = (141,125,101)
WHITE = (255, 255, 255)
GREEN = (130, 138, 104)
LIGHT_RED = (194,62,62)
BLACK = (33, 39, 15)
BLUE = (124,135,172)
RED = (191,125,101)

# Constants for file types and their corresponding icons 
FILE_ICONS = {
    '.mp3': 'assets/pixel/music.png',
    '.wav': 'assets/pixel/music.png',
    '.mp4': 'assets/pixel/film.png',
    '.png': 'assets/pixel/img.png',
    '.jpg': 'assets/pixel/img.png',
    '.jpeg': 'assets/pixel/img.png',
    '.pdf': 'assets/pixel/pdf.png',
    '.exe': 'assets/pixel/exe.png'
}

# Constants for layout
PREMADE_COLORS_RECTS = [pygame.Rect(20 + i*30, 260, 20, 20) for i in range(10)]
BRIGHTNESS_SLIDER_RECT = pygame.Rect(224, 50, 20, 200)  # Moved 2 pixels to the right
BACKGROUND_COLOR_RECT = pygame.Rect(0, 0, 340, 30)
SELECTED_COLOR_RECT = pygame.Rect(260, 50, 60, 60)
COLOR_PICKER_RECT = pygame.Rect(20, 50, 200, 200)
CLOSE_BUTTON_RECT = pygame.Rect(290, 0, 50, 30)
WINDOW_RECT = pygame.Rect(200, 200, 340, 300)
TOP_BAR_RECT = pygame.Rect(0, 0, 290, 30)

COLOR_WINDOW_OPEN = False
DRAGGING = False

OFFSET = (0, 0)

RGB_RECTS = [pygame.Rect(260, 120 + i*30, 60, 30) for i in range(3)]

#10 premade rgb colors
# '#0000FF', '#BF40BF', '#D2042D', '#ff9900', '#FFEA00', '#32CD32'
PREMADE_COLORS = [pygame.Color(0, 0, 255), pygame.Color(191, 64, 191), pygame.Color(210, 4, 45), pygame.Color(255, 153, 0), pygame.Color(255, 234, 0), pygame.Color(50, 205, 50), pygame.Color(255, 255, 255), pygame.Color(64, 244, 208), pygame.Color(255, 127, 80), pygame.Color(223, 255, 0)]

FILE_CARD_TEXT_HEIGHT = 20
SEARCH_BAR_MAX_LENGTH = 50
FILE_CARD_ICON_SIZE = 100
NUM_VISIBLE_ENTRIES = 16
SCROLL_BAR_COLOR = BLACK
DOUBLE_CLICK_TIME = 0.5
FILE_CARD_HEIGHT = 150
FILE_CARD_PADDING = 20
FILE_CARD_WIDTH = 150
SCROLL_BAR_WIDTH = 20
SCREEN_HEIGHT = 600
COLOR_PICKT = False
BUTTON_PADDING = 20
BUTTON_HEIGHT = 30
SCREEN_WIDTH = 800
BUTTON_WIDTH = 40
SCROLL_SPEED = 30
FONT_SIZE = 18
PADDING = 10

# use pixel.ttf for better looking text
KINDA_BIG_FONT = pygame.font.Font('assets/pixel.ttf', 30)
VERY_BIG_FONT = pygame.font.Font('assets/pixel.ttf', 40)
FONT = pygame.font.Font('assets/pixel.ttf', FONT_SIZE)
SMALL_FONT = pygame.font.Font('assets/pixel.ttf', 16)
BIG_FONT = pygame.font.Font('assets/pixel.ttf', 20)

# Tab related constants
TAB_WIDTH = SCREEN_WIDTH // 5
TAB_HEIGHT = 35
TAB_NAMES = ["Start", "File", "Settings", "Info", "Credits"]

# Button related constants
BUTTON_NAMES = ["Folder", "File", "Manual"]
OUTPUTNAME = ""

MODE_SELECTED = False
MANUAL_MODE = False

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

device = None
context = None  

interception.auto_capture_devices(keyboard=True)
