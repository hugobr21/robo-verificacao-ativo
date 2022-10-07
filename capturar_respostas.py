from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import pandas as pd
import logging
import time
import json

def carregarParametros():
    with open("parametros.json", "r") as infile:
        parametros = json.load(infile)
    return parametros

profile_path = r'C:\Users\vdiassob\AppData\Roaming\Mozilla\Firefox\Profiles\eituekku.robo'
options = Options()
options.add_argument("-profile")
options.add_argument(profile_path)
options.binary_location = carregarParametros()["caminhonavegador"]

driver = webdriver.Firefox(options=options)
time.sleep(7)
driver.get('https://web.whatsapp.com/')
os.system('pause')

def baixarMensagens():
    conversa = driver.find_elements(By.CLASS_NAME, 'copyable-text')
    for indice,mensagens in zip(range(len(conversa)),conversa):
        if mensagens.get_attribute('data-pre-plain-text') != None:
            print(indice, mensagens.get_attribute('data-pre-plain-text'),mensagens.text)

baixarMensagens()
