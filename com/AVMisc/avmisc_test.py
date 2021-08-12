"""Tests for avmisc.py."""

import pytest # pylint: disable=unused-import
import avmisc

class TestAVMisc():
  def testCommandDictValidity(self):
    """Validates the entries in the command dictionary.

    Makes sure each entry in the command dictionary has a description
    and method.
    """
    for command_info in avmisc.COMMANDS.values():
      assert 'description' in command_info
      assert 'method' in command_info
      assert command_info['description'] != ''

  def testCommandEnumMatchesCommandDict(self):
    """Compares the Command enum to the command dictionary.

    Makes sure each entry in the Command enum is used in the
    command dictionary.
    """
    for command in avmisc.Command:
      assert command in avmisc.COMMANDS
