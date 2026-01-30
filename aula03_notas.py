# Variaveis (Boas praticas)
# Não pode:
# 1. iniciar com numero
# 2. ter espaço
# Tente não começar com caracteres especiais
# _ab = 1 

# ideal -> começar com letra minuscula
# ideal -> usar uma só formatação
# Obs.: Tudo maiusculo indica uma "constante"

# formatação
# rio de janeiro
# 1. snake_case: underline no lugar do espaço
# ex.:
rio_de_janeiro = 'Cuidado'

# 2. camelCase: onde teria o espaço, letra
# maiuscula
rioDeJaneiro = 'Cuidado redobrado'

# 3. PascalCase: usado para classes (sempre 
# inicia a palavra com letra maiuscula)
RioDeJaneiro = 'a'

# Dadas as 4 notas de um estudante, 
# calcular sua média: 
# caso a média seja maior que 7, 
# emitir mensagem de aprovado; 
# caso a média esteja entre 5 e 7, 
# emitir mensagem que o estudante está em recuperação;
# caso esteja abaixo de 5, 
# emitir mensagem de reprovação.


# etapa 1: pegar as notas (4)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

# print('Média do aluno(a): ', media)

if media > 7:
    print('Aprovado!')

elif media >= 5 and media <=7:
    print('Recuperação')

else:
    print('Reprovado')