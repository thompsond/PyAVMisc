"""Tests for avmisc.py."""

import pytest
import avmisc

class TestAVMisc():
  def testCommandDictValidity(self):
    """Validates the entries in the command dictionary.

    Makes sure each entry in the command dictionary has a description
    and method.
    """
    for command in avmisc.COMMAND_DICT:
      assert 'description' in avmisc.COMMAND_DICT[command]
      assert 'method' in avmisc.COMMAND_DICT[command]
      assert avmisc.COMMAND_DICT[command]['description'] != ''

  def testCommandEnumMatchesCommandDict(self):
    """Compares the Command enum to the command dictionary.

    Makes sure each entry in the Command enum is used in the
    command dictionary.
    """
    for command in avmisc.Command:
      assert command in avmisc.COMMAND_DICT
