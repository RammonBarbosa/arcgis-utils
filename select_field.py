
""" Separa uma camada em shapefiles diferentes com base em categorias de um campo de sua tabela de atributo.

    Args:
        camada (str): Caminho ou nome da camada (pode ser a layer ativa no ArcGIS Pro).
        pasta_saida (str): Pasta onde serão salvos os shapefiles resultantes.
        campo (str): Nome do campo a ser usado para filtro (atenção ao prefixo em joins).
        categorias (list[str]): Lista de categorias (valores) a filtrar.
        prefixo_saida (str): Prefixo para nomear os arquivos de saída. Default: "Resultado".

    Returns:
        list[str]: Lista com os caminhos completos dos shapefiles gerados.
    """

import arcpy
import os

def select_field_by_category(
    camada: str,
    pasta_saida: str,
    campo: str,
    categorias: list[str],
    prefixo_saida: str = "Resultado"
) -> list[str]:
   
    arcpy.env.overwriteOutput = True
    saidas = []

    for cat in categorias:
        shapefile_saida = os.path.join(pasta_saida, f"{prefixo_saida}_{cat}.shp")
        expressao = f"\"{campo}\" = '{cat}'"
        arcpy.Select_analysis(camada, shapefile_saida, expressao)
        print(f"✅ Shapefile criado: {shapefile_saida}")
        saidas.append(shapefile_saida)

    return saidas