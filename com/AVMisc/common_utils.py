"""A collection of helper functions for AVMisc."""

from datetime import datetime as dt
from os import path

def get_file_path() -> str:
  """Gets a file path from the user.

  Reads a file path from the user and checks that the file exits.

  Returns:
    A validated path to a file.

  Raises:
    FileNotFoundError: If the given file path does not exist.
  """
  file_path = input('Enter the path to the file: ')
  if not path.exists(file_path):
    raise FileNotFoundError(f'The file \'{file_path}\' does not exist.')
  return file_path

def get_formatted_date() -> str:
  return dt.now().strftime('%m_%d_%Y_%H_%M_%S')
