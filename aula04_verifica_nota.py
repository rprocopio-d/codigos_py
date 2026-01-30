# somente notas entre 0 e 10 devem ser aceitas

nota = float(input('Digite a nota: '))

while nota < 0 or nota > 10:
    print('Valor Inválido, Digite novamente')
    nota = float(input('Digite a nota: '))

print(nota)