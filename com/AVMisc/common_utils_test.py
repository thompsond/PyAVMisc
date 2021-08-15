"""Tests for common_utils.py."""

import common_utils
import pytest

class TestCommonUtils:
  def testGetFilePathShouldRaiseError(self):
    common_utils.input = lambda _: 'foo'
    with pytest.raises(FileNotFoundError):
      common_utils.get_file_path()
    common_utils.input = input


  def testGetFilePathShouldNotRaiseError(self, tmp_path):
    directory = tmp_path / 'audio'
    directory.mkdir()
    file_path = directory / 'test.wav'
    file_path.write_text('')
    common_utils.input = lambda _:  file_path
    try:
      common_utils.get_file_path()
      assert True
    except FileNotFoundError as err:
      assert False, err
    finally:
      common_utils.input = input
