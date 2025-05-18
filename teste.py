cpf = input("14538220620")

d1 = int(cpf[0]) * 10
d2 = int(cpf[1]) * 9
d3 = int(cpf[2]) * 8
d4 = int(cpf[3]) * 7
d5 = int(cpf[4]) * 6
d6 = int(cpf[5]) * 5
d7 = int(cpf[6]) * 4
d8 = int(cpf[7]) * 3
d9 = int(cpf[8]) * 2

soma = d1+d2+d3+d4+d5+d6+d7+d8+d9
multiplicacao = soma * 10
restDivisao = multiplicacao % 11
print(restDivisao)