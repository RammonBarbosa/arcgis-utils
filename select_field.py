import arcpy
import os

def select_field(camada, pasta_saida, campo, categorias):
# Camada resultante do join (layer ativo no ArcGIS Pro)
    camada = "Manut22_09_2025_temp_Layer1"

# Pasta de saída
    pasta_saida = r"C:\\EsriTraning\\GISA\\Shapefile"

# Campo correto (com prefixo do Excel)
    campo = "ListaManutenção2025.EXECUÇÃO"

# Lista de meses que você quer separar
    categorias = ['SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO', 'JANEIRO', 'FEVEREIRO', 'MARÇO', 'PREVISTA']

# Permite sobrescrita
    arcpy.env.overwriteOutput = True  

for cat in categorias:
    shapefile_saida = os.path.join(pasta_saida, f"ManuMes22_09_2025_{cat}.shp")
    
    # Expressão SQL (campo prefixado + valor)
    expressao = f"\"{campo}\" = '{cat}'"
    
    # Seleção
    arcpy.Select_analysis(camada, shapefile_saida, expressao)
    print(f"✅ Shapefile criado: {shapefile_saida}")