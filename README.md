# AgroClima
Projeto desenvolvido através da Trilha de Engenharia de Dados da POD Tiller 

 **Descrição:** Este projeto foi desenvolvido como parte da  trilha UPSKILL TILLER | de Engenharia de Dados e tem como objetivo principal analisar a relação entre a produção de milho e dados históricos de temperatura. A proposta envolve a coleta, o tratamento e o cruzamento de dados agrícolas e meteorológicos, buscando identificar padrões que possam impactar o rendimento das safras. 

**Configurações** Todos os notebook de extração de dados foram parametrizados para flexibilizar  a extração dos dados. Todas as API's são publicas e não nescessita de token ou API key.

#### API's Utilizadas

**1 - API de serviços agregados do IBGE** 
A API de Agregados do IBGE fornece acesso estruturado a dados estatísticos de diversas pesquisas do IBGE (como o Censo Demográfico, PNAD, IPCA, entre outras), permitindo que usuários consultem:
- Tabelas estatísticas;
- Variáveis (como população, renda, escolaridade, etc.);
- Níveis geográficos (Brasil, estados, municípios, etc.);
- Séries históricas.

Documentação: https://servicodados.ibge.gov.br/api/docs/agregados?versao=3

Enpoints utilizados: https://servicodados.ibge.gov.br/api/v3/agregados/839/periodos/{ano}/variaveis/109|216|214

Parametros:
- localidades
- classificacao

**2 - Open‑Meteo**: Essa API retorna dados históricos climáticos (com resoluções horárias e/ou diárias) para qualquer localização global, usando coordenadas geográficas (latitude/longitude) e intervalo de datas.

Documentação: https://open-meteo.com/en/docs/historical-weather-api

Enpoints utilizados: https://archive-api.open-meteo.com/v1/archive

Parametros:
- latitude
- longitude
- daily
- timezone
- start_date
- end_date

**3 - API de Localidades do IBGE**: API referente aos países e às divisões político-administrativas do Brasil bem como meso e microrregiões, institucionalizadas pela aprovação da presidência do IBGE da resolução PR nº 51/1989 e pela publicação Divisão regional do Brasil em mesorregiões e microrregiões geográficas.

Documentação: https://servicodados.ibge.gov.br/api/docs/localidades

Endpoints utilizados: https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo_estado}/municipios


**4 -  Outras Fontes**
- https://raw.githubusercontent.com/kelvins/municipios-brasileiros/main/json/municipios.json





