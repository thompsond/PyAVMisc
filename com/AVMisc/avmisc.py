"""The entry point for AVMisc."""
import sys

def begin():
  """Serves as the entry method for AVMisc."""
  command_dict = {
    'exit': sys.exit
  }
  while True:
    command = input('avmisc>')
    if command in command_dict:
      command_dict[command]()
    else:
      print(f'\'{command}\' is not a recognized command. Type \'help\' for ' +
      'a list of available commands.')


if __name__ == '__main__':
  begin()
