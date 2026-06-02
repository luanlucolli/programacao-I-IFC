def somar_dois_numeros():
    numero1 = int(input("número 1: "))
    numero2 = int(input("número 2: "))

    soma = numero1 + numero2
    print(soma)


def converter_metros_para_centimetros():
    metros = float(input("metros:"))
    centimetros = metros * 100
    print(centimetros)


def calcular_area_retangulo():
    largura = int(input("largura: "))
    altura = int(input("altura: "))
    area = largura * altura
    print("area:", area)


def calcular_ano_nascimento():
    idade = int(input("idade: "))
    anoNascismento = 2026 - idade
    print("idade:", idade, "| ano de nascimento:", anoNascismento)


def converter_tempo_para_segundos():
    dias = int(input("dias: "))
    horas = int(input("horas: "))
    minutos = int(input("minutos: "))
    segundos = int(input("segundos: "))

    totalSegundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
    print("total de segundos:", totalSegundos)


def calcular_desconto():
    valor = float(input("valor: "))
    desconto = float(input("desconto: "))
    valorDesconto = valor * (desconto / 100)
    valorFinal = valor - valorDesconto
    print("valor desconto:", valorDesconto, "| valor final:", valorFinal)


def calcular_tempo_viagem():
    distancia = float(input("distância em km: "))
    velocidadeMedia = float(input("velocidade média: "))
    tempo = distancia / velocidadeMedia
    print("tempo em horas:", tempo)


def converter_celsius_para_fahrenheit():
    temperaturaCelsius = float(input("temperatura em celsius: "))
    f = (temperaturaCelsius * 1.8) + 32
    print("temperatura em fahrenheit:", f)


def calcular_valor_aluguel():
    valorDiaAluguel = 60
    valorKmRodado = 0.15

    kmPercorrido = float(input("km percorrido: "))
    diasPercorridos = int(input("dias percorridos: "))

    valorTotal = (valorDiaAluguel * diasPercorridos) + (valorKmRodado * kmPercorrido)
    print("valor total do aluguel:", valorTotal)


def calcular_tempo_perdido_cigarro():
    minutosPerdidosCigarro = 10

    qtdCigarros = int(input("quantidade de cigarros fumados por dia: "))
    anosFumando = int(input("quantos anos fumando: "))

    totalMinutosPerdidos = qtdCigarros * minutosPerdidosCigarro * 365 * anosFumando
    totalDiasPerdidos = totalMinutosPerdidos / (60 * 24)
    print("total de minutos perdidos:", totalMinutosPerdidos, "| total de dias perdidos:", totalDiasPerdidos)


def testar_tipos():
    var = input("digite um número: ")
    print("o número digitado foi:", var)
    var = int(var)
    print(type(var))
    var = float(var)
    print(type(var))
    var = False
    print(type(var))
