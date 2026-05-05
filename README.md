# ArcGIS Utilities: Automação para Gestão Viária
Este repositório apresenta a utilização de Python, por meio da biblioteca ArcPy, para automatizar processos no ArcGIS Pro relacionados à gestão viária urbana. As ferramentas desenvolvidas permitem a criação de camadas a partir de bases oficiais, cálculos de extensão e processamento de dados para suporte à tomada de decisão.

## Objetivo e Contexto
A lógica por trás do script nasceu da necessidade de demonstrar em quais vias da cidade o órgão fiscalizador atua. Desenhar polilinha por polilinha, representando cada via com manutenção de sinalização prevista, demandaria um tempo excessivo.

A Solução: O projeto utiliza um arquivo shapefile base da prefeitura e, por meio de uma planilha (Excel) de programação, identifica e extrai automaticamente as vias correspondentes para a criação de um novo shapefile, desenhando-as de forma automática no mapa.

## Funcionalidades
Classificação de vias: Identifica trechos a serem sinalizados.

Geração de Layers: Cria novos shapefiles a partir de categorias selecionadas.

Cálculo de Engenharia: Mede extensões em metros de forma automatizada.

Exportação: Gera relatórios e camadas prontas para análise.

## Estrutura do Projeto
O código é organizado de forma modular para facilitar a manutenção:

📂 src/
    📂 gis_utilities/            # Pacote com funções reutilizáveis
        📄 __init__.py
        📄 calculate_extension.py # Cálculos de métricas (metros)
        📄 join_excel.py          # União de dados externos (Excel)
        📄 select_field.py        # Filtros por categoria/mês
        📄 create.py              # Script principal de criação/extração
        📄 main.py                # Orquestrador do fluxo

## Como rodar (local)
Certifique-se de possuir o ArcGIS Pro instalado (necessário para a biblioteca arcpy).

Utilize o ambiente Python padrão do ArcGIS Pro (arcgispro-py3).

Execute o script principal:

Bash
python src/gis_utilities/main.py

## Próximos Passos (Roadmap)
Atualmente o projeto foca em correspondências exatas, mas o plano de evolução inclui:

[ ] Tratamento de Dados: Implementação de lógica via Fuzzy Matching para tratar divergências em nomes de logradouros e reduzir revisões manuais.

[ ] Visualização: Integração direta com dashboards do ArcGIS Online para monitoramento da gestão viária em tempo real.

## Observações
A biblioteca arcpy é proprietária e exige o ArcGIS Pro instalado.

Dados sensíveis ou volumosos não são versionados neste repositório.