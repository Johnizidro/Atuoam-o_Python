import pyautogui
import time
import pyperclip

pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(5)

pyperclip.copy('https://www.youtube.com/')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(10)

pyautogui.click(600, 1075)
pyperclip.copy('Senac')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

