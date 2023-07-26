#  passo a passo do projeto
# passo 01: entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui 
import time

# pyautogui.write # escrever um texto
# pyautogui.press # apertar uma tecla
# pyautogui.click # clicar em algum lugar
# pyautogui.hotkey # combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)


# passo 02: fazer login
# selecionar o campo de e-mail
pyautogui.click(x=700, y=590)
# escrever seu email
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('sua senha')
pyautogui.click(x=979, y=819)
time.sleep(3)
# teste


# passo 03: importar a base de produtos pra cadastrar
import pandas as pd
produtos = pd.read_csv('produtos.csv')
print(produtos)

#  passo 04: cadastrar um produto
#  passo 05: repetir o processo de cadastro até o fim   

for linha in produtos.index: #index = linhas colums = colunas
    print(linha)
    # clicar no campo de código:
    pyautogui.click(x=734, y=411)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = produtos.loc[linha,'codigo']
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press('tab')
    # preencher o campo
    pyautogui.write(str(produtos.loc[linha,'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha,'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha,'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha,'custo']))
    pyautogui.press('tab')
    obs = produtos.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(produtos.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter') #botao enviar

    # dar scrool de td pra cima
    pyautogui.scroll(5000)

    
