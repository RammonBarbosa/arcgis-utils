
#Função para calcular a extensão de um shapefile
"""
    Calcula a extensão (comprimento) de feições lineares em um shapefile.
    
    shapefile: caminho do shapefile ou feature class
    campo_metragem: nome do campo que receberá a metragem
    """
import arcpy
def calcular_extensao(shapefile, campo_metragem="EXTENSAO"):
    
    # Verifica se o campo já existe; se não, cria
    campos = [f.name for f in arcpy.ListFields(shapefile)]
    if campo_metragem not in campos:
        arcpy.management.AddField(shapefile, campo_metragem, "DOUBLE")

    # Calcula o comprimento em METROS
    arcpy.management.CalculateGeometryAttributes(
        shapefile,
        [[campo_metragem, "LENGTH_GEODESIC"]],
        length_unit="METERS"
    )

    print(f"Extensão calculada no campo {campo_metragem} para {shapefile}")