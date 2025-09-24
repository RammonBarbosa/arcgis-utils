#puxando lista de vias do arquivo excel existente
from gis_utilities import criar_shapefile_manutencao

criar_shapefile_manutencao(
    shapefile_entrada=r"C:/EsriTraning/GISA/Shapefile/TrechoLogradouros.shp",
    shapefile_saida=r"C:/EsriTraning/GISA/Shapefile/Manutencao2025.shp",
    excel_path=r"C:/EsriTraning/GISA/Shapefile/ListaManutencao2025.xlsx",
    coluna_excel="LOGRADOURO",
    campo_shapefile="NLGPAVOFIC"
)

#chamando a função para calcular extensão do shapefile
from gis_utilities.calculate_extension import calcular_extensao

shapefile = r"C:\\EsriTraning\\GISA\\Shapefile\\ManuMes22_09_2025_NOVEMBRO.shp"
calcular_extensao(shapefile)

#bloco que junta informaçoes de uma planilha excel com as informações da tabela de atributo do shapefile
#com isso consigo trazer informações extras de outras tabelas, para a tabela de atributo do shapefile
from gis_utilities.join_excel import join_excel_to_shapefile
if __name__ == "__main__":
    shp_in = r"C:\\EsriTraning\\GISA\Shapefile\\TrechoLogradouros.shp"
    excel = r"C:\\EsriTraning\\GISA\\Shapefile\\l.xlsx"
    shp_out = r"C:\\EsriTraning\\GISA\\Shapefile\\Manut23_09_2025.shp"

    resultado = join_excel_to_shapefile(
        shapefile_entrada=shp_in,
        excel_path=excel,
        shapefile_saida=shp_out,
        campo_shp="NLGPAVOFIC",
        campo_excel="LOGRADOURO",
        sheet_name="Planilha1"
    )

    print("Shapefile final criado em:", resultado)

#bloco do codigo que separa o shapefile por categoria escolhida no campo da tabela de atributos
#criando outros arquivos shapefile de acordo com a seleção do campo
from gis_utilities.select_field import select_field_by_category
if __name__ == "__main__":
    camada = "Manut22_09_2025_temp_Layer1"
    pasta_saida = r"C:\\EsriTraning\\GISA\\Shapefile"
    campo = "l.EXECUÇÃO"
    categorias = ['SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO', 
                  'JANEIRO', 'FEVEREIRO', 'MARÇO', 'PREVISTA']

    arquivos = select_field_by_category(
        camada=camada,
        pasta_saida=pasta_saida,
        campo=campo,
        categorias=categorias,
        prefixo_saida="ManuMes22_09_2025"
    )

    print("Arquivos gerados:", arquivos)