"""The entry point for AVMisc."""
import sys
from enum import Enum
from rich import print
import audio_utils

class Command(Enum):
  LIST_DEFAULT_AUDIO_DEVICES = 'list_def_audio_dev'
  LIST_ALL_AUDIO_DEVICES = 'list_all_audio_dev'
  HELP = 'help'
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
  },
  Command.HELP: {
    'description': 'Show this help message.',
    'method': None
  }
}

def _print_help() -> None:
  print('[bold red]------------------------\n'
        '[bold red]AVMISC OPTIONS\n'
        '[bold red]------------------------\n')
  for command, data in COMMANDS.items():
    print(f'\'{command.value}\': {data["description"]}\n')

def process_command(command: str) -> None:
  """Runs the method associated with the given command if it is valid.

  Args:
    command: The name of the command to run.

  Raises:
    ValueError: If an invalid command is given.
  """
  if command in [member.value for member in Command.__members__.values()]:
    COMMANDS[Command(command)]['method']()
  else:
    raise ValueError

def begin() -> None:
  """Serves as the entry method for AVMisc."""
  while True:
    print('[bold blue]avmisc>', end=' ')
    command = input('')
    try:
      if command == Command.HELP.value:
        _print_help()
      else:
        process_command(command)
    except ValueError:
      print(f'\'{command}\' is not a recognized command. Type \'help\' for ' +
      'a list of available commands.')


if __name__ == '__main__':
  begin()
