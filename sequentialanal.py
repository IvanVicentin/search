# -*- coding: utf-8 -*-

import time
import random
import matplotlib.pyplot as plt

def sequential_search(arr, target):
    """
    Faz uma busca sequencial no array para encontrar o elemento alvo
    """
    start_time = time.time()  # Marca o tempo de início da busca

    # O loop for percorre todo o array e compara todos os elementos com o alvo
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()  # Marca o tempo de fim da busca
            return i, end_time - start_time  # Retorna o indice e o tempo de execução

    end_time = time.time()  # Marca o tempo de fim da busca
    return -1, end_time - start_time  # Retorna -1 se o elemento não for encontrado e o tempo de execução

# Listas para armazenar os resultados
array_sizes = []
execution_times = []

# Realiza a análise experimental
for array_size in range(10, 101, 10):  # Varia o tamanho do array de 10 em 10 até 100
    arr = [random.randint(1, 100) for _ in range(array_size)]  # Gera um array aleatório
    target = random.randint(1, 100)  # Gera um alvo aleatório
    index, time_taken = sequential_search(arr, target)  # Executa a busca sequencial
    print(f"Tamanho do array: {array_size}, Tempo gasto: {time_taken:.6f} segundos")
    array_sizes.append(array_size)
    execution_times.append(time_taken)

# Plotando o gráfico
plt.plot(array_sizes, execution_times, marker='o')
plt.title('Análise Experimental do Algoritmo de Busca Sequencial')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo de Execução (segundos)')
plt.grid(True)
plt.show()
