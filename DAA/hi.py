import networkx as nx

# Load the dataset
file_path = "./synthetic_data.edgelist"  # Replace with your file path
graph = nx.read_edgelist(file_path, create_using=nx.Graph())

# Function to find mutual friends
def find_mutual_friends(graph, node1, node2):
    # Get neighbors of the two nodes
    neighbors1 = set(graph.neighbors(node1))
    neighbors2 = set(graph.neighbors(node2))
    # Find intersection of the two sets
    mutual_friends = neighbors1.intersection(neighbors2)
    return list(mutual_friends)

# Test the function
node1 = "0"  # Replace with a valid node from your dataset
node2 = "4"  # Replace with a valid node from your dataset
mutual_friends = find_mutual_friends(graph, node1, node2)
print(f"Mutual Friends between {node1} and {node2}: {mutual_friends}")