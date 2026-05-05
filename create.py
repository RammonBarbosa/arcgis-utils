#Esse bloco do codigo abre um arquivo excel
#Ler um campo(coluna) escolhido(ruas)
#Faz outro shapefile a partir de outro shapefile(trecho e lougradouro) de acordo com o campo em comum



import arcpy
import pandas as pd
import os

# Caminhos
shapefile_entrada = r"C:\EsriTraning\GISA\Shapefile\TrechoLogradouros.shp"
shapefile_saida = r"C:\EsriTraning\GISA\Shapefile\l4Recap2025.shp"
excel_path = r"C:\EsriTraning\GISA\Shapefile\rcp4.xlsx"

# Lê o Excel e pega a coluna "NOME_RUA" como lista
df = pd.read_excel(excel_path)
ruas = df["LOGRADOURO"].dropna().tolist()  # remove valores nulos

# Monta a expressão SQL usando IN
lista_ruas = "', '".join(ruas)
expressao = f"NLGPAVOFIC IN ('{lista_ruas}')"

# Executa a seleção
arcpy.Select_analysis(shapefile_entrada, shapefile_saida, expressao)

print("Novo shapefile criado com sucesso em:", shapefile_saida)
