#Como cirar uma automação

#Acessar o netflix, colocar o login e senha, apertar no entrar e escolher o usuário que irá ver o filme

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#Iniciar o webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#1 - Navegar até o site https://store.steampowered.com/login/?redir=%3Fl%3Dportuguese&redir_ssl=1&snr=1_4_4__global-header

driver.get('https://www.netflix.com/br/login')

#Encontrar os elementos na página
#2 - Clicar no campo de e-mail

campo_email = driver.find_element(By.CLASS_NAME,'placeLabel') #Achar o elemento             
campo_email.click() #Clicar no elemento
campo_email = driver.find_element(By.ID,'id_userLoginId')
campo_email.click()


#3 - Digitar um e-mail

campo_email.send_keys('rafa10rafa1@hotmail.com')
sleep(2)

#4 - Clicar no campo senha

campo_senha = driver.find_element(By.ID,'id_password')
campo_senha.click()


#5 - Digitar uma senha

campo_senha.send_keys('231605')
sleep(2)

#6-Apertar o botão, encontrar o campo através do xpath

campo_botao = driver.find_element(By.XPATH,"//button[@data-uia='login-submit-button']")
campo_botao.click()
sleep(2)

driver.get('https://www.netflix.com/browse')
sleep(2)

campo_usuario = driver.find_element(By.XPATH,"//div[@data-profile-guid='VDQOT2W42REWVDJGBLXFDXZISM']")
campo_usuario.click()

input()