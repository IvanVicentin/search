# -*- coding: utf-8 -*-
"""binarys.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2r7nkyBw2thwUUKdMtuFaT_wjEqzLjA
"""

print("A idéia desse código é usar uma busca binária onde o array é ordenado com um quicksort\njá que a amanda nao me deixou usar a função sort do python :(")

def partition(arr, low, high, indices):
    """
    Particiona o array com base no elemento pivô.
    Os elementos menores que o pivô ficarão à esquerda e os maiores à direita.
    Além de particionar o array, mantém também o array de índices correspondente.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Troca elementos no array
            arr[i], arr[j] = arr[j], arr[i]
            # Troca índices para manter a correspondência com os elementos
            indices[i], indices[j] = indices[j], indices[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    indices[i + 1], indices[high] = indices[high], indices[i + 1]
    return i + 1

def quicksort(arr, low, high, indices):
    """
    Função recursiva para ordenar o array usando o algoritmo quicksort.
    """
    if low < high:
        # Particiona o array
        pi = partition(arr, low, high, indices)
        # Ordena recursivamente as partições esquerda e direita
        quicksort(arr, low, pi - 1, indices)
        quicksort(arr, pi + 1, high, indices)

def binarySearch(arr, target):
    """
    Realiza busca binária no array ordenado para encontrar todas as ocorrências do valor alvo.
    Retorna uma lista contendo índices de todas as ocorrências do valor alvo.
    """
    # Cria uma lista de tuplas contendo elementos e seus índices originais (O código estava retornando os índices ordenados)
    indices = [(arr[i], i) for i in range(len(arr))]
    # Ordena o array usando o algoritmo quicksort
    quicksort(arr, 0, len(arr)-1, indices)

    # Inicializa ponteiros para busca binária
    low = 0
    high = len(arr) - 1
    result_indices = [] # A lista mostra todas as ocorrências de um elemento no array, caso ele esteja duplicado

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            # Adiciona o índice do elemento encontrado à lista de resultados
            result_indices.append(indices[mid][1])
            # Verifica outras ocorrências à esquerda
            left = mid - 1
            while left >= 0 and arr[left] == target:
                result_indices.append(indices[left][1])
                left -= 1
            # Verifica outras ocorrências à direita
            right = mid + 1
            while right < len(arr) and arr[right] == target:
                result_indices.append(indices[right][1])
                right += 1
            # Retorna a lista de índices
            return result_indices
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Se o alvo não for encontrado, retorna uma lista vazia
    return result_indices

# Exemplo de uso:
arr = [13, 5, 7, 1, 11, 3, 9, 7]
alvo = 7

resultado = binarySearch(arr, alvo)

#Se resultado == True
if resultado:
    print("Elemento está presente nos índices:", resultado)

# Se resultado == False
else:
    print("Elemento não está presente no array")