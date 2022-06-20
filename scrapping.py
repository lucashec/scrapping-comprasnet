

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def obter_situacoes(driver, opcao = 0, cod_uasg='910813'):
    records = []
    try:
        celula = 5 if opcao == 1 else 6
        td = 'tex3' if opcao == 2 else 'tex3a'

        driver.get(f'http://comprasnet.gov.br/acesso.asp?url=/livre/Pregao/lista_pregao_filtro.asp?Opc={opcao}')

        element = driver.find_element(By.NAME, 'main2')
        driver.switch_to.frame(element)
        element = driver.find_element(By.ID, 'lstSituacao')

        select = Select(driver.find_element(By.ID, 'lstSituacao'))
        select.select_by_visible_text('Todas')

        input = driver.find_element(By.ID, 'co_uasg')
        input.send_keys(f'{cod_uasg}')

        element = driver.find_element(By.ID, 'ok')
        element.click()

        table = driver.find_element(By.CLASS_NAME, 'td')
        for row in table.find_elements(By.CLASS_NAME, f'{td}'):
            pregao = row.find_element(By.TAG_NAME,'a').text
            situacao = row.find_element(By.CSS_SELECTOR, f'td:nth-child({celula})').text
            records.append({"pregao_id": pregao, "situacao": situacao})
        return records
    except:
        raise('Erro ao obter dados do compras.gov.br')
        
