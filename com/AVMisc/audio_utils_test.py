"""Tests for audio_utils.py."""
# Figure out how to mock query_devices()

import pytest # pylint: disable=unused-import
import audio_utils

DEVICE_NAME_1 = 'Device 1'
DEVICE_NAME_2 = 'Device 2'
DEFAULT_SAMPLE_RATE_1 = 45.0
DEFAULT_SAMPLE_RATE_2 = 100.0
INPUT_DEVICE_INFO = {
  'name': DEVICE_NAME_1,
  'default_samplerate': DEFAULT_SAMPLE_RATE_1
}
OUTPUT_DEVICE_INFO = {
  'name': DEVICE_NAME_2,
  'default_samplerate': DEFAULT_SAMPLE_RATE_2
}

def fake_query_devices(kind):
  if kind == 'input':
    return INPUT_DEVICE_INFO
  elif kind == 'output':
    return OUTPUT_DEVICE_INFO

class TestAudioUtils():
  def testGetSimpleInfo(self):
    """Make sure get_simple_info parses correctly."""
    actual = audio_utils.get_simple_info(INPUT_DEVICE_INFO)
    expected = f'Name: {DEVICE_NAME_1}, Sample Rate: {DEFAULT_SAMPLE_RATE_1}'
    assert actual == expected

  def testListDefaultDevices(self, mocker):
    mock_sounddevice = mocker.MagicMock(name='mock_snd_device')
    mock_sounddevice.query_devices.side_effect = fake_query_devices
    mocker.patch('audio_utils.sd', new=mock_sounddevice)
    audio_utils.list_default_devices()
    mock_sounddevice.query_devices.assert_has_calls(
        [mocker.call(kind='input'),
         mocker.call(kind='output')])
