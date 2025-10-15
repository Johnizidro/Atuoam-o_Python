import pyautogui
import time

time.sleep(2)

pyautogui.hotkey('win','d')

time.sleep(2)

pyautogui.hotkey('ctrl','shift', 'n')

pyautogui.write('Minha_Pasta',interval=0.2)

pyautogui.press('enter')


pyautogui.doubleClick(x=337, y=331)

time.sleep(2)

pyautogui.rightClick(x=870, y=680)

pyautogui.click(x=796, y=984)

pyautogui.click(x=928, y=940)

pyautogui.write('Minha_Nota',interval=0.2)

pyautogui.press('enter')

time.sleep(3)

pyautogui.doubleClick(x=576, y=557)

time.sleep(1)

pyautogui.write('Acabei',interval=0.2)

pyautogui.hotkey('ctrl','s')

pyautogui.hotkey('alt','f4')