import heapq

class aresta:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso


class vertice:
    def __init__(self, identificador):
        self.identificador = identificador
        self.arestas = []
        
    def adicionar_aresta(self, destino, peso):
        nova_aresta = aresta(destino, peso)
        self.arestas.append(nova_aresta)
        
class grafo:
    def __init__(self):
        self.vertices={}
        
    def adicionar_vertice(self, identificador):
        if identificador not in self.vertices:
            self.vertices[identificador]=vertice(identificador)
            
    def criar_conexao(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        self.vertices[origem].adicionar_aresta(destino, peso)
        
    def dijkstra(self, inicio):
        distancias={vertice: float('inf') for vertice in self.vertices}
        distancias[inicio]=0
        visitados=set()
        
        ordem_resolucao=[]
        predecessores={vertice: None for vertice in self.vertices}
        lista=[(0, inicio)]
        while lista:
            distancia_atual, vertice_atual=heapq.heappop(lista)
            
            if vertice_atual in visitados:
                continue
            
            visitados.add(vertice_atual)
            ordem_resolucao.append(vertice_atual)
            for aresta in self.vertices[vertice_atual].arestas:
                vizinho=aresta.destino
                peso=aresta.peso
                nova_distancia=distancia_atual+peso
                
                if nova_distancia<distancias[vizinho]:
                    distancias[vizinho]=nova_distancia
                    predecessores[vizinho]=vertice_atual
                    heapq.heappush(lista, (nova_distancia, vizinho))
        return ordem_resolucao, distancias, predecessores
        
        
        
    

# Test code
if __name__ == "__main__":
    g = grafo()
    
    # Construindo um novo mapa mais complexo (6 vértices)
    g.criar_conexao('S', 'A', 4)
    g.criar_conexao('S', 'B', 2)
    g.criar_conexao('A', 'C', 5)
    g.criar_conexao('A', 'D', 10)
    g.criar_conexao('B', 'A', 1)  # Atalho escondido de B para A!
    g.criar_conexao('B', 'C', 8)
    g.criar_conexao('C', 'D', 2)
    g.criar_conexao('C', 'T', 6)
    g.criar_conexao('D', 'T', 3)
    
    origem = 'S'
    ordem, dist, pred = g.dijkstra(origem)
    
    # 1. Imprime o vetor de Vértices na ordem exata de resolução
    print(f"Vetor de Vértices (Ordem de determinação): {ordem}\n")
    
    # --- NOVA ADIÇÃO: Resumo das distâncias totais ---
    print(f"=== Resumo de Custos Totais (Saindo de {origem}) ===")
    for v in ordem:
        print(f"Custo total até {v}: {dist[v]}")
    print("==================================================\n")
    
    # 2. Varre cada vértice para mostrar o trajeto detalhado
    print("=== Detalhamento do Trajeto por Vértice ===")
    for v in ordem:
        print(f"Destino: [{v}]")
        
        # Reconstrói o caminho percorrido
        caminho_reverso = []
        passo_atual = v
        
        while passo_atual is not None:
            caminho_reverso.append(passo_atual)
            passo_atual = pred[passo_atual]
        
        caminho_final = caminho_reverso[::-1]
        caminho_formatado = " -> ".join(str(no) for no in caminho_final)
        
        print(f"  -> Custo da viagem: {dist[v]}")
        print(f"  -> Rota utilizada: {caminho_formatado}")
        print("-" * 50)
