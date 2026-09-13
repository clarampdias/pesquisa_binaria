'''

Exercícios com pesquisa binária
1. Quantos números primos são menores que 67

'''

# Lista ordenada de números primos
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Função genérica de busca binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto: # Enquanto houver intervalo para buscar
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        if chute == item:
            return meio  # Retorna o índice 
        elif chute > item:
            alto = meio - 1 # Busca na metade esquerda
        else:
            baixo = meio + 1 # Busca na metade direita

    return None

# Chamada da função para encontrar a posição do 67
quantidade_menores = pesquisa_binaria(primos, 67)
print(f"Quantidade de primos menores que 67: {quantidade_menores}")