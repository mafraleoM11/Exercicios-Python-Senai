#ex 1

pag = input('Qual a forma de pagamento? (cartao ou boleto) ')

if pag == 'cartao':
    print ('Processando pagamento no cartão...')
elif pag == 'boleto':
    print ('Gerando boleto bancário...')
else:
    print ('Método de pagamento não reconhecido.')
    
    
#ex 2

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print ('Criança')
elif idade >= 13 and idade <= 17:
    print ('Adolescente')
elif idade >= 18 and idade <= 59:
    print ('Adulto')
elif idade >= 60:
    print ('Idoso')
    

#ex 3

entrega = input('Qual será o tipo de entrega? (padrao ou boleto) ')

if entrega == 'padrao':
    print ('Valor a ser pago: R$10,00.')
elif entrega == 'expresso':
    print ('Valor a ser pago: R$20,00.')
else:
    print ('Opção de entrega inválida.')
    