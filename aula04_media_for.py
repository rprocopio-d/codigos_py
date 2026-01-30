# 10 alunos
# 2 notas cada aluno
# fazer média de cada aluno

for i in range(0, 10):
    nota1 = \
    float(input('Digite a primeira nota: '))
    nota2 = \
    float(input('Digite a segunda nota: '))

    media = (nota1 + nota2)/2
    print(f'Aluno {i+1} - Média: {media}')