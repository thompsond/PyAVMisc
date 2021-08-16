"""The entry point for AVMisc."""
import sys
from enum import Enum
from rich import print
import audio_utils
import misc_utils

class Command(Enum):
  LIST_DEFAULT_AUDIO_DEVICES = 'list_def_audio_dev'
  LIST_ALL_AUDIO_DEVICES = 'list_all_audio_dev'
  PLAY_AUDIO = 'play_audio'
  STOP_PLAYING_AUDIO = 'stop_audio_playback'
  TAKE_SCREENSHOT = 'screenshot'
  CLIPBOARD = 'clipboard'
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
    Command.PLAY_AUDIO: {
        'description': 'Play an audio file on the system.',
        'method': audio_utils.play_audio_file
    },
    Command.STOP_PLAYING_AUDIO: {
        'description': 'Stop playing audio.',
        'method': audio_utils.stop_playing_audio
    },
    Command.TAKE_SCREENSHOT: {
        'description': 'Take a screenshot.',
        'method': misc_utils.take_screenshot
    },
    Command.CLIPBOARD: {
        'description': 'View the contents of the clipboard.',
        'method': misc_utils.get_clipboard_contents
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
    try:
      print('[bold blue]avmisc>', end=' ')
      command = input('')
      if command == Command.HELP.value:
        _print_help()
      else:
        process_command(command)
    except KeyboardInterrupt:
      sys.exit()
    except ValueError:
      print(f'\'{command}\' is not a recognized command. Type \'help\' for ' +
      'a list of available commands.')


if __name__ == '__main__':
  begin()
