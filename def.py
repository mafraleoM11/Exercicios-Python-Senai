# situação 1
def sistema_notas():
    nome = input('Digite o nome do aluno: ')

    n1 = float(input('Digite a 1ª nota do aluno: '))
    n2 = float(input('Digite a 2ª nota do aluno: '))
    n3 = float(input('Digite a 3ª nota do aluno: '))

    media = (n1 + n2 + n3) / 3

    if media >= 7:
        result = "Aprovado"
    elif media >= 5:
        result = "Recuperação"
    else:
        result = 'Reprovado'
    

    print (f'\n nome aluno: {nome}')
    print (f'notas: {n1,n2,n3}')
    print (f'media: {media}')
    print (f'Resultado: {result}')

sistema_notas()

# ex 1

def Consumo_comb() :
    nome = input('Digite o nome do motorista: ')
    km = float(input('Digite a quantidade de km percorridos: '))
    l = float(input('Digite a quantidade de litros de combustivel gastos: '))
    consumo = km/l

    if consumo >= 15:
        valor = 'Econômico'
    elif consumo >= 10:
        valor = 'Regular'
    else:
        valor = 'Alto consumo'

    print (f'\nO seu consumo foi de: {consumo}')
    print (f'Ele foi: {valor}')

Consumo_comb()

# ex 2

def imc_calc():
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    altura = float(input('DIgite a altura: '))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        result = 'Abaixo do peso!'
    elif imc >= 18.5:
        result = 'Peso normal!'
    elif imc >= 25:
        result = 'Sobrepeso!'
    elif imc >= 30:
        result = 'Obesidade!'

    print(f'\nnome: {nome}')
    print(f'Valor do IMC: {imc}')
    print(f'classificação: {result}')

imc_calc()

#ex 3

def verificar_vel():
    nome = input('Digite o nome do motorista: ')
    vel = float(input('Digite a velocidade registrada: '))

    if vel <= 80:
        result = 'Dentro do limite'
    elif vel >= 81:
        result = 'Acima do limite(leve)'
    elif vel > 100:
        result = 'Acima do limite(grave)'

    print(f'nome : {nome}')
    print(f'Velocidade: {vel}')
    print(f'Classificação: {result}')

verificar_vel()

# ex 4

def soma(a, b):
    print (a + b)

v1 = float(input('Digite um número: '))
v2 = float(input('Digite outro número: '))
soma(v1, v2)