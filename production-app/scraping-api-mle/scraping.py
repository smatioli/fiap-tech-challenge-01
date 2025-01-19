from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import datetime
import re
import unicodedata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-images")

# funcao para remover acentos
def remove_accents(header):  
    return ''.join(
        c for c in unicodedata.normalize('NFD', header) if unicodedata.category(c) != 'Mn'
    )

# funcao para tratar strings
def process_string(header):  
    header = header.lower()  
    first_word = header.split()[0]    
    return remove_accents(first_word)

# funcao para substituir os caracteres * e - por 0 
def replace_characters(df, column):    
    df[column] = df[column].str.replace(r'[*-]', '0', regex=True)
    return df

# funcao para remover o caractere . dos numeros
def remove_dots(df, column):
    df[column] = df[column].str.replace('.', '', regex=False)
    return df

# funcao para encontrar os valores dos queries params
def extract_params_values(url):
    # regex para encontrar os valores entre '=' e '&'
    parametros = re.findall(r'=(.*?)(&|$)', url)
    return [parametro[0] for parametro in parametros]

# funcao para adicionar colunas necessarias no df
def add_columns(df, dict_labels):    
    if not df.empty:
        params = extract_params_values(df['url'][0])                   
        df['ano'] = params[0]
        df['opcao'] = params[1]
        if params[1] in dict_labels:
            if params[1] == 'opt_03':
                df['classificacao_uva'] = dict_labels[params[1]].get(params[2], 'Não Especificado')

                if 'sem' in df.columns:
                    df.rename(columns={'sem': 'cultivar'}, inplace=True)

            else:
                df['derivado_uva'] = dict_labels[params[1]].get(params[2], 'Não Especificado')
        df.drop('url', axis=1, inplace=True)
    return df

# funcao para obter dados do site da embrapa e retornar um dataframe
def fetch_table_data(url, driver):    
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    try:               
        content_center = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'content_center')))
        table = content_center.find_element(By.TAG_NAME, 'table')
        headers = [process_string(header.text.strip()) for header in table.find_elements(By.XPATH, ".//thead//th")]        

        table_rows = table.find_elements(By.TAG_NAME, 'tr')
        content = []
        for row in table_rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            if columns:
                content.append([col.text for col in columns])

        df = pd.DataFrame(content, columns=headers)        
        df['url'] = url
                
        return df

    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()
    
# funcao para construir todos os endpoints
def make_urls(dict_endpoints, years, url_base):
    urls = []
    for key, value in dict_endpoints.items():        
        for item in value:
            for year in years:
                url = f"{url_base}ano={year}&opcao={key}&subopcao={item}" if item.strip() else f"{url_base}ano={year}&opcao={key}"
                urls.append(url)
    return urls

# funcao para paralelizar o scraping dos dados
def fetch_data_concurrently(urls):
    results = []

    def fetch_data(url):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        result = fetch_table_data(url, driver)
        driver.quit()
        return result
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_data, url): url for url in urls}

        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Erro ao processar a URL: {futures[future]} - {e}")    
    
    return results

# funcao para conversao de data types
def convert(df, column, dtype):
    try:        
        if column not in df.columns:
            raise ValueError(f"A coluna '{column}' nao existe no datafame.")
        
        df[column] = df[column].astype(dtype)         
        return df    
    except Exception as e:
        print(f"Erro na conversao: {e}")

# funcao tratar os dados
def replace_and_convert(df, column_name, dtype):
    df = replace_characters(df, column_name)
    df = remove_dots(df, column_name)
    df = convert(df, column_name, dtype)
    return df

# funcao para processar o df com base nas colunas
def process_dataframe(df):    
    df = replace_and_convert(df, 'quantidade', int)
    df = convert(df, 'ano', int)
   
    if 'valor' in df.columns:
        df = replace_and_convert(df, 'valor', int)
    
    if 'opcao' in df.columns:
        df.drop('opcao', axis=1, inplace=True)  
        
    return df

# funcao para iterar sobre o dicionario
def process_result_dict(result_dict):
    for key, value in result_dict.items():
        df = process_dataframe(value)
        result_dict[key] = df

    return result_dict


# funcao principal que orquestra o data scraping e o processamento
def run_scrapping():    
    #years = [2022, 2023]
    years = list(range(1970, datetime.datetime.now().year-1))
    url_base = "http://vitibrasil.cnpuv.embrapa.br/index.php?"

    dict_endpoints = {
        'opt_02' : [''],        
        'opt_03' : ['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'],
        'opt_04' : [''],
        'opt_05' : ['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04', 'subopt_05'],
        'opt_06' : ['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04']
    }

    dict_labels = {
        'opt_03' : {
            'subopt_01' : 'Viníferas',
            'subopt_02' : 'Americanas e Híbridas',
            'subopt_03' : 'Uvas de Mesa',
            'subopt_04' : 'Sem Classificação',
        },
        'opt_05' : {
            'subopt_01' : 'Vinhos de Mesa',
            'subopt_02' : 'Espumantes',
            'subopt_03' : 'Uvas Frescas',
            'subopt_04' : 'Uvas Passas',
            'subopt_05' : 'Suco de Uva'
        },
        'opt_06' : {
            'subopt_01' : 'Vinhos de Mesa',
            'subopt_02' : 'Espumantes',
            'subopt_03' : 'Uvas Frescas',
            'subopt_04' : 'Suco de Uva'
        }
    }

    urls = make_urls(dict_endpoints, years, url_base)
    result = fetch_data_concurrently(urls)

    dfs = []
    for df in result:
        df = add_columns(df, dict_labels)
        dfs.append(df)

    # concatena os dataframes agrupando-os por 'opcao' ('opt_02', 'opt_03', 'opt_04', 'opt_05' ou 'opt_06')
    result_dict = {}
    for df in dfs:    
        for option, group in df.groupby('opcao'):
            # se a chave ja existe no dicionario, concatena
            if option in result_dict:
                result_dict[option] = pd.concat([result_dict[option], group], ignore_index=True)
            else:
                result_dict[option] = group

    result_dict = process_result_dict(result_dict)

    for key, value in result_dict.items():
        value.to_csv(f'app/files/{key}.csv', index=False)

    print('Processamento finalizado com sucesso')

run_scrapping()