import networkx as nx
import random


COUNT = 10
NUM_VERTICES = 1000
NUM_EDGES = 2000
WEIGHT_RANGE = (1,100)


def generate_random_graph(num_vertices, num_edges, weight_range):
    G = nx.gnm_random_graph(num_vertices, num_edges)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(*weight_range)
    return G

def write_graph_to_file(G, file_path, mode = 'a', for_website = False):
    with open(file_path, mode=mode) as file:
        for (u, v, data) in G.edges(data=True):
            file.write(f"{u}{'-' if for_website else ' '}{v}{' ' + str(data['weight']) if not for_website else ''}\n")
        file.write('\n')

def main():
    for i in range(COUNT):
        write_graph_to_file(
            generate_random_graph(
                NUM_VERTICES,
                NUM_EDGES,
                WEIGHT_RANGE
                ),
            'input.txt'
            )
  
if __name__ == "__main__":
    main()