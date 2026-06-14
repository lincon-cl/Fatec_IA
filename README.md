# Busca Gulosa (Greedy Search) em Inteligência Artificial

Este repositório contém uma implementação detalhada e explicativa do algoritmo de **Busca Gulosa (Greedy Best-First Search)**, um dos métodos de busca heurística mais conhecidos no campo da Inteligência Artificial.

---

## 📌 O que é a Busca Gulosa?

A Busca Gulosa é um algoritmo de busca informada (ou heurística) utilizado para encontrar caminhos em grafos ou árvores de estados. Ela recebe esse nome porque, a cada passo, toma a decisão que parece ser a **melhor no momento imediato**, sem considerar as consequências a longo prazo ou o custo acumulado até ali.

### Como ela funciona?
Diferente de algoritmos como o de Dijkstra ou o A*, que olham para o custo do caminho já percorrido, a Busca Gulosa foca exclusivamente em chegar o mais rápido possível ao objetivo baseado em uma **função heurística $h(n)$**.

* **Função Heurística $h(n)$:** Estima o custo do nó atual $n$ até o objetivo. Um exemplo clássico é a **distância em linha reta** entre duas cidades.
* **Critério de Escolha:** O algoritmo avalia todos os nós vizinhos disponíveis e escolhe aquele que possui o **menor valor de $h(n)$**.

> 💡 **Em resumo:** Ela se comporta como uma pessoa perdida em uma névoa que, querendo subir uma montanha, sempre escolhe dar o passo na direção que parece subir mais rápido, mesmo que esse caminho leve a um penhasco ou a um beco sem saída.

---

## 🛠️ Detalhes de Funcionamento (Passo a Passo)

1. **Inicialização:** Adiciona o nó inicial à lista de nós a serem explorados (lista aberta/fronteira).
2. **Seleção:** Remove da lista aberta o nó $n$ que possui o menor valor de $h(n)$.
3. **Verificação de Objetivo:** Se $n$ for o estado objetivo, o algoritmo termina e o caminho é retornado.
4. **Expansão:** Caso contrário, move o nó $n$ para a lista de nós já visitados (lista fechada) e expande seus vizinhos.
5. **Atualização da Fronteira:** Para cada vizinho que ainda não foi visitado, calcula-se $h(vizinho)$ e ele é adicionado à lista aberta.
6. **Repetição:** Repete a partir do passo 2 até encontrar o objetivo ou a lista aberta ficar vazia (o que significa que não há solução).

### Exemplo Visual Clássico: Romênia
No problema clássico de encontrar o caminho de **Arad** até **Bucharest**:
* A busca olha para os vizinhos de Arad: Sibiu, Timisoara e Zerind.
* Ela verifica qual dessas cidades está mais perto de Bucharest *em linha reta*.
* Se Sibiu tiver a menor distância em linha reta, o algoritmo vai para Sibiu, ignorando completamente a distância real das estradas que já percorreu.

---

## ⏳ Como e Por Que Ela Foi Criada?

### O Contexto Histórico
Nos anos 1950 e 1960, os pioneiros da computação e da IA (como Allen Newell, Herbert Simon e os criadores do GPS - *General Problem Solver*) perceberam que os computadores sofriam com a **explosão combinatória**. Tentar encontrar caminhos perfeitos em problemas complexos usando busca cega (como Busca em Largura ou Profundidade) exigia memória e processamento que as máquinas da época simplesmente não tinham.

Para resolver isso, os pesquisadores começaram a formalizar o conceito de **Heurísticas** (regras práticas baseadas em intuição humana ou aproximações úteis). 

### A Origem do Conceito "Guloso" (Greedy)
O termo "Guloso" (Greedy) foi cunhado na ciência da computação para descrever uma classe de algoritmos (como o algoritmo de Prim e Kruskal para árvores geradoras mínimas) que resolvem problemas de otimização fazendo a escolha localmente ótima em cada etapa. 

A **Busca Gulosa Baseada em Heurística** surgiu naturalmente como uma simplificação dos estudos que mais tarde geraram o algoritmo **A*** (publicado em 1968 por Peter Hart, Nils Nilsson e Bertram Raphael). Enquanto o A* foi criado para ser matematicamente perfeito combinando custo real + heurística, a Busca Gulosa foi mantida e estudada como uma alternativa focada estritamente em **velocidade e economia de memória**, sacrificando a precisão.

---

## ⚖️ Vantagens e Desvantagens

| Vantagens | Desvantagens |
| :--- | :--- |
| **Altamente Eficiente:** Costuma encontrar uma solução muito mais rápido do que buscas cegas. | **Não é Ótima:** Não garante encontrar o caminho mais curto/mais barato real. |
| **Baixo Consumo de Memória:** Mantém menos nós na fronteira comparado a buscas completas se a heurística for boa. | **Pode Entrar em Loops:** Se não houver controle de nós visitados, pode ficar presa entre dois estados. |
| **Fácil Implementação:** Depende apenas do cálculo da função heurística local. | **Suscetível a Falsos Atalhos:** Pode ser enganada por caminhos que parecem bons no início, mas são bloqueados depois. |

---

## 💻 Exemplo de Implementação (Python)

Aqui está um trecho simples de como a estrutura da busca pode ser implementada utilizando uma fila de prioridade:

```python
import heapq

def busca_gulosa(grafo, inicio, objetivo, heuristica):
    # Fila de prioridade: armazena tuplas (valor_heuristica, no_atual, caminho)
    fronteira = [(heuristica[inicio], inicio, [inicio])]
    visitados = set()

    while fronteira:
        # Pega o nó com a MENOR heurística estimada
        _, no_atual, caminho = heapq.heappop(fronteira)

        if no_atual == objetivo:
            return caminho  # Sucesso!

        if no_atual not in visitados:
            visitados.add(no_atual)
            
            # Explora os vizinhos
            for vizinho in grafo[no_atual]:
                if vizinho not in visitados:
                    heapq.heappush(fronteira, (heuristica[vizinho], vizinho, caminho + [vizinho]))
                    
    return None # Caminho não encontrado