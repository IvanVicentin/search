import random
import time
import matplotlib.pyplot as plt

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

# Função para gerar um array aleatório de tamanho n
def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Lista para armazenar os tempos de ordenação
sorting_times = []

# Tamanhos de dados a serem testados
data_sizes = list(range(10, 101, 10))

# Loop sobre os tamanhos de dados
for size in data_sizes:
    # Gera um array aleatório de tamanho 'size'
    arr = generate_random_array(size)
    # Cria uma cópia do array para manter os índices originais
    arr_copy = arr[:]
    # Cria uma lista de índices correspondentes
    indices = list(range(len(arr)))

    # Mede o tempo de execução do Quicksort
    start_time = time.time()
    quicksort(arr, 0, len(arr)-1, indices)
    end_time = time.time()
    sorting_time = end_time - start_time
    sorting_times.append(sorting_time)

# Exibindo apenas os tempos de ordenação
print("Tempos de ordenação:")
for i, size in enumerate(data_sizes):
    print(f"Tamanho do array: {size}, Tempo de ordenação: {sorting_times[i]:.6f} segundos")

# Plotando o gráfico dos tempos de ordenação
plt.plot(data_sizes, sorting_times, marker='o')
plt.title('Tempo de ordenação usando Quicksort em função do tamanho do array')
plt.xlabel('Tamanho do array')
plt.ylabel('Tempo de ordenação (segundos)')
plt.grid(True)
plt.show()
