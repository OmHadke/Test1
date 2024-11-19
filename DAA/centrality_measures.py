import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
file_path = "./synthetic_data.edgelist"  # Replace with your file path
graph = nx.read_edgelist(file_path, create_using=nx.Graph())

# Function to calculate centrality measures
def calculate_centrality_measures(graph):
    # Ensure centrality measures are calculated
    degree_centrality = nx.degree_centrality(graph)
    betweenness_centrality = nx.betweenness_centrality(graph)
    closeness_centrality = nx.closeness_centrality(graph)
    eigenvector_centrality = nx.eigenvector_centrality(graph)
    return {
        "Degree Centrality": degree_centrality,
        "Betweenness Centrality": betweenness_centrality,
        "Closeness Centrality": closeness_centrality,
        "Eigenvector Centrality": eigenvector_centrality,
    }

# Initialize centrality measures
centrality_measures = calculate_centrality_measures(graph)

# Function to visualize centrality
def visualize_top_centralities(graph, centrality, top_n=5):
    top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:top_n]
    top_node_list = [node for node, _ in top_nodes]
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, with_labels=True, node_size=100, font_size=8)
    nx.draw_networkx_nodes(graph, pos, nodelist=top_node_list, node_color='red', node_size=250)
    plt.title("Top Nodes by Centrality")
    plt.show()

# Call visualization for Degree Centrality
print("Top 5 Degree Centrality Nodes:")
print(sorted(centrality_measures["Degree Centrality"].items(), key=lambda x: x[1], reverse=True)[:5])

visualize_top_centralities(graph, centrality_measures["Degree Centrality"])
