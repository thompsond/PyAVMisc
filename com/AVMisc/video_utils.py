"""A collection of methods for accessing local video devices and info."""

import cv2
from common_utils import get_formatted_date


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
