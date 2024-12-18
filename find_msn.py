import networkx as nx
import math
from os import remove, listdir

FOR_WEBSITE = False 

def write_graph_to_file(G, file_path, mode = 'a', for_website = False):
    with open(file_path, mode=mode) as file:
        for (u, v, data) in G.edges(data=True):
            file.write(f"{u}{'-' if for_website else ' '}{v}{' ' + str(data['weight']) if not for_website else ''}\n")
        file.write('\n')
        
def read_graphs_from_file(file_path):
    graphs = []
    G = nx.Graph()
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line == '\n':
            graphs.append(G)
            G = nx.Graph()
            continue
        u, v, w = map(int, line.split())
        G.add_edge(u, v, weight=w)
    return graphs

def prim_mst(G):
    return nx.minimum_spanning_tree(G, algorithm='prim')

def modify_mst(G, L):
    for node in list(G.nodes):
        while G.degree(node) > 3:
            edges = list(G.edges(node, data=True))
            edges.sort(key=lambda x: x[2]['weight'], reverse=True)
            G.remove_edge(edges[0][0], edges[0][1])

    leaves = [node for node in G.nodes if G.degree(node) == 1]
    while len(leaves) > L:
        leaf = leaves.pop(0)
        neighbors = list(G.neighbors(leaf))
        if neighbors:
            G.remove_edge(leaf, neighbors[0])
        leaves = [node for node in G.nodes if G.degree(node) == 1]

    return G


def find_mst(G, for_website = False):
    L = math.floor((len(G.nodes) - 10) / 10)
    mst = prim_mst(G)
    modified_mst = modify_mst(mst, L)
    write_graph_to_file(modified_mst, 'output.txt', 'a', for_website=for_website)

def main():
    if 'output.txt' in listdir(): 
        remove('output.txt')
        
    graphs = read_graphs_from_file('input.txt')
    print(len(graphs))
    
    for graph in graphs:
        find_mst(graph, for_website=True)
    
if __name__ == "__main__":
    main()