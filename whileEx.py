#Ex1

n = 1

while n <= 10:
    print (n)
    n +=1
    

#Ex2

nome = ''

while True:
    nome = input('Digite um nome: ')
    
    if nome == 'sair':
        print ('finalizando código')
        break
    

#Ex3

chamada = 0

while chamada < 10:
    chamada += 1
    if chamada == 5:
        print ('Faltou')
        continue
    print (f'Aluno {chamada}')
    

#Ex4

saque = 0
senha = '1234'
tentativa = ''

while tentativa != senha:
    tentativa = input('Digite sua senha para sacar: ')
    if tentativa == senha:
        print ('Saque realizado!')
        break
    else:
        print ('Senha errada tente novamente!')
        saque +=1
        
    if saque == 3:
        print ('Caixa bloqueado!')
        break