from processamento_dados import Dados

# Configurações

path_json = '/home/felipeguimaraes/Documentos/pipeline_dados/data_raw/dados_empresaA.json'
path_csv = '/home/felipeguimaraes/Documentos/pipeline_dados/data_raw/dados_empresaB.csv'

dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

# Iniciando a leitura

print(f"Número de linhas da empresa A: {dados_empresaA.qtd_linhas}")
print(f"Número de linhas da empresa B: {dados_empresaB.qtd_linhas}")

# Transformação dos dados

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Número de linhas da fusão: {dados_fusao.qtd_linhas}")

# Load

path_dados_combinados = '/home/felipeguimaraes/Documentos/pipeline_dados/data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Sucesso! Seus dados foram salvos na pasta {path_dados_combinados}")
