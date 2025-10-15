import pyautogui
import time

print("Pressione Crtl+C para parar.")

while True:
    x,y = pyautogui.position()
    print(f"Posição Atual do Mouse: X={x}, Y={y}")
    time.sleep(0.1)