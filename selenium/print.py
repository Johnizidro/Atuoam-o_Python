from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.python.org")
time.sleep(3)

driver.save_screenshot("site.png")

driver.quit()