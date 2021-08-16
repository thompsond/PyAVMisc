"""Tests for avmisc.py."""

import re
import pytest
import avmisc
from avmisc import Command, COMMANDS

class TestAVMisc():
  def testCommandDictIsValid(self):
    """Validates the entries in the command dictionary.

    Makes sure each entry in the command dictionary has a description
    and method. Also makes sure that each description starts with a capital
    letter and ends with a period.
    """
    for command_info in COMMANDS.values():
      assert 'description' in command_info
      assert 'method' in command_info
      assert command_info['description'] != ''
      assert re.match('[A-Z].+[.]', command_info['description']) != None

  def testCommandEnumMatchesCommandDict(self):
    """Compares the Command enum to the command dictionary.

    Makes sure each entry in the Command enum exists in the command
    dictionary and vice versa.
    """
    for command in Command:
      assert command in COMMANDS

    for command in COMMANDS:
      assert command in Command

  def testProcessCommandShouldRaiseError(self):
    with pytest.raises(ValueError):
      avmisc.process_command('foo')

  def testProcessCommandShouldNotRaiseError(self):
    try:
      avmisc.process_command(Command.LIST_ALL_AUDIO_DEVICES.value)
      assert True
    except ValueError:
      assert False, 'process_command failed unexpectedly.'
