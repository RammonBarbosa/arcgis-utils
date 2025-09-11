# Arcgis_Vias_Recife
Utilização de python para automatizar funcionalidade do ArcGIS Pro por meio da biblioteca Arcpy, para criação de layers de classificação de vias, calculo de extensão em metros e identificação de vias a sinalizar.

## Objetivo
Scripts para: classificar vias, calcular de extensão em metros, gerar camadas para sinalização e exportar relatórios.

## Estrutura
- `src/` — scripts Python (classificar_vias.py, sinalizacao_vias.py, utils.py)
- `data/` — dados de exemplo (usar apenas amostra; ver observações)
- `docs/` — screenshots e instruções
- `requirements.txt` — libs Python (exceto arcpy)

## Como rodar (local)
1. Abrir ArcGIS Pro com Python environment que inclua `arcpy`.
2. Rodar: `python src/classificar_vias.py --input data/exemplo.shp --output data/output.shp`

## Observações
- `arcpy` não pode ser instalado via pip; precisa do ArcGIS Pro.
- Dados completos não são versionados aqui (ver `data/README.md`).

