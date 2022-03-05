"""
# Questão 01

A mediana de uma lista de números é basicamente o elemento que se encontra no
meio da lista após a ordenação. Dada uma lista de números com um número ímpar
de elementos, desenvolva um algoritmo que encontre a mediana.

Exemplo:

Entrada:
arr = [9, 2, 1, 4, 6]

Saída:
4
"""

arr = [9, 2, 1, 4, 6]

def desafio1(arr):
    arr.sort()
    soma = sum(arr)
    t = len(arr)
    media = int(soma / t)
    return media


