"""A collection of miscellaneous functions for accessing system devices."""

import pyautogui
from common_utils import get_formatted_date
from random import seed, randint
from time import sleep
import pyperclip
import pyttsx3

def take_screenshot() -> None:
  """Take a screenshot.

  This is not fully supported on Linux.
  """
  pyautogui.screenshot(f'Screenshot_{get_formatted_date()}.png')

def get_clipboard_contents() -> str:
  return pyperclip.paste() or 'Nothing on the clipboard.'

def start_cursor_jump() -> None:
  """Make the cursor move to random locations on the screen."""
  seed(1)
  width, height = pyautogui.size()
  try:
    while True:
      pyautogui.moveTo(randint(0, width), randint(0, height))
      sleep(0.002)
  except KeyboardInterrupt:
    return

def speak_text() -> None:
  """Use an automated voice to speak the text given by the user."""
  text = input('Enter the text to speak: ')
  engine = pyttsx3.init()
  engine.setProperty('rate', 125)
  engine.say(text)
  engine.runAndWait()
