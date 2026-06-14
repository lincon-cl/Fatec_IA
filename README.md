# Busca A* (A-Estrela / A-Star) em Inteligência Artificial

Este repositório contém uma implementação detalhada, comentada e explicativa do algoritmo de **Busca A***, um dos algoritmos de busca de caminho e travessia de grafos mais eficientes e amplamente utilizados no mundo da Inteligência Artificial e no desenvolvimento de jogos.

---

## 📌 O que é a Busca A*?

O A* é um algoritmo de busca informada (heurística) que encontra o **caminho mais curto real** entre um nó inicial e um nó objetivo. 

Diferente da Busca Gulosa (que foca apenas no que falta para chegar ao destino) e do Algoritmo de Dijkstra (que foca apenas no custo já percorrido), o A* combina o melhor dos dois mundos. Ele é considerado **ótimo** (garante o menor caminho) e **completo** (sempre encontra uma solução, se ela existir), desde que a heurística utilizada seja admissível.

### A Equação Mágica: $f(n) = g(n) + h(n)$
O segredo do A* está em como ele avalia qual nó expandir a seguir. Para cada nó $n$, ele calcula uma função de avaliação $f(n)$:

* **$g(n)$:** O custo real do caminho do nó inicial até o nó atual $n$. (Evita que o algoritmo tome caminhos longos passados).
* **$h(n)$:** O custo estimado (heurística) do nó atual $n$ até o objetivo. (Guia o algoritmo na direção certa).
* **$f(n)$:** O custo total estimado do caminho mais barato que passa pelo nó $n$.

> 💡 **Em resumo:** O A* escolhe o próximo passo olhando para trás ($g$) para ver o quanto já gastou, e olhando para frente ($h$) para estimar o quanto falta, escolhendo sempre o nó com o menor $f(n)$ total.

---

## 🛠️ Detalhes de Funcionamento (Passo a Passo)

1. **Inicialização:** Cria-se duas listas:
   * `Fronteira` (Lista Aberta): nós que foram descobertos, mas ainda não avaliados. Começa com o nó inicial.
   * `Visitados` (Lista Fechada): nós que já foram avaliados. Começa vazia.
2. **Seleção:** Escolhe o nó $n$ da lista aberta que possui o **menor valor de $f(n)$**.
3. **Condição de Parada:** Se o nó selecionado for o objetivo, o caminho foi encontrado. O algoritmo reconstrói o caminho de volta e encerra.
4. **Expansão:** Move o nó $n$ para a lista de visitados e analisa todos os seus vizinhos acessíveis:
   * Se o vizinho já estiver na lista de visitados com um custo menor, ele é ignorado.
   * Calcula-se o $g(vizinho)$ temporário ($g(n) + \text{custo da aresta para o vizinho}$).
   * Se esse novo caminho para o vizinho for mais curto do que qualquer caminho anterior (ou se ele não estiver na lista aberta):
     * Atualiza o pai do vizinho para $n$.
     * Grava os valores de $g(vizinho)$, $h(vizinho)$ e calcula $f(vizinho) = g + h$.
     * Adiciona o vizinho à lista aberta (se ainda não estiver lá).
5. **Repetição:** Volta para o passo 2. Se a lista aberta esvaziar e o objetivo não for alcançado, não há caminho possível.

---

## ⏳ Como e Por Que Ele Foi Criado?

### O Contexto Histórico (1968)
A história do A* está diretamente ligada ao desenvolvimento da robótica. Nos anos 1960, pesquisadores do *Stanford Research Institute* (SRI) estavam construindo o **Shakey, o Robô**, o primeiro robô móvel genérico capaz de raciocinar sobre suas próprias ações.



Para que o Shakey pudesse navegar por salas cheias de obstáculos, ele precisava de um algoritmo que encontrasse rotas eficientes. Inicialmente, a equipe tentou usar uma versão modificada do algoritmo de Dijkstra (criado em 1956). Embora o Dijkstra encontrasse o caminho perfeito, ele se expandia radialmente em todas as direções ("busca cega"), gastando muito tempo de processamento e memória computando caminhos na direção oposta ao objetivo.

### A Junção de Forças
Três pesquisadores foram fundamentais para transformar essa realidade:
* **Peter Hart** percebeu que podiam usar estimativas estatísticas (heurísticas) para direcionar a busca.
* **Nils Nilsson** sugeriu uma forma de usar a geometria do ambiente para acelerar o processo.
* **Bertram Raphael** ajudou a consolidar a estrutura de dados.

Eles descobriram que combinando o custo acumulado de Dijkstra ($g$) com uma estimativa de linha reta de formato guloso ($h$), e provando matematicamente que se $h$ nunca superestimasse o custo real (heurística admissível), o algoritmo seria **perfeitamente ótimo**. 

Eles chamaram essa versão aprimorada de algoritmo **A**. Como ele provou ser estatisticamente superior a qualquer outra extensão, eles adicionaram o caractere estrela (`*`), que na computação frequentemente denota otimalidade ou fechamento absoluto. Assim nasceu o **A*** em 1968.

---

## ⚖️ A* vs Busca Gulosa

| Característica | Busca Gulosa | Busca A* |
| :--- | :--- | :--- |
| **Função de Seleção** | $f(n) = h(n)$ | $f(n) = g(n) + h(n)$ |
| **Garantia de Caminho Curto** | Não. Pode pegar atalhos ruins. | Sim (É Ótimo se $h$ for admissível). |
| **Velocidade** | Geralmente mais rápida (avalia menos nós). | Pode ser um pouco mais lenta, mas é muito mais precisa. |
| **Uso em Jogos** | Raramente usada para caminhos críticos. | O padrão da indústria para *pathfinding* de NPCs. |

---

## 💻 Exemplo de Implementação (Python)

Uma implementação simplificada do A* em uma grade 2D (onde a heurística comum é a Distância de Manhattan):

```python
import heapq

def heuristica_manhattan(a, b):
    # (x1, y1) e (x2, y2)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def busca_a_estrela(grade, inicio, objetivo):
    # Fila de prioridade: (f_score, no_atual)
    lista_aberta = []
    heapq.heappush(lista_aberta, (0, inicio))
    
    # Dicionários para rastrear caminhos e custos
    veio_de = {}
    g_score = {inicio: 0}
    f_score = {inicio: heuristica_manhattan(inicio, objetivo)}
    
    while lista_aberta:
        _, atual = heapq.heappop(lista_aberta)
        
        if atual == objetivo:
            # Reconstrói o caminho completo
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            return caminho[::-1] # Retorna o caminho invertido (do início ao fim)
            
        # Assumindo movimentos nas 4 direções cardinais (cima, baixo, esquerda, direita)
        for vizinho in obter_vizinhos(atual, grade):
            # Custo do movimento para o vizinho é sempre 1 nesta grade
            g_temporario = g_score[atual] + 1 
            
            if g_temporario < g_score.get(vizinho, float('inf')):
                # Este caminho para o vizinho é o melhor mapeado até agora!
                veio_de[vizinho] = atual
                g_score[vizinho] = g_temporario
                f_score[vizinho] = g_temporario + heuristica_manhattan(vizinho, objetivo)
                
                if vizinho not in [item[1] for item in lista_aberta]:
                    heapq.heappush(lista_aberta, (f_score[vizinho], vizinho))
                    
    return None # Não encontrou caminho

def obter_vizinhos(no, grade):
    # Implementação interna para obter células válidas vizinhas na grade
    pass
