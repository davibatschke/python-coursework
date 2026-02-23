# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times_brasileirao = ('Palmeiras', 'São Paulo', 'Bahia', 'Fluminense', 'Corinthians', 
                     'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 
                     'Flamengo', 'Botafogo', 'Grêmio', 'Vitória', 'Atlético-MG', 
                     'Remo', 'Vasco da Gama', 'Santos', 'Internacional', 'Cruzeiro')

print('=-=-=[ TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL ]=-=-=\n')
print(f'-> Os 5 primeiros times presentes na tabela: {times_brasileirao[:5]}')
print(f'-> Os 4 últimos times presentes na tabela: {times_brasileirao[-4:]}')
print(f'-> Posição em que se encontra o time da Chapecoense: {times_brasileirao.index('Chapecoense') + 1}')
print(f'-> Lista dos times presentes na tabela em ordem alfabética:\n')

for time in sorted(times_brasileirao):
    print(f'-> {time}')