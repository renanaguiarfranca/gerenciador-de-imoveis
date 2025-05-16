print('Validador de CPF')
cpf = input('Digite seu CPF:\n>>> ')  

# Remove pontos, traços e espaços (deixa apenas números)
cpf_numeros = ''.join(filter(str.isnumeric, cpf))#essa sequencia de funções pega todos os digitos da parte em que
#a pessoa digita o CPF e pega cada digito.

# função join: (''.join) a parte das aspas vazias é o espaço a ser preenchido no qual a pessoa irá preencher la em cima
#e a função join em si ela  é um método das strings usado para juntar elementos de uma lista (ou qualquer iterável) em uma única string,
#separando-os com um caractere ou string específico.

# função filter: A função filter() no Python é usada para filtrar elementos de um iterável (como listas, tuplas, strings, etc.) 
# com base em uma função que define um critério. Ela retorna um objeto iterador ( Iterador no Python = "Contador de Elementos Inteligente", ou seja oque eu manda ele mostrar apartir do ex: [0],[1]... ele mostra. ) 
# contendo apenas os elementos que atendem à condição especificada(como dito anteriormente [0],[1]...).

# str.isnumeric: A função str.isnumeric() em Python é usada para verificar se todos os caracteres de uma string são numéricos, incluindo dígitos comuns (0-9)

n1 = int(cpf_numeros[0]) #defini o primeiro digito para numero inteiro
resultadoN1 = n1 * 10 #usei a função anterior para fazer a conta necessaria para fazer o validador

n2 = int(cpf_numeros[1])
resultadoN2 = n2 * 9

n3 = int(cpf_numeros[2])
resultadoN3 = n3 * 8

n4 = int(cpf_numeros[3])
resultadoN4 = n4 * 7

n5 = int(cpf_numeros[4])
resultadoN5 = n5 * 6

n6 = int(cpf_numeros[5])
resultadoN6 = n6 * 5

n7 = int(cpf_numeros[6])
resultadoN7 = n7 * 4

n8 = int(cpf_numeros[7])
resultadoN8 = n8 * 3

n9 = int(cpf_numeros[8])
resultadoN9 = n9 * 2
#conta para validação, numero 1 * 10, numero 2 * 9, numero 3 * 8... e assim por diante até o numero 9, os dois ultimos numeros não entrão nessa soma.

r = ((resultadoN1 + resultadoN2 + resultadoN3 + resultadoN4 + resultadoN5 + resultadoN6 + resultadoN7 + resultadoN8 + resultadoN9) *10) %11

n10 = int(cpf_numeros[9])

resultadoN10 = n10 #numero que representa o resultado a ser alcançado, ou seja, o resultado do validador tem que ser esse

#conta a ser feita, todos os numeros depois da multiplicação, o resultado deles somados em seguida multiplicados por 10 e depois pegando o resto da divisão inteira por 11.
print('obs: se caso o resultado tiver sido 10, ele vale por 0')
print('o resultado a ser alcançado é de {} e o resultado obtido foi de {}'.format(n10,r))