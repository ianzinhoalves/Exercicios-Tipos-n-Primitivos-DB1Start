# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 5 - Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais.
#(Exemplo de lista: ['abc','xyz','aba','1221'] Resultado esperado: 2)

lista = []
for i in range(5):
  lista.append(input('Digite uma string: '))

aparicoes = 0
choosen = []
for i in lista:
  if len(i) > 2 and i[0] == i[len(i)-1]:
    aparicoes += 1
    choosen.append(i)

print(f'Você digitou {aparicoes} strings que tem tamanho maior que 2 e o primeiro e o último caracteres sejam iguais.')
for i in range(len(choosen)):
  print(choosen[i] , end=' ')