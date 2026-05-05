
"""
    Cria um novo shapefile contendo apenas as feições que correspondem
    a uma lista de logradouros fornecida em um arquivo Excel.

    Parâmetros:
        shapefile_entrada (str): Caminho do shapefile original.
        shapefile_saida (str): Caminho onde o novo shapefile será salvo.
        excel_path (str): Caminho do arquivo Excel (.xlsx).
        coluna_excel (str): Nome da coluna no Excel que contém os logradouros.
        campo_shapefile (str): Nome do campo no shapefile que será usado para correspondência.

    Exemplo de uso:
        criar_shapefile_manutencao(
            shapefile_entrada=r"C:/dados/TrechoLogradouros.shp",
            shapefile_saida=r"C:/dados/Manutencao2025.shp",
            excel_path=r"C:/dados/ListaManutencao.xlsx",
            coluna_excel="LOGRADOURO",
            campo_shapefile="NLGPAVOFIC" certo
        )
    """
import arcpy
import pandas as pd

def criar_shapefile_manutencao(shapefile_entrada, shapefile_saida, excel_path, coluna_excel, campo_shapefile):
    
    try:
        # Lê o Excel e pega os logradouros da coluna escolhida
        df = pd.read_excel(excel_path)
        valores = df[coluna_excel].dropna().unique().tolist()

        if not valores:
            print("Nenhum valor encontrado no Excel.")
            return

        # Monta a expressão SQL (campo IN ('A', 'B', 'C'))
        lista_valores = "', '".join(map(str, valores))
        expressao = f"{campo_shapefile} IN ('{lista_valores}')"

        # Executa a seleção no ArcGIS
        arcpy.Select_analysis(shapefile_entrada, shapefile_saida, expressao)

        print(f"Novo shapefile criado com sucesso em: {shapefile_saida}")

    except arcpy.ExecuteError:
        print("Erro do ArcPy:", arcpy.GetMessages(2))
    except Exception as e:
        print("Erro inesperado:", e)
