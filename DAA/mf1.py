# Function to build adjacency list from edge list file
def build_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split line into parts
            parts = line.strip().split()
            
            # Skip lines that don't have at least two elements
            if len(parts) < 2:
                continue
            
            # Extract the first two elements as nodes
            node1, node2 = parts[:2]
            
            # Build adjacency list
            if node1 not in adjacency_list:
                adjacency_list[node1] = []
            if node2 not in adjacency_list:
                adjacency_list[node2] = []
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
    return adjacency_list

# Function to find mutual friends
def manual_find_mutual_friends(graph_data, node1, node2):
    neighbors1 = graph_data.get(node1, [])
    neighbors2 = graph_data.get(node2, [])
    mutual_friends = []

    for neighbor in neighbors1:
        if neighbor in neighbors2:
            mutual_friends.append(neighbor)

    return mutual_friends


#1
# # Build adjacency list from file
# file_path = "./synthetic_data.edgelist"  # Replace with the correct path
# adjacency_list = build_adjacency_list(file_path)

# # Test nodes
# node1 = "0"
# node2 = "4"

# # Find mutual friends
# mutual_friends = manual_find_mutual_friends(adjacency_list, node1, node2)
# print(f"Mutual friends between {node1} and {node2}: {mutual_friends}")
