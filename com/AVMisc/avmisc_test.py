"""Tests for avmisc.py."""

import unittest
import avmisc

class AVMiscTest(unittest.TestCase):
  def testCommandDictValidity(self):
    """Validates the entries in the command dictionary.

    Makes sure each entry in the command dictionary has a description
    and method.
    """
    for command in avmisc.COMMAND_DICT:
      self.assertIn('description', avmisc.COMMAND_DICT[command])
      self.assertIn('method', avmisc.COMMAND_DICT[command])
      self.assertNotEqual(avmisc.COMMAND_DICT[command]['description'], '')

  def testCommandEnumMatchesCommandDict(self):
    """Compares the Command enum to the command dictionary.

    Makes sure each entry in the Command enum is used in the
    command dictionary.
    """
    for command in avmisc.Command:
      self.assertIn(command, avmisc.COMMAND_DICT)

if __name__ == '__main__':
  unittest.main()
