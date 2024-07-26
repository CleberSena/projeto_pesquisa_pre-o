from selenium.common.exceptions import *
import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
import random
import openpyxl
import os

def inicializacao_do_bot():
    print(f'\033[1;34m<=>'*15)
    print('\033[33m      Iniciando o Bot')
    print(f'\033[1;34m<=>\033[;m'*15)
def iniciarDriver():
    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU    
    '''
    arguments = ['--lang=pt-br', '--window-size=1200,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,        
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    
    driver = webdriver.Chrome(options = chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

def criarPlanilha(produto, data, valorAtual, linkProduto):
    workbook = openpyxl.Workbook()
    del workbook['Sheet']
    workbook.create_sheet('Iphone 15 Pro Max')
    sheet_ifone = workbook['Iphone 15 Pro Max']
    sheet_ifone.append(['Produto', 'Data', 'Valor Atual', 'Link do Produto'])
    sheet_ifone.append([produto, data, valorAtual, linkProduto])
    workbook.save('preçosIfone15.xlsx') 

def intervalo():
    for v in range(30, -1, -1):
        if v >=20:        
            pausa = print(f'\033[36mBot Pausado! Novas Pesquisa daqui a \33[1;37m{v}\033[;36m minutos')
            sl(60)
            os.system('cls')
        elif v >= 10:
            pausa = print(f'\033[36mBot Pausado! Novas Pesquisa daqui a \33[1;33m{v}\033[;36m minutos')
            sl(60)
            os.system('cls')
        elif v > 1:
            pausa = print(f'\033[36mBot Pausado! Novas Pesquisa daqui a \33[1;32m{v}\033[;36m minutos')
            sl(60)
            os.system('cls')
        else:
            for v in range(60, -1, -1):
                pausa = print(f'\033[32mBot Pausado! Novas Pesquisa daqui a \33[1;31m{v}\033[;32m minutos')
                sl(1)
                os.system('cls') 
            break


