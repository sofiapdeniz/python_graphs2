class Grafo:
    def __init__(self):
        self.lista_adj = {}

    def adicionar_vertice(self, v):
        if v not in self.lista_adj:
            self.lista_adj[v] = []

    def adicionar_aresta(self, x, y):
        if x not in self.lista_adj:
            self.lista_adj[x] = []
        if y not in self.lista_adj:
            self.lista_adj[y] = []

        if y not in self.lista_adj[x]:
            self.lista_adj[x].append(y)
        if x not in self.lista_adj[y]:
            self.lista_adj[y].append(x)

    def vizinhos_de(self, v):
        return self.lista_adj.get(v, [])

    def __str__(self):
        return str(self.lista_adj)


def menor_caminho_bfs(grafo, origem, alvo):
    fila_busca = [(origem, [origem])]
    visitados = set([origem])

    while fila_busca:
        atual, rota_atual = fila_busca.pop(0)

        if atual == alvo:
            return rota_atual

        for adj in grafo.vizinhos_de(atual):
            if adj not in visitados:
                visitados.add(adj)
                nova_rota = rota_atual + [adj]
                fila_busca.append((adj, nova_rota))

    return []


if __name__ == "__main__":
    g = Grafo()
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("A", "C")
    g.adicionar_aresta("B", "D")
    g.adicionar_aresta("B", "E")
    g.adicionar_aresta("C", "F")
    g.adicionar_aresta("E", "F")
    g.adicionar_aresta("F", "G")
    g.adicionar_aresta("E", "H")

    print("Grafo utilizado:")
    print(g)

    print("\n### Menor Caminho BFS ###")

    pares_teste = [
        ("A", "G"),
        ("D", "G"),
        ("A", "H"),
        ("A", "Z")
    ]

    for o, d in pares_teste:
        resultado = menor_caminho_bfs(g, o, d)
        print(f"Caminho de {o} até {d}: {resultado}")
