import heapq  # Importa o módulo heapq para utilizarmos uma Fila de Prioridade (Min-Heap)

# Definimos o Grafo do Mapa da Romênia como um dicionário de dicionários.
# As chaves são as cidades e os valores são dicionários com as cidades vizinhas e suas distâncias reais (custo g).
mapa_romenia = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 118, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Definimos a Heurística h(n): Distância em linha reta de cada cidade até o objetivo final (Bucharest)
heuristica_bucharest = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

def busca_a_estrela(grafo, inicio, objetivo, heuristica):
    # Cria a fila de prioridade (lista aberta). Armazena tuplas no formato: (f_score, no_atual)
    lista_aberta = []
    
    # Insere o nó inicial na fila de prioridades com f_score inicial igual à sua própria heurística
    heapq.heappush(lista_aberta, (heuristica[inicio], inicio))
    
    # Dicionário para armazenar o histórico de navegação (chave: nó filho, valor: nó pai)
    veio_de = {}
    
    # Dicionário para rastrear o custo real acumulado (g_score) para chegar a cada nó. Inicializa com infinito.
    g_score = {cidade: float('inf') for cidade in grafo}
    # O custo real para ir do início para o próprio início é, obviamente, zero
    g_score[inicio] = 0
    
    # Dicionário para rastrear o custo total estimado (f_score = g + h). Inicializa com infinito.
    f_score = {cidade: float('inf') for cidade in grafo}
    # O f_score inicial do ponto de partida é apenas o valor de sua heurística h(inicio) + 0
    f_score[inicio] = heuristica[inicio]
    
    # O loop continuará executando enquanto houver nós a serem explorados na lista aberta
    while lista_aberta:
        # Extrai da lista aberta o nó que possui o MENOR valor de f_score atual
        _cost, atual = heapq.heappop(lista_aberta)
        
        # Verifica se o nó atual extraído é o destino (Bucharest)
        if atual == objetivo:
            # Se for, cria uma lista para reconstruir o caminho percorrido
            caminho_total = [atual]
            # Faz o caminho reverso do objetivo até o início usando o dicionário 'veio_de'
            while atual in veio_de:
                atual = veio_de[atual]  # Move para o pai do nó atual
                caminho_total.append(atual)  # Adiciona o pai à lista do caminho
            # Retorna o caminho invertido (para ficar do início ao fim) e o custo total gasto
            return caminho_total[::-1], g_score[objetivo]
            
        # Percorre todos os nós vizinhos e as respectivas distâncias do nó atual no grafo
        for vizinho, distancia_aresta in grafo[atual].items():
            # Calcula o custo g temporário para o vizinho passando pelo nó atual
            g_temporario = g_score[atual] + distancia_aresta
            
            # Se este novo caminho até o vizinho for menor do que qualquer caminho descoberto antes:
            if g_temporario < g_score[vizinho]:
                # Registra que o melhor caminho para chegar a este vizinho vem do nó atual
                veio_de[vizinho] = atual
                # Atualiza o custo real g do vizinho com o novo valor menor encontrado
                g_score[vizinho] = g_temporario
                # Calcula o novo f(n) do vizinho: f(n) = g(n) + h(n)
                f_score[vizinho] = g_temporario + heuristica[vizinho]
                
                # Se o vizinho ainda não estiver na lista aberta para ser expandido, adiciona ele
                if vizinho not in [item[1] for item in lista_aberta]:
                    heapq.heappush(lista_aberta, (f_score[vizinho], vizinho))
                    
    # Caso a lista aberta esvazie e o objetivo não tenha sido atingido, o caminho não existe
    return None, float('inf')

# --- EXECUÇÃO DO CÓDIGO ---

# Define a cidade de partida e o objetivo final na Romênia
ponto_partida = 'Arad'
ponto_destino = 'Bucharest'

# Executa a função do algoritmo A* passando as estruturas criadas
rota, custo = busca_a_estrela(mapa_romenia, ponto_partida, ponto_destino, heuristica_bucharest)

# Exibe os resultados formatados na tela
print(f"--- Busca A* no Mapa da Romênia ---")
print(f"Origem: {ponto_partida} -> Destino: {ponto_destino}\n")
print(f"Melhor Rota Encontrada: {' -> '.join(rota)}")
print(f"Custo Total do Caminho (Distância Real): {custo} km")