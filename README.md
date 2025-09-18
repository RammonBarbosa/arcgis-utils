# utilidades_arcgis
Utilização de python para automatizar funcionalidade do ArcGIS Pro por meio da biblioteca Arcpy, para criação de layers de classificação de vias, calculo de extensão em metros, identificação de vias a sinalizar e criação de novos shapefiles de acordo com categoria escolhida.

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

