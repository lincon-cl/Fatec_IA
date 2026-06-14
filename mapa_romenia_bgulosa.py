# Para resolver o clássico problema do Mapa da Romênia usando a Busca Gulosa (Greedy Best-First Search), 
# precisamos de duas coisas principais:O Grafo do Mapa: As conexões entre as cidades e as distâncias reais entre elas.A Heurística ($h(n)$): 
# A distância em linha reta de cada cidade até o nosso objetivo final, que tradicionalmente é Bucharest. 
# A busca gulosa foca apenas nessa heurística para tomar decisões.Aqui está um código em Python completo, estruturado e pronto para rodar.
# Utilizei a biblioteca heapq para garantir que a cidade com a menor distância heurística seja sempre escolhida primeiro.O Código em PythonPythonimport heapq

# 1. Definição do Mapa da Romênia (Grafo de adjacências)
# O formato é: Cidade_Atual: {Cidade_Vizinha: Distancia_Real, ...}
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

# 2. Heurística: Distância em linha reta até Bucharest
heuristica_bucharest = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

def busca_gulosa(grafo, heuristica, inicio, objetivo):
    # Fila de prioridade armazena tuplas: (valor_heuristico, cidade_atual, caminho_percorrido)
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica[inicio], inicio, [inicio]))
    
    # Conjunto para evitar visitar a mesma cidade mais de uma vez
    visitados = set()
    
    while fila_prioridade:
        # Extrai a cidade com a MENOR distância em linha reta (heurística) até o objetivo
        h_atual, cidade_atual, caminho = heapq.heappop(fila_prioridade)
        
        # Se chegamos ao objetivo, retornamos o caminho e o custo total
        if cidade_atual == objetivo:
            return caminho
        
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            
            # Explora os vizinhos da cidade atual
            for vizinho in grafo[cidade_atual]:
                if vizinho not in visitados:
                    # Na busca gulosa, a prioridade depende APENAS da heurística do vizinho
                    h_vizinho = heuristica[vizinho]
                    novo_caminho = caminho + [vizinho]
                    heapq.heappush(fila_prioridade, (h_vizinho, vizinho, novo_caminho))
                    
    return None # Caso não encontre caminho

# 3. Execução do teste de Arad para Bucharest
inicio = 'Arad'
objetivo = 'Bucharest'

caminho_final = busca_gulosa(mapa_romenia, heuristica_bucharest, inicio, objetivo)

# Calcular o custo total real do caminho encontrado
custo_total = 0
for i in range(len(caminho_final) - 1):
    custo_total += mapa_romenia[caminho_final[i]][caminho_final[i+1]]

print(f"--- Resultado da Busca Gulosa ---")
print(f"Origem: {inicio} -> Destino: {objetivo}")
print(f"Caminho encontrado: {' -> '.join(caminho_final)}")
print(f"Custo total real do caminho: {custo_total} km")

# Como esse código funciona na prática?
# Ele começa em Arad. Olhando os vizinhos de Arad (Sibiu, Timisoara, Zerind), 
# ele ignora a distância das estradas e olha apenas a tabela de linha reta até Bucharest:
# Sibiu: 253Timisoara: 329Zerind: 374 Como Sibiu tem o menor valor (253), 
# ele vai direto para Sibiu.Em Sibiu, ele olha os vizinhos (Arad, Oradea, Rimnicu Vilcea, Fagaras) e compara suas heurísticas.
# Fagaras vence com 176.De Fagaras, o vizinho com menor heurística é o próprio Bucharest (0).
# ⚠️ Nota importante do livro do Norvig: A busca gulosa é rápida, mas não é ótima. 
# Se você reparar bem, o caminho Arad -> Sibiu -> Fagaras -> Bucharest dá um custo real de 450 km.
# Se utilizássemos o algoritmo $A^*$ (que soma o custo real da estrada com a heurística), 
# o caminho escolhido passaria por Rimnicu Vilcea e Pitesti, resultando em um caminho mais curto de 418 km.
