'''
4) Descubra a lógica e complete o próximo elemento: 
a) 1, 3, 5, 7, ___ 
b) 2, 4, 8, 16, 32, 64, ____ 
c) 0, 1, 4, 9, 16, 25, 36, ____ 
d) 4, 16, 36, 64, ____ 
e) 1, 1, 2, 3, 5, 8, ____ 
f) 2,10, 12, 16, 17, 18, 19, ____

'''

# a)
i = 1
for _ in range(5):
    print(i, end = ", ")
    i+=2

# b)
i = 2
for _ in range(7):
    print(i, end = ", ")
    i*=2

# c)

i = 0
for _ in range(8):
    print(i*i, end = ", ")
    i+=1

# d)

i = 2
for _ in range(5):
    print(i*i, end = ", ")
    i+=2

# e)

n = 8
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

# f)

print(2, 10, 12, 16, 17, 18, 19)
print(200)