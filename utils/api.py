# Pacote python com funções de chamada de API que serão reutilizadas em varios notebooks

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


# Referencia retry + backof => https://medium.com/@bounouh.fedi/enhancing-resilience-in-python-applications-with-tenacity-a-comprehensive-guide-d92fe0e07d8

# Função que chama a API com retry + backoff 
# Em casos de exceções da biblioteca requests ocorrerar outras tentativas com intervalos de 2s, 4s, 8s, 16s e 30s
@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    retry=retry_if_exception_type((requests.exceptions.RequestException,)),
    reraise=True
)
def buscar_dados(url, params={}, encoding='utf-8'):
    resposta = requests.get(url, params=params, timeout=30)
    #Caso o valor do encoding não for informado o valor será o defaut = utf-8    
    resposta.encoding = encoding
    resposta.raise_for_status()
    return resposta.json()


# Função que Busca o Id da UF informada no parametro
def obter_estado_id_por_uf(uf):
    IBGE_ESTADO_URL =  f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/"
    dados = buscar_dados(IBGE_ESTADO_URL)
    estado_id = dados['id']
    return estado_id

