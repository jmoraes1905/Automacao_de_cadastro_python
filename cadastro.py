import pyautogui
import time

#Waiting time between commands
pyautogui.PAUSE=1
#Open web browser
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#Before writting the weblink, make sure the browser has enough time to load
time.sleep(1)
#Search for link
web_link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(web_link)
pyautogui.press("enter")

#mouse position accordind to auxiliar.py
pyautogui.click(x=1222,y=472)

email = "meuemail@provedor.com"
senha = "minhasenha"
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)  

pyautogui.press("enter")

#ignorar aviso de senha fake
pyautogui.press("enter")

import pandas as pd

tabela = pd.read_csv("produtos.csv")
#print(type(tabela))
#print(tabela)


for linha in tabela.index:
  
  pyautogui.click(x=1140,y=336)
  # Product code
  pyautogui.write(str(tabela.loc[linha,"codigo"]))
  pyautogui.press("tab")
  
  # brand
  pyautogui.write(str(tabela.loc[linha,"marca"]))
  pyautogui.press("tab")

  # type
  pyautogui.write(str(tabela.loc[linha,"tipo"]))
  pyautogui.press("tab")

  # categoria
  pyautogui.write(str(tabela.loc[linha,"categoria"]))
  pyautogui.press("tab")

   # preco
  pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
  pyautogui.press("tab")

   # custo11.0
  pyautogui.write(str(tabela.loc[linha,"custo"]))
  pyautogui.press("tab")

  # OBS
  pyautogui.write(str(tabela.loc[linha,"obs"]))
  pyautogui.press("tab")

  pyautogui.press("enter")
  pyautogui.press("up",presses=13)

print("Products inserted in database!")





