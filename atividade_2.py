'''

Exercícios com pesquisa binária
2. Qual o nome associado ao número 256 e quantas tentativas foram feitas? Quantas tentativas seriam em uma pesquisa sequencial?

'''
lista = [
    (3, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'), (19, 'Eduardo'),
    (28, 'Fernanda'), (33, 'Gustavo'), (35, 'Helena'), (43, 'Igor'), (48, 'Juliana'),
    (58, 'Kleber'), (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Tiago'), (122, 'Vanessa'),
    (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'), (149, 'Diego'), (151, 'Eliane'),
    (175, 'Fabiano'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabela'), (194, 'João'),
    (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirela'), (213, 'Nicolas'), (232, 'Olívia'),
    (241, 'Pedro'), (244, 'Queila'), (246, 'Rodrigo'), (256, 'Simone'), (258, 'Túlio'),
    (259, 'Ursula'), (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'), (294, 'Fábio')
]

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tentativas = 0

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto) // 2
        numero_procurado = lista[meio][0] # Pega o número da tupla

        if numero_procurado == item:
            return meio, tentativas # Retorna a posição e a quantidade de tentativas
        elif numero_procurado > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None, tentativas

# Executando a Busca Binária
posicao, tentativas_bin = pesquisa_binaria(lista, 256)
nome_encontrado = lista[posicao][1] # Pega o nome (índice 1 da tupla)

print(f"Nome associado ao numero 256: {nome_encontrado}")
print(f"Tentativas utilizando Pesquisa BINÁRIA: {tentativas_bin}")

# Executando a Busca Sequencial (Para comparar)
tentativas_seq = 0

for numero, nome in lista:
    tentativas_seq += 1
    if numero == 256:
        print(f"Tentativas utilizando Pesquisa SEQUENCIAL: {tentativas_seq}")
        break
