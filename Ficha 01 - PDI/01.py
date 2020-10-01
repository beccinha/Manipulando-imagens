import random
import statistics
import numpy

def somaElementos(rangeNumero):
    elementosSomados = 0
    if rangeNumero < 100:
        arrayAleatorio = random.sample(range(0,100), rangeNumero)
    for numero in arrayAleatorio:
        elementosSomados += numero
    print("Lista Aleatória:", arrayAleatorio)
    print("Soma dos elementos:", elementosSomados)
    pass

def valorMinimo(rangeNumero):
    if rangeNumero < 100:
        arrayAleatorio = random.sample(range(0,100), rangeNumero)
    minimo = min(arrayAleatorio)
    print("Lista Aleatória:", arrayAleatorio)
    print("Valor Mínimo:", minimo)
    pass

def valorMaximo(rangeNumero):
    if rangeNumero < 100:
        arrayAleatorio = random.sample(range(0,100), rangeNumero)
    maximo = max(arrayAleatorio)
    print("Lista Aleatória:", arrayAleatorio)
    print("Valor Máximo:", maximo)
    pass

def media(rangeNumero):
    if rangeNumero < 100:
        arrayAleatorio = random.sample(range(0,100), rangeNumero)
    mediaNumero = numpy.mean(arrayAleatorio)
    print("Lista Aleatória:", arrayAleatorio)
    print("Valor Médio:", mediaNumero)
    pass

def mediana(rangeNumero):
    if rangeNumero < 100:
        arrayAleatorio = random.sample(range(0,100), rangeNumero)
    medianaValor = statistics.median(arrayAleatorio)
    print("Lista Aleatória:", arrayAleatorio)
    print("Mediana:", medianaValor)
    pass

print('Defina um range se selecionou uma lista aleatória')
rangeNumero = int(input())
print('Escolha uma função para o sua lista')
print({
    '1 - Soma de Elementos'
    ' 2 - Valor Minimo'
    ' 3 - Valor Máximo'
    ' 4 - Valor Médio'
    ' 5 - Mediana'
})
funcao = input()
if funcao == '1':
    somaElementos(rangeNumero)
elif funcao == '2':
    valorMinimo(rangeNumero)
elif funcao == '3':
    valorMaximo(rangeNumero)
elif funcao == '4':
    media(rangeNumero)
elif funcao == '5':
    mediana(rangeNumero)