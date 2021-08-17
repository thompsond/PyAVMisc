"""A collection of miscellaneous functions for accessing system devices."""

from random import seed, randint
from time import sleep
import pyautogui
from common_utils import get_formatted_date
from gtts import gTTS
from playsound import playsound
import pyperclip

def take_screenshot() -> None:
  """Take a screenshot.

  This is not fully supported on Linux.
  """
  file_path = f'Screenshot_{get_formatted_date()}.png'
  pyautogui.screenshot(file_path)
  print(f'Screenshot saved to {file_path}.')

def get_clipboard_contents() -> None:
  print(pyperclip.paste() or 'Nothing on the clipboard.')

def set_clipboard_contents() -> None:
  text = input('Enter the text to save to the clipboard: ')
  pyperclip.copy(text)

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
  tts_obj = gTTS(text=text, lang='en', slow=False)
  file_path = f'Text_{get_formatted_date()}.mp3'
  tts_obj.save(file_path)
  print(f'Speech saved to {file_path}.')
  playsound(file_path)
