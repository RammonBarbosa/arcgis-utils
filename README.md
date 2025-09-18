# utilidades_arcgis
Este repositório apresenta a utilização de Python, por meio da biblioteca ArcPy, para automatizar processos no ArcGIS Pro relacionados à gestão viária. As ferramentas desenvolvidas permitem criar layers de classificação de vias, calcular extensões em metros, identificar trechos a serem sinalizados e gerar novos shapefiles a partir de categorias selecionadas. O objetivo é aprimorar a análise de dados sobre a malha viária urbana, oferecendo suporte mais ágil e preciso para estudos e tomadas de decisão.

## Objetivo
Scripts para: classificar vias, calcular de extensão em metros, gerar camadas para sinalização e exportar relatórios.

## Estrutura
📂 src/ — Código principal

  📂 ARCPY/

    📂 gis_utils/ ← Pacote com funções reutilizáveis

      📄 __init__.py

      📄 calcular_metragem.py

      📄 campos_excel.py

      📄 selecao_excel.py

      📄 main.py

📂 data/ — Dados de exemplo (usar apenas amostra; ver observações)

📂 docs/ — Screenshots e instruções

📄 requirements.txt — Bibliotecas Python (exceto arcpy)

## Como rodar (local)
1. Abrir ArcGIS Pro com Python environment que inclua `arcpy`.
2. Rodar: `python src/classificar_vias.py --input data/exemplo.shp --output data/output.shp`

## Observações
- `arcpy` não pode ser instalado via pip; precisa do ArcGIS Pro.
- Dados completos não são versionados aqui (ver `data/README.md`).

