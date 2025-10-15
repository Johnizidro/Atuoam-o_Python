from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://pt.anotepad.com")
time.sleep(20)

titulo = driver.find_element(By.ID, "edit_title")
titulo.send_keys("Sou aluno do Senac")

conteudo = driver.find_element(By.ID, "edit_textarea")
titulo.send_keys("Teste automatizado")

time.sleep(30)

driver.quit()