    #Escreva um progama para aprovar o empréstimo bancário para a compra de uma casa.
    #o programa vai perguntar o Valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    #calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
    #o valor será negado.

from time import sleep #importando delay para o programa

nome = str(input('Inserir seu nome: ')).title().strip() #title para nomes e strip para colocar espaçador de forma exata.
sleep(0.5)

print(f'Olá, {nome}, façamos uma verificação do seu pedido de empreśtimo...')
sleep(0.5)

print('Para isso, preencha as perguntas a seguir: ')
sleep(1)

valor = float(input('inserir o valor da casa: R$ '))
salário = float(input('inserir o seu salário: R$ '))
anos = float(input('Em quantos anos será pago a prestação: '))

#Prestação mensal




