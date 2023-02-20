# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 7 - Escreva um programa que adicione uma chave (key) a um dicionário. Exemplo dicionário(Dict): {0: 10, 1: 20}
# Resultado esperado: {0: 10, 1: 20, 2: 30}
# Sendo a ideia do exercício fixar o aprendizado sobre adicionar elementos em um dicionário, a lógica usada foi criar um dicionário do tamanho que a pessoa quer e digitar 0 quando quiser finaliza-la. Para facilitar, apenas números inteiros foram utilizados.


dicionario = {} #Cria um dict vazio
i = 0
while i < 100: #Estrutura de repetição com grande valor para que mesmo se o número digitado for errado, a pessoa possa tentar outra vez sem perder o que já havia colocado. Retornando em então para o pedido por uma chave.
    try:
        key = int(input('\n-----Digite a chave do dicionário(Digite 0 para finalizar): '))
        if key == 0: #Finaliza a estrutura de repetição e mostra o dicionário caso o número da chave for 0
            print('Você finalizou o dicionário.')
            break
        valor = int(input(f'Digite o valor da chave {key}: '))
        if key not in dicionario.keys(): #Verifica se a chave está na visão do dicionário das chaves
            print(f'A chave {key} foi adicionada no dicionário com o valor {valor}.')
        else:
            print(f'A chave {key} já existia no dicionário, por tal, atualizamos o valor dela para {valor}.')
            #Se a chave já existir no dicionário, a mesma será adicionada e o seu valor terá prioridade, substituindo o anterior
        dicionario[key] = valor #Adiciona o par chave valor no dicionário
        i += 1
    except ValueError:
        print('\nDigine números inteiros')

if dicionario == {}: #Diferencia o dicionário vazio do dicionário com valores.
  print(f'Você criou um dicionário vazio!.')
else:
  print(f'O dicionário criado foi: {dicionario}.')
