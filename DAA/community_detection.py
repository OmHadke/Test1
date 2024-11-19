import networkx as nx
import matplotlib.pyplot as plt
#import community as community_louvain
import community.community_louvain as community_louvain
print(community_louvain.__name__)  # Should output: 'community_louvain'


# Load the dataset
file_path = "./synthetic_data.edgelist"  # Replace with your file path
graph = nx.read_edgelist(file_path, create_using=nx.Graph())

# Perform Community Detection using Louvain method
def detect_communities(graph):
    # Partition the graph into communities
    partition = community_louvain.best_partition(graph)
    return partition

# Get communities
communities = detect_communities(graph)

# Print community assignments
print("Node to Community Mapping:")
for node, community in communities.items():
    print(f"Node {node}: Community {community}")

# Visualize the graph with community colors
def visualize_communities(graph, partition):
    # Assign colors to nodes based on community
    pos = nx.spring_layout(graph)  # Layout for nodes
    cmap = plt.cm.get_cmap('viridis', max(partition.values()) + 1)
    colors = [cmap(partition[node]) for node in graph.nodes()]
    
    # Draw the graph
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, node_color=colors, with_labels=True, node_size=200, font_size=10)
    plt.title("Community Detection Visualization")
    plt.show()

# Visualize the graph
visualize_communities(graph, communities)
