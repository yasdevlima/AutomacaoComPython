# Passo 1 - Entrar no sistema da empresa
# Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Automatizar 

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui # Automatizar
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5 # configuração de Pausa

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)


# Passo 2: Fazer login
pyautogui.click(x=830, y=464)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("yasmindados2024@gmail.com")


pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("12345")

pyautogui.click(x=941, y=669) # clique no botao de login

time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas 

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar 
    pyautogui.click(x=656, y=337)

    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)


    # Marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    
    # tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preco_unitario
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)


    # custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
      pyautogui.write(obs)

    # clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.write("enter")

    pyautogui.scroll(5000)

