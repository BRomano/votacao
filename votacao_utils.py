import pandas as pd

headers = dict()
headers[2010] = headers[2008] = ['DATA_GERACAO', 'HORA_GERACAO', 'ANO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF', 'SIGLA_UE', 'MUN_COD', 'MUN_NOME', 'NUM_ZONA',
                     'NUM_SECAO', 'CARGO_COD', 'CARGO_DESC', 'NUM_VOTAVEL', 'QTD_VOTOS']

unused_columns = dict()
unused_columns[2010] = unused_columns[2008] = [0, 1, 2, 4, 5, 8, 12]


def load_data_votacao(file):
    secao = pd.read_csv(file, encoding='latin1', sep=';')

    year = secao.loc[0][2]
    secao_headers = []
    secao_headers = headers[year]

    if len(secao_headers) <= 0:
        Exception('Ano nao configurado')

    secao.columns = secao_headers
    secao.drop(secao.columns[unused_columns[year]], axis=1, inplace=True)
    return secao

#resultado = load_data_votacao('dados/votacao_secao_2010_PR.txt')
#resultado.head(5)
