"""A collection of methods for accessing local video devices and info."""

import multiprocessing
import cv2
from common_utils import get_formatted_date

_recording_video_process = None

def take_snapshot() -> None:
  """Take a photo with the webcam."""
  video_capture = cv2.VideoCapture(0)
  try:
    _, frame = video_capture.read()
    filename = f'Snapshot_{get_formatted_date()}.png'
    cv2.imwrite(filename, frame)
    print(f'Snapshot saved as {filename}.')
  except cv2.error as err:
    print(err)
  finally:
    video_capture.release()

def _record_video(duration: int) -> None:
  """Record video using the webcam.

  Args:
    duration: The recording time in seconds.
  """
  fps = 25
  filename = f'Video_{get_formatted_date()}.avi'
  video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  out = cv2.VideoWriter(filename,
                        cv2.VideoWriter_fourcc(*'XVID'),
                        fps,
                        (640, 480)
                       )
  try:
    remaining_frames = duration * fps
    while remaining_frames > 0:
      ret, frame = video_capture.read()
      if ret:
        out.write(frame)
        remaining_frames -= 1
      else:
        break
    print(f'Video saved as {filename}.')
  except cv2.error as err:
    print(err)
  finally:
    video_capture.release()
    out.release()
    global _recording_video_process
    _recording_video_process = None

def start_video_record() -> None:
  """Create the process for recording video."""
  duration = int(input('Enter the recording time in seconds: '))
  global _recording_video_process
  _recording_video_process = multiprocessing.Process(target=_record_video,
                                                     args=(duration, ))
  _recording_video_process.start()

def stop_recording_video() -> None:
  global _recording_video_process
  if _recording_video_process is not None:
    _recording_video_process.terminate()
    _recording_video_process = None
