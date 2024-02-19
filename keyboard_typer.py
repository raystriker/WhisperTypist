import subprocess
from getpass import getpass


def type_text(text):
    """
    This function types the given text using ydotool.
    :param text: The text to be typed
    :return: None
    """
    command = f'sudo ./ydotool type "{text}"'
    subprocess.run(command, shell=True)


def type_text_init():
    """
    A function to initialize typing, using ydotool and subprocess, with a password prompt for sudo access.
    """
    password = getpass("Enter your password: ")
    command = 'sudo -S ./ydotool type ""'
    subprocess.run(command, shell=True, input=password.encode())
