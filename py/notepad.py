import pyautogui
import time
import subprocess

subprocess.Popen('notepad.exe')
time.sleep(2)

pyautogui.write('Ola, teste automatizado', interval=0.1)

