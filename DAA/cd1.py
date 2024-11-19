import networkx as nx

# Function to calculate modularity
def calculate_modularity(graph, partition, degrees, m):
    modularity = 0
    for node, community in partition.items():
        degree = degrees[node]
        in_degree = sum(1 for neighbor in graph.neighbors(node) if partition[neighbor] == community)
        modularity += (in_degree / m) - (degree / (2 * m))**2
    return modularity

# Louvain-like community detection
def manual_community_detection(graph, threshold=0.0001):
    degrees = dict(graph.degree())
    m = sum(degrees.values()) / 2  # Total edge weight (for unweighted graphs, it's just |E|)

    # Initialize each node as its own community
    partition = {node: int(node) for node in graph.nodes()}
    improvement = True

    while improvement:
        improvement = False
        for node in graph.nodes():
            current_community = partition[node]
            best_community = current_community
            best_gain = 0

            # Test moving node to each neighbor's community
            for neighbor in graph.neighbors(node):
                neighbor_community = partition[neighbor]
                if neighbor_community != current_community:
                    # Calculate modularity gain
                    delta_modularity = (
                        sum(1 for n in graph.neighbors(node) if partition[n] == neighbor_community) / m
                        - (degrees[node] * degrees[neighbor]) / (2 * m)
                    )
                    if delta_modularity > best_gain:
                        best_gain = delta_modularity
                        best_community = neighbor_community

            # Move to the best community
            if best_gain > threshold:
                partition[node] = best_community
                improvement = True

    return partition

# Build the graph from an edge list
def build_graph(file_path):
    graph = nx.read_edgelist(file_path, create_using=nx.Graph())
    return graph
