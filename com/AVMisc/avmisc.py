"""The entry point for AVMisc."""
import sys
from enum import Enum
import audio_utils

class Command(Enum):
  LIST_DEFAULT_AUDIO_DEVICES = 'list_def_audio_dev'
  LIST_ALL_AUDIO_DEVICES = 'list_all_audio_dev'
  EXIT = 'exit'

COMMANDS = {
  Command.LIST_DEFAULT_AUDIO_DEVICES: {
    'description': 'List the default audio devices on the system.',
    'method': audio_utils.list_default_devices
  },
  Command.LIST_ALL_AUDIO_DEVICES: {
    'description': 'List all the audio devices on the system.',
    'method': audio_utils.list_all_devices
  },
  Command.EXIT: {
    'description': 'Exit the program.',
    'method': sys.exit
  }
}

def process_command(command: str) -> None:
  """Runs the method associated with the given command if it is valid.

  Args:
    command: The name of the command to run.
  """
  try:
    COMMANDS[Command(command)]['method']()
  except ValueError:
    print(f'\'{command}\' is not a recognized command. Type \'help\' for ' +
      'a list of available commands.')

def begin() -> None:
  """Serves as the entry method for AVMisc."""
  while True:
    command = input('avmisc>')
    process_command(command)


if __name__ == '__main__':
  begin()
