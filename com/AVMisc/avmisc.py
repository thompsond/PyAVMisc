"""The entry point for AVMisc."""
import sys
from enum import Enum
from rich import print
import audio_utils
import misc_utils
import ftp_utils
import video_utils

class InvalidCommandError(Exception):
  pass

class Command(Enum):
  """All of the commands for AVMisc."""
  LIST_DEFAULT_AUDIO_DEVICES = 'list_def_audio_dev'
  LIST_ALL_AUDIO_DEVICES = 'list_all_audio_dev'
  PLAY_AUDIO = 'play_audio'
  STOP_PLAYING_AUDIO = 'stop_audio_playback'
  RECORD_AUDIO = 'record_audio'
  STOP_RECORDING_AUDIO = 'stop_recording_audio'
  TAKE_SNAPSHOT = 'take_snapshot'
  TAKE_SCREENSHOT = 'screenshot'
  READ_CLIPBOARD = 'read_clipboard'
  WRITE_CLIPBOARD = 'write_clipboard'
  START_CURSOR_JUMP = 'start_cursor_jump'
  SPEAK_TEXT = 'speak_text'
  UPLOAD_FTP = 'upload_ftp'
  DOWNLOAD_FTP = 'download_ftp'
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
    Command.RECORD_AUDIO: {
        'description': 'Record audio on the system.',
        'method': audio_utils.start_recording_audio
    },
    Command.STOP_RECORDING_AUDIO: {
        'description': 'Stop recording audio.',
        'method': audio_utils.stop_recording_audio
    },
    Command.TAKE_SNAPSHOT: {
        'description': 'Take a picture with the webcam.',
        'method': video_utils.take_snapshot
    },
    Command.TAKE_SCREENSHOT: {
        'description': 'Take a screenshot.',
        'method': misc_utils.take_screenshot
    },
    Command.READ_CLIPBOARD: {
        'description': 'View the contents of the clipboard.',
        'method': misc_utils.get_clipboard_contents
    },
    Command.WRITE_CLIPBOARD: {
        'description': 'Write some text to the clipboard.',
        'method': misc_utils.set_clipboard_contents
    },
    Command.START_CURSOR_JUMP: {
        'description': 'Make the cursor move to random locations.',
        'method': misc_utils.start_cursor_jump
    },
    Command.SPEAK_TEXT: {
        'description': 'Enter some text to speak through the system.',
        'method': misc_utils.speak_text
    },
    Command.UPLOAD_FTP: {
        'description': 'Upload a file to an FTP server.',
        'method': ftp_utils.upload
    },
    Command.DOWNLOAD_FTP: {
        'description': 'Download a file from an FTP server.',
        'method': ftp_utils.download
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
    raise InvalidCommandError

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
    except ValueError as err:
      print(err)
    except InvalidCommandError:
      print(f'\'{command}\' is not a recognized command. Type \'help\' for ' +
      'a list of available commands.')


if __name__ == '__main__':
  begin()
