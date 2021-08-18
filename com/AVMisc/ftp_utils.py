"""A collection of methods for uploading and downloading files to and from an FTP server."""

from ftplib import FTP, error_perm
from typing import Union
import getpass

def connect_to_ftp_server() -> Union[FTP, None]:
  """Creates a connection to an FTP server.
  
  Handles login using credentials if necessary.

  Returns:
    A connection to an FTP server or None if an error occurs.
  """
  try:
    host = input('Enter the IP address or hostname of the server: ')
    need_login = input('Do you need to login? (y/n): ')
    ftp = FTP(host)
    if need_login.lower() == 'y':
      user = input('Enter the user: ')
      password = getpass.getpass('Enter the password: ')
      ftp.login(user, password)
      return ftp
    elif need_login.lower() == 'n':
      ftp.login()
      return ftp
    else:
      print('Invalid response')
      return None
  except error_perm as err:
    print(err)
    return None

def upload() -> None:
  """Uploads a file to an FTP server."""
  ftp = connect_to_ftp_server()
  if ftp is None:
    return
  try:
    welcome = ftp.getwelcome()
    print(welcome)
    local_file_path = input('Enter the local path for the file to upload: ')
    server_file_path = input('Enter the server path to upload the file: ')
    with open(local_file_path, 'rb') as fp:
      ftp.storbinary(f'STOR {server_file_path}', fp)
    print(f'File saved as {server_file_path}.')
    ftp.quit()
  except error_perm as err:
    print(err)

def download() -> None:
  """Download a file from an FTP server."""
  ftp = connect_to_ftp_server()
  if ftp is None:
    return
  try:
    welcome = ftp.getwelcome()
    print(welcome)
    server_file_path = input('Enter the server path for the file to download: ')
    local_file_path = input('Enter the local path to save the file: ')
    with open(local_file_path, 'wb') as fp:
      ftp.retrbinary(f'RETR {server_file_path}', fp.write)
    print(f'File saved as {local_file_path}.')
    ftp.quit()
  except error_perm as err:
    print(err)
