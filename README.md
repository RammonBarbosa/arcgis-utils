# arcgis_utilities
Este repositório apresenta a utilização de Python, por meio da biblioteca ArcPy, para automatizar processos no ArcGIS Pro relacionados à gestão viária. As ferramentas desenvolvidas permitem criar layers de classificação de vias, calcular extensões em metros, identificar trechos a serem sinalizados e gerar novos shapefiles a partir de categorias selecionadas. O objetivo é aprimorar a análise de dados sobre a malha viária urbana, oferecendo suporte mais ágil e preciso para estudos e tomadas de decisão.

## Objetivo
Scripts para: classificar vias, calcular de extensão em metros, gerar camadas para sinalização e exportar relatórios.

## Estrutura
📂 src/ — Código principal

    📂 gis_utilities/ ← Pacote com funções reutilizáveis

      📄 __init__.py

      📄 calculate_extension.py

      📄 join_excel.py

      📄 select_field.py

      📄 create.py

      📄 main.py

## Como rodar (local)
1. Abrir ArcGIS Pro com Python environment que inclua `arcpy`.
2. Rodar: `python src/create.py `

## Observações
- `arcpy` não pode ser instalado via pip; precisa do ArcGIS Pro.
- Dados completos não são versionados aqui (ver `data/README.md`).

