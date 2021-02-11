#gerador cpf
from random import randint

num = str(randint(100000000, 999999999))

n_cpf = num
z = 10
soma = 0

for x in range(2):
    soma = 0
    for x in n_cpf:
        soma += int(x)*z
        z -= 1

    dig = 0 if 11-(soma%11) > 9 else 11-(soma%11)
    n_cpf += str(dig)
    z = 11

print(n_cpf)









