import pyautogui
import time
import subprocess

subprocess.Popen('notepad.exe')
time.sleep(3)

pyautogui.write('Ola, estou fazendo um teste automatizado para testar a funciolalidade de abertura e salvamento do arquivo', interval=0.2)

time.sleep(2)

pyautogui.hotkey('ctrl' , 's')

time.sleep(1)

pyautogui.write('Minha_Nota')

pyautogui.press('enter')

time.sleep(2)

pyautogui.hotkey('alt','f4')

