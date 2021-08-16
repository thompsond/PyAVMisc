"""A collection of methods for accessing local audio devices and info."""

from typing import Dict
import sounddevice as sd
import soundfile as sf
import common_utils

def get_simple_info(device_info: Dict) -> str:
  """Generates a simple string containing the device name and sample rate.

  Args:
    device_info: A dictionary containing device info for an audio device.
  """
  return ('Name: %s, Sample Rate: %s' %
         (device_info['name'], device_info['default_samplerate']))

def list_default_devices() -> None:
  """Lists the default audio devices on the system."""
  input_device_info = get_simple_info(sd.query_devices(kind='input'))
  output_device_info = get_simple_info(sd.query_devices(kind='output'))
  print('DEFAULT INPUT DEVICE:\n'
        f'{input_device_info}\n\n'
        'DEFAULT OUTPUT DEVICE:\n'
        f'{output_device_info}')

def list_all_devices() -> None:
  """Lists all audio devices on the system."""
  print(sd.query_devices())

def play_audio_file() -> None:
  """Plays an audio file if it exists."""
  try:
    filename = common_utils.get_file_path()
    data, fs = sf.read(filename)
    sd.play(data, fs)
  except FileNotFoundError as err:
    print(err)

def stop_playing_audio() -> None:
  """Stops playing audio."""
  sd.stop()
