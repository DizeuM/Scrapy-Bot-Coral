from __future__ import print_function
from pprint import pprint
from pydoc import pager
from webbrowser import get
from numpy import tile
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from time import sleep




link = "https://www.armazemcoral.com.br"

options = webdriver.ChromeOptions()
options.headless = True

#headless ou não

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

driver.set_window_size(1300, 800)
driver.get(link)


lista_categorias = []
lista_subcategoria = []
lista_nomes = []

errocat = []

def PUXADADO():
    
    nomecat = driver.find_element(By.XPATH, 
                                  '/html/body/div[2]/div[1]/div/div[1]/div/h1')
    nomecat = nomecat.text
    

    tituloabasolo = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/ul/li[1]/a').text
    
    print(nomecat)
    
    if  tituloabasolo == nomecat:

        try: 
            
            numloop = 2
            
            for x in range(20):
                
                vercatnum = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/ul/li[{numloop}]/a')
                numloop += 1
            
        except:
            pass
        
        linha = 2

        urlcat = driver.current_url
        
        for i in range(numloop - 2):
            
            sleep(1)
            
            subcat = driver.find_element(By.XPATH, 
                                         f'/html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/ul/li[{linha}]/a')
            subcat.click()
            
            sleep(2)
            
            nomesubcat = driver.find_element(By.XPATH, 
                                  '/html/body/div[2]/div[1]/div/div[1]/div/h1')
            nomesubcat = nomesubcat.text


            numeroprodutospag = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div[4]/label').text
            numeroprodutospag = s_nums = "".join([ch for ch in numeroprodutospag if ch.isdigit()])
            numeroprodutospag = int(numeroprodutospag)
                
            # print(numeroprodutospag)
            
            if numeroprodutospag > 30:
                
                scroll = int(numeroprodutospag/30)
                
                for s in range(scroll):
                    
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(3)

            item = 1 
            pag = 1
            produtnum = 1
            
            for i in range(numeroprodutospag):

                if item > 32:
                    
                    item = 1
                    pag += 1
                        
                try:
                    
                    nome_produto = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div[{pag}]/div/div[{item}]/div/div[1]/div[3]/div[1]/a').text
                    
                except:
                    
                    try: 
            
                        nome_produto = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/div[2]/div[{pag}]/div/div[{item}]/div/div[1]/div[3]/div[1]/a').text
                    except:
                        try:
                            
                            nome_produto = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div[{item}]/div/div[1]/div[3]/div[1]/a').text
                        except:
                            try:
                                
                                nome_produto = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div[{item}]/div/div[1]/div[3]/div[1]/a').text
                            except:
                                try:
                                
                                    nome_produto = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/div[2]/div[{item}]/div/div/div/div[1]/div[3]/div[1]/a').text
                                except:
                                    pass
                        
                lista_nomes.append(nome_produto)
                lista_categorias.append(nomecat)
                lista_subcategoria.append(nomesubcat)
                
                
                # print(str(produtnum) + " " + nome_produto)
                
                item += 1
                produtnum += 1
                
            print(" " + nomesubcat)    
                
            print("")
            sleep(2)
            
            linha += 1
            
            driver.get(f"{urlcat}")
            



                        
     


#cria uma planilha para cada categoria do menu

def PLANILHA():
    
    columns = ["Nome", "Categoria", "Subcategoria"]
    rows = list(zip(lista_nomes, lista_categorias, lista_subcategoria))

    dadosnum = pd.DataFrame(rows, columns=columns)
    # print(dadosnum)
    dadosnum.to_excel(f"categorias{plan}.xlsx", index = False)


sleep(2)

plan = 1

for x in range(1):
    
    
    #especifica o numero de colunas e linhas do menu principal
    
    col = 2
    
    cat = 10

    for x in range(1):
        
        menu = driver.find_element(By.XPATH, 
                                '/html/body/div[2]/header[2]/div/div[3]/div/div/div/div[1]/ul/li[1]/a/div/i[1]')

        categ = driver.find_element(By.XPATH, 
                                    f'/html/body/div[2]/header[2]/div/div[3]/div/div/div/div[1]/ul/li[1]/div/div/div/div/div[{col}]/ul/li/ul/li[{cat}]/a')
        
        ActionChains(driver).move_to_element(menu).click(menu).perform()
        sleep(0.3)
        ActionChains(driver).move_to_element(categ).click(categ).perform()
        sleep(0.3)
        
        print(cat)
        PUXADADO()
        PLANILHA()
        
        
        plan += 1
        
        cat += 1
    
    col += 1
    

