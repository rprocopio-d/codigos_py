# Construa um programa que exiba a 
# sequência de Fibonacci de zero até dois mil.

# 3 numeros
# 2 anteriores, 1 "atual"

anterior = 0
atual = 1
proximo = anterior + atual #(3)
while proximo <= 2000:
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    print(proximo)




fibo1, fibo2 = 0, 1

while fibo1 <= 2000:
    print(fibo1)
    fibo1, fibo2 = fibo2, fibo1 + fibo2
