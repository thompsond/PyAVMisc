"""A collection of miscellaneous functions for accessing system devices."""

import pyautogui
from common_utils import get_formatted_date
import pyperclip

def take_screenshot() -> None:
  """Take a screenshot.

  This is not fully supported on Linux.
  """
  pyautogui.screenshot(f'Screenshot_{get_formatted_date()}.png')

def get_clipboard_contents() -> str:
  return pyperclip.paste() or 'Nothing on the clipboard.'
