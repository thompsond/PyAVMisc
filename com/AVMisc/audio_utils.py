"""A collection of methods for accessing local audio devices and info."""

from typing import Dict
import multiprocessing
import sounddevice as sd
import soundfile as sf
import common_utils

_recording_audio_process = None

def _record_audio(duration: int) -> None:
  """Record audio using the microphone.

  Args:
    duration: The recording time in seconds.
  """
  filename = f'Audio_{common_utils.get_formatted_date()}.wav'
  samplerate = sd.query_devices(kind='input')['default_samplerate']
  recording = sd.rec(int(duration * samplerate), channels=2)
  sd.wait()
  sf.write(filename, recording, samplerate=int(samplerate))
  print(f'Recording saved as {filename}')
  global _recording_audio_process
  _recording_audio_process = None

def start_recording_audio() -> None:
  """Create the process for recording audio."""
  duration = int(input('Enter the recording time in seconds: '))
  global _recording_audio_process
  _recording_audio_process = multiprocessing.Process(target=_record_audio,
                                                    args=(duration, ))
  _recording_audio_process.start()

def stop_recording_audio() -> None:
  global _recording_audio_process
  if _recording_audio_process is not None:
    _recording_audio_process.terminate()
    _recording_audio_process = None

def get_simple_info(device_info: Dict) -> str:
  """Generates a simple string containing the device name and sample rate.

  Args:
    device_info: A dictionary containing device info for an audio device.
  """
  return (
    f"Name: {device_info['name']}"
    f"Sample Rate: {device_info['default_samplerate']}"
  )

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
