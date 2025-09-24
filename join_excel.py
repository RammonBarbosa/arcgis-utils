#Função para juntar informações de tabelas excel
#Tabela de atributos > Tabela Excel
"""
    Faz join entre shapefile e planilha Excel para trazer informações adicionais.

    Args:
        shapefile_entrada (str): Caminho do shapefile de entrada.
        excel_path (str): Caminho do arquivo Excel.
        shapefile_saida (str): Caminho do shapefile final de saída.
        campo_shp (str): Nome do campo no shapefile para fazer join.
        campo_excel (str): Nome do campo no Excel para fazer join.
        sheet_name (str): Nome da planilha no Excel (default: "Planilha1").
    """
import arcpy
import pandas as pd

def join_excel_to_shapefile(
    shapefile_entrada: str,
    excel_path: str,
    shapefile_saida: str,
    campo_shp: str,
    campo_excel: str,
    sheet_name: str = "Planilha1"
):

    #Shapefile temporário
    shapefile_temp = shapefile_saida.replace(".shp", "_temp.shp")

    #Converte Excel para DBF
    tabela_excel = excel_path.replace(".xlsx", ".dbf")
    arcpy.conversion.ExcelToTable(excel_path, tabela_excel, sheet_name)

    #Lê os valores de ruas
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    ruas = df[campo_excel].dropna().unique().tolist()
    lista_ruas = "', '".join(ruas)
    expressao = f"{campo_shp} IN ('{lista_ruas}')"

    #Seleciona os registros do shapefile
    arcpy.Select_analysis(shapefile_entrada, shapefile_temp, expressao)

    #Faz join com Excel
    arcpy.management.AddJoin(shapefile_temp, campo_shp, tabela_excel, campo_excel)

    #Exporta para shapefile final
    arcpy.management.CopyFeatures(shapefile_temp, shapefile_saida)

    return shapefile_saida