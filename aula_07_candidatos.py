# modulo/biblioteca para trabalhar com datas

# usar "import" você pega o modulo inteiro
# para pegar só parte dele use:
# "from 'modulo' import 'coisa'"
from datetime import datetime

candidatos = []

# len -> tamanho (comprimento) da lista
while len(candidatos) < 2:
    # strip -> remove espaço em branco
    # do inicio e do final
    nome = input('Nome Completo: ').strip()
    # isso é para forçar a ter algo escrito
    data_nasc = \
    input('Data de Nascimento (dd/mm/aaaa): ')

    try:
        # converter em um objeto tipo data
        data_convertida = \
            datetime.strptime(data_nasc, '%d/%m/%Y')

        # restrição do problema
        hoje = datetime.now()
        # fazer a conta
        idade = \
            hoje.year - data_convertida.year - \
            ((hoje.month, hoje.day) <
             (data_convertida.month,
                data_convertida.day))

        if idade < 18:
            print(f'Candidato tem {idade} anos.\
                  Cadastro não permitido')
            continue

    except ValueError:
        print('Data Inválida')
        continue

    telefone = input('Telefone: ').strip()
    email = input('E-mail: ').strip()
    formacao = \
        input('Formação Acadêmica: ').strip()

    pessoa = {
        'nome': nome,
        'data_nasc': data_convertida,
        'telefone': telefone,
        'email': email,
        'formacao': formacao
    }
    # guardar a pessoa na lista de candidatos
    candidatos.append(pessoa)
    
print(40*'=')
for candidato in candidatos:
    for chave, valor in candidato.items():
        print(f'{chave}: {valor}')
    print('\n')