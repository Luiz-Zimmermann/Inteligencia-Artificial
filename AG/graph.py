import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def draw_graph(population, cities):
    g = nx.Graph()
    g.add_nodes_from(cities)

    print(g.nodes())

    short_path = population.pop(0)
    print("Melhor caminho: ", short_path.rotas)


    tam = len(cities) * len(population)
    edges = None
    for edge in population:
        edges = np.append(edges, edge.rotas)

    edges = np.append(edges, short_path.rotas)
    edges = np.delete(edges,0)
    print(tam)
    print(edges)

    for i in range(len(edges)-1):
        if i <= tam-1:
            node1 = edges[i]
            node2 = edges[i + 1]
            g.add_edge(node1, node2, color='b', label='cu', weight=4)
            if i == tam:
                g.add_edge(edges[len(edges) - 1], edges[0], color='b', label="cu", weight=4)
        else:
            node1 = edges[i]
            node2 = edges[i + 1]
            g.add_edge(node1, node2, color='r', label='cu', weight=2)


    g.add_edge(edges[len(edges) - 1], edges[tam], color='r', label="cu", weight=2)

    colors = nx.get_edge_attributes(g, 'color').values()
    distances = nx.get_edge_attributes(g, 'weight')
    pos = nx.spring_layout(g)

    nx.draw(g, edge_color=colors, with_labels="true")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=distances)
    plt.axis('off')
    plt.show()



# testes
if __name__ == "__main__":
    g = nx.Graph()
    path = np.array([1,2,3,4,5])
    tam = len(path) * 4
    g.add_nodes_from(path)

    print(g.nodes())

    edges = np.append(np.array([2,1,5,4,3]),np.array([5,1,3,4,2]))
    edges = np.append(edges, np.array([2, 5, 3, 4, 1]))
    edges = np.append(edges, np.array([2, 5, 3, 4, 1]))
    edges = np.append(edges, path)
    print(edges)
    for i in range(len(edges)-1):
        if i <= tam-1:
            node1 = edges[i]
            node2 = edges[i + 1]
            g.add_edge(node1, node2, color='b', label='cu', weight=4)
            if i == tam:
                g.add_edge(edges[len(edges) - 1], edges[0], color='b', label="cu", weight=4)
        else:
            node1 = edges[i]
            node2 = edges[i + 1]
            g.add_edge(node1, node2, color='r', label='cu', weight=2)


    g.add_edge(edges[len(edges) - 1], edges[tam], color='r', label="cu", weight=2)
    print(g.edges())


    colors = nx.get_edge_attributes(g, 'color').values()
    distances = nx.get_edge_attributes(g, 'weight')
    pos = nx.spring_layout(g)

    nx.draw(g, edge_color=colors, with_labels="true")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=distances)
    plt.axis('off')
    plt.show()