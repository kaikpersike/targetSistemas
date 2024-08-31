'''
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre. 
'''

texto = str(input())
cont  = 0

for i in texto.lower():
    if i == 'a':
        cont+=1

if cont >= 1:
    print(f"A letra 'a' existe no texto e a quantidade é: {cont}")
else:
    print(f"Quantidade de letra 'a': {cont}")
