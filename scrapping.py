
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

os.environ['GH_TOKEN'] = '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'
records = []
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

def obter_situacoes(driver, opcao):
    celula = 5 if opcao == 1 else 6
    td = 'tex3' if opcao == 2 else 'tex3a'

    driver.get(f'http://comprasnet.gov.br/acesso.asp?url=/livre/Pregao/lista_pregao_filtro.asp?Opc={opcao}')

    element = driver.find_element(By.NAME, 'main2')
    driver.switch_to.frame(element)
    element = driver.find_element(By.ID, 'lstSituacao')

    select = Select(driver.find_element(By.ID, 'lstSituacao'))
    select.select_by_visible_text('Todas')

    input = driver.find_element(By.ID, 'co_uasg')
    input.send_keys('910813')

    element = driver.find_element(By.ID, 'ok')
    element.click()


    table = driver.find_element(By.CLASS_NAME, 'td')
    for row in table.find_elements(By.CLASS_NAME, f'{td}'):
        pregao = row.find_element(By.TAG_NAME,'a').text
        situacao = row.find_element(By.CSS_SELECTOR, f'td:nth-child({celula})').text
        records.append({"pregao_id": pregao, "situacao": situacao})

obter_situacoes(driver, 0)
obter_situacoes(driver, 1)
obter_situacoes(driver, 2)

for pregao in records:
    print(pregao)
print(len(records))

#driver.close()
#driver.quit()
