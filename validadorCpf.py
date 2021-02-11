#validar cpf

cpf = input('Digite seu cpf: ')
n_cpf = cpf[:-2]
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

seq = n_cpf == str(n_cpf[0]) * len(cpf)
if cpf == n_cpf and not seq:
    print('Válido')
else:
    print('Inválido')





