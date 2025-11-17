class Grafo:
    def __init__(self):
        self.lista_adj = {}

    def adicionar_vertice(self, v):
        if v not in self.lista_adj:
            self.lista_adj[v] = []

    def adicionar_aresta(self, a, b):
        if a not in self.lista_adj:
            self.lista_adj[a] = []
        if b not in self.lista_adj:
            self.lista_adj[b] = []

        if b not in self.lista_adj[a]:
            self.lista_adj[a].append(b)
        if a not in self.lista_adj[b]:
            self.lista_adj[b].append(a)

    def vizinhos_de(self, v):
        return self.lista_adj.get(v, [])

    def __str__(self):
        return str(self.lista_adj)


def busca_largura(grafo, inicio):
    fila_pendentes = [inicio]
    colecao_visitados = {inicio}

    print(f"--> Iniciando a busca em largura a partir de: {inicio}")

    while fila_pendentes:
        atual = fila_pendentes.pop(0)
        print(f"Visitando nó: {atual}")

        for adj in grafo.vizinhos_de(atual):
            if adj not in colecao_visitados:
                colecao_visitados.add(adj)
                fila_pendentes.append(adj)
                print(f"  Inserindo na fila: {adj}")

    print(f"Final da BFS. Visitados: {list(colecao_visitados)}")
    return list(colecao_visitados)


if __name__ == "__main__":
    g = Grafo()
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("A", "C")
    g.adicionar_aresta("B", "D")
    g.adicionar_aresta("B", "E")
    g.adicionar_aresta("C", "F")
    g.adicionar_aresta("E", "F")

    g.adicionar_vertice("G")

    print("Grafo atual:")
    print(g)

    print("\n=== BFS ===")
    busca_largura(g, "A")

    print("\n=== BFS iniciando de vértice isolado ===")
    busca_largura(g, "G")
