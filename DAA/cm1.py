import networkx as nx
import matplotlib.pyplot as plt

# Function to calculate degree centrality manually
def degree_centrality(graph):
    centrality = {}
    total_nodes = graph.number_of_nodes() - 1
    for node in graph.nodes():
        centrality[node] = len(list(graph.neighbors(node))) / total_nodes
    return centrality

# Function to calculate closeness centrality manually
def closeness_centrality(graph):
    centrality = {}
    for node in graph.nodes():
        shortest_paths = nx.single_source_shortest_path_length(graph, node)
        total_distance = sum(shortest_paths.values())
        if total_distance > 0:
            centrality[node] = (len(shortest_paths) - 1) / total_distance
        else:
            centrality[node] = 0
    return centrality

# Function to calculate betweenness centrality manually
def betweenness_centrality(graph):
    centrality = {node: 0 for node in graph.nodes()}
    for source in graph.nodes():
        shortest_paths = nx.single_source_shortest_path_length(graph, source)
        for target, path_length in shortest_paths.items():
            if source != target:
                for node in nx.shortest_path(graph, source=source, target=target):
                    if node != source and node != target:
                        centrality[node] += 1
    # Normalize by dividing by (n-1)(n-2)
    total_nodes = graph.number_of_nodes()
    normalization_factor = (total_nodes - 1) * (total_nodes - 2)
    for node in centrality:
        centrality[node] /= normalization_factor
    return centrality

# Function to calculate eigenvector centrality manually
def eigenvector_centrality(graph, max_iter=100, tol=1e-06):
    centrality = {node: 1 for node in graph.nodes()}
    for _ in range(max_iter):
        prev_centrality = centrality.copy()
        for node in graph.nodes():
            centrality[node] = sum(prev_centrality[neighbor] for neighbor in graph.neighbors(node))
        # Normalize
        norm = sum(value ** 2 for value in centrality.values()) ** 0.5
        centrality = {node: value / norm for node, value in centrality.items()}
        # Check convergence
        if all(abs(centrality[node] - prev_centrality[node]) < tol for node in graph.nodes()):
            break
    return centrality

# Visualization function
def visualize_centrality(graph, centrality, filename="static/centrality_graph.png"):
    pos = nx.spring_layout(graph)
    node_sizes = [5000 * centrality[node] for node in graph.nodes()]
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, node_size=node_sizes, with_labels=True, cmap=plt.cm.Blues)
    plt.title("Graph with Centrality")
    plt.savefig(filename)
    plt.close()
