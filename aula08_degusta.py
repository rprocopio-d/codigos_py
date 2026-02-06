import random

# 1) Gerar Dados
def gerar_dados(qtd, minimo, maximo):
    '''
    Gera uma lista com 'qtd' números inteiros
    pseudo aleatórios entre o mínimo e máximo
    '''
    dados = []

    # o '_' (underline) serve para dizer para o 
    # python (e quem esta lendo) que esse for
    # é apenas para executar o comando varias vezes0
    for _ in range(qtd):
        dados.append(random.randint(minimo, maximo))
    return dados

# 2) Processar dados -> tente dar nome com 
# 'significado'
def calcular_total(valores):
    '''Soma todos os valores da lista'''
    return sum(valores)
    # total = 0
    # for valor in valores:
    #     total += valor
    #     # total = total + valor
    # return valor

def calcular_media(valores):
    '''Calcula media dos valores.
    Retorna 0 se a lista estiver vazia '''
    # if len(valores) == 0:
    #     return 0
    # outro jeito de fazer -> pergunta se tem 
    # nada dentro da variavel
    if not valores:
        return 0
    total = calcular_total(valores)
    return total/len(valores)

def calcula_amplitude(valores):
    '''Calcula a amplitude dos valores, pegando
    o máximo e o mínimo da lista'''
    maximo = max(valores)
    minimo = min(valores)

    return maximo - minimo

def calcular_projecao(valores, fator):
    pass

def exibir_resultados(dados):
    '''Mostra os dados e calculos realizados'''

    print(f'Dados Gerados: {dados}')
    print(f'Soma: {calcular_total(dados)}')
    media = calcular_media(dados)
    print(f'Média: {media}')
    print(f'A Amplitude dos dados é: \
          {calcula_amplitude(dados)}')
    

def main():
    qtd = 10
    minimo = 0
    maximo = 100

    dados = gerar_dados(qtd, minimo, maximo)
    exibir_resultados(dados)

main()