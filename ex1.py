'''
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 
'''
n = int(input())
arr = []
if n == 1:
    print("0")
elif n == 2:
    print("0 1")
else:
    print("0 1", end=" ")
    a = 0
    b = 1
    
    for i in range (n-2):
        soma = a+b
        arr.append(soma)
        print(soma, end = " ")
        a = b
        b = soma

for i in arr:
    if n == i:
        print(f"\nO nº {n} pertence a sequencia Fibonacci")