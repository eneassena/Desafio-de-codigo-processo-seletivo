"""
# Questão 02

Dado um vetor de inteiros n e um inteiro qualquer x. Construa um
algoritmo que determine o número de elementos pares do vetor que
tem uma diferença igual ao valor de x.

Exemplo:
Entrada:
n = [1, 5, 3, 4, 2]

Saída:
3

Explicação:

Existem 3 pares de inteiros no vetor com uma diferença de 2:
[5, 3], [4, 2] e [3, 1].

"""

def desafio2(numbers):
    # declaração de variaveis
    numbers = numbers #[1, 5, 3, 4, 2]

    num = 3

    cont = 0

    indices = []

    pares_de_elementos = []


    # loop pecorre a lista de números
    for x in range(len(numbers)):

        cont += 2

        gerador = numbers[cont-2:cont]

        if len(gerador) == 0: continue

        if len(gerador) == 1:

            gerador.append(num)

        pares_de_elementos.append(gerador)


    # saida 
    for el in pares_de_elementos:
        print(el, end=" ")


