from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://automatizado.netlify.app")
time.sleep(3)

driver.maximize_window()
time.sleep(3)

input_nome = driver.find_element(By.ID, 'nome')
input_nome.send_keys("João Victor")
time.sleep(2)

input_email = driver.find_element(By.ID, 'email')
input_email .send_keys("joaovictor@gmail.com")
time.sleep(2)

input_telefone = driver.find_element(By.ID, 'telefone')
input_telefone .send_keys("19999999999")
time.sleep(2)

input_nascimento = driver.find_element(By.ID, 'nascimento')
input_nascimento .send_keys("12032009")
time.sleep(2)

input_cpf = driver.find_element(By.ID, 'cpf')
input_cpf .send_keys("99999999999")
time.sleep(2)

input_cep = driver.find_element(By.ID, 'cep')
input_cep .send_keys("99999999")
time.sleep(2)

input_endereco = driver.find_element(By.ID, 'endereco')
input_endereco.send_keys("Rua 123, Avenida slq das quantas")
time.sleep(2)

input_cidade = driver.find_element(By.ID, 'cidade')
input_cidade.send_keys("São Paulo")
time.sleep(2)

input_estado = driver.find_element(By.ID, 'estado')

for _ in range(25):
    input_estado.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)  # Pequena pausa entre os arrow downs (ajuste se quiser)

input_estado.send_keys(Keys.ENTER)
time.sleep(2)


input_observacoes = driver.find_element(By.ID, 'observacoes')
input_observacoes.send_keys("Nehuma observação")
time.sleep(3)

input_salvar = driver.find_element(By.TAG_NAME, 'button')
input_salvar.send_keys(Keys.ENTER)

time.sleep(8)

input_salvar.send_keys(Keys.ENTER)

time.sleep(2)

driver.quit()
