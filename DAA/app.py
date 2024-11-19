
from flask import Flask, redirect, render_template, request, url_for
from collections import defaultdict  # Create default dictionaries for adjacency lists
#
import os
import networkx as nx
from cd1 import manual_community_detection, build_graph
from cm1 import degree_centrality, closeness_centrality, betweenness_centrality, eigenvector_centrality, visualize_centrality
import matplotlib.pyplot as plt

app = Flask(__name__)
#2
UPLOAD_FOLDER = 'upload1'
STATIC_FOLDER = 'static1'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#

# Home route
# @app.route('/')
# def index():
#     return render_template('new.html')

## Function to build an adjacency list from an edgelist file

def build_adjacency_list(filename):

    adjacency_list = {}

    with open(filename, 'r') as file:

        for line in file:

            node1, node2 = line.strip().split()

            if node1 not in adjacency_list:

                adjacency_list[node1] = set()

            if node2 not in adjacency_list:

                adjacency_list[node2] = set()

            adjacency_list[node1].add(node2)

            adjacency_list[node2].add(node1)

    return adjacency_list


# Function to find mutual friends between two nodes

def find_mutual_friends(adjacency_list, node1, node2):

    if node1 in adjacency_list and node2 in adjacency_list:

        mutual_friends = adjacency_list[node1].intersection(adjacency_list[node2])

        return list(mutual_friends)

    return []


@app.route('/', methods=['GET', 'POST'])

def upload_and_find_friends():

    error = None

    adjacency_list = None

    mutual_friends = None

    node1 = None

    node2 = None


    if request.method == 'POST':

        file = request.files.get('edgelist_file')

        node1 = request.form.get('node1')

        node2 = request.form.get('node2')


        if file:

            # Save the uploaded file temporarily

            filepath = os.path.join('uploads', file.filename)

            file.save(filepath)


            # Build the adjacency list from the uploaded file

            adjacency_list = build_adjacency_list(filepath)


            # Find mutual friends

            mutual_friends = find_mutual_friends(adjacency_list, node1, node2)


            # Clean up the uploaded file if needed

            os.remove(filepath)


    return render_template('new.html', error=error, adjacency_list=adjacency_list, mutual_friends=mutual_friends, node1=node1, node2=node2)

#2
# Function to visualize the graph with communities
def visualize_communities(graph, partition, filename="static/community_graph.png"):

    partition = {node: int(community) for node, community in partition.items()}

    pos = nx.spring_layout(graph)  # Generate graph layout
    max_community = max(int(community) for community in partition.values())
    cmap = plt.cm.get_cmap('viridis', max_community + 1)
    #cmap = plt.cm.get_cmap('viridis', max(partition.values()) + 1)  # Generate colors for communities
    colors = [cmap(partition[node]) for node in graph.nodes()]  # Assign colors to nodes

    # Plot the graph
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, node_color=colors, with_labels=True, node_size=200, font_size=10)
    plt.title("Community Detection Visualization")
    plt.savefig(filename)  # Save the graph as an image
    plt.close()  # Close the plot to free memory


# Community detection route
@app.route('/community_detection', methods=['POST'])
def community_detection():
    if 'file' not in request.files:
        return redirect(url_for('new'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('new'))
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    try:
        # Build the graph and detect communities
        graph = build_graph(filepath)
        communities = manual_community_detection(graph)

        # Visualize the graph with communities
        image_path = os.path.join(STATIC_FOLDER, "community_graph.png")
        visualize_communities(graph, communities, filename=image_path)

        # Render the results
        return render_template(
            'new.html',
            communities=communities,
            image=url_for('static', filename='community_graph.png')
        )
    except Exception as e:
        return render_template('new.html', error=f"Error during community detection: {str(e)}")


#cm1
@app.route('/centrality', methods=['POST'])
def centrality():
    if 'file' not in request.files:
        return redirect(url_for('new'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('new'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        graph = nx.read_edgelist(filepath, create_using=nx.Graph())
        
        # Calculate centrality measures
        degree = degree_centrality(graph)
        closeness = closeness_centrality(graph)
        betweenness = betweenness_centrality(graph)
        eigenvector = eigenvector_centrality(graph)

         # Visualize centrality
        visualize_centrality(graph, degree, filename=os.path.join(STATIC_FOLDER, "centrality_graph.png"))

        return render_template(
            'new.html',
            degree=degree,
            closeness=closeness,
            betweenness=betweenness,
            eigenvector=eigenvector,
            image=url_for('static', filename='centrality_graph.png')
        )
    except Exception as e:
        return render_template('new.html', error=f"Error during centrality calculation: {str(e)}")



#3ep1
# Global variables to store the graph and adjacency list
graph = None
adjacency_list = None

# @app.route('/')
# def index():
#     return render_template('new.html')

# Function to build adjacency list from edge list file
def build_adjacency_list(file_path):
    adjacency_list = defaultdict(list)
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:  # Ensure valid edge format
                node1, node2 = parts
                adjacency_list[node1].append(node2)
                adjacency_list[node2].append(node1)
    return adjacency_list

# Upload route to load the graph
@app.route('/upload', methods=['POST'])
def upload_graph():
    global graph, adjacency_list

    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        # Build graph and adjacency list
        graph = nx.read_edgelist(filepath, create_using=nx.Graph())
        adjacency_list = build_adjacency_list(filepath)
        return render_template('new.html', message="Graph uploaded successfully!")
    except Exception as e:
        return render_template('new.html', error=f"Error uploading graph: {str(e)}")

# Function to predict edges using common neighbors
def predict_edge(adjacency_list, node1, node2):
    if node1 not in adjacency_list or node2 not in adjacency_list:
        return 0, []  # Return score 0 and an empty list if nodes are invalid

    neighbors1 = set(adjacency_list[node1])
    neighbors2 = set(adjacency_list[node2])

    # Calculate common neighbors
    common_neighbors = neighbors1.intersection(neighbors2)
    score = len(common_neighbors)  # Edge prediction score

    return score, list(common_neighbors)

# Edge prediction route
@app.route('/predict', methods=['POST'])
def edge_prediction():
    global adjacency_list

    if adjacency_list is None:
        return render_template('new.html', error="No graph uploaded. Please upload a graph first.")

    node1 = request.form['node1']
    node2 = request.form['node2']

    try:
        # Perform edge prediction
        score, common_neighbors = predict_edge(adjacency_list, node1, node2)
        return render_template(
            'new.html',
            node1=node1,
            node2=node2,
            score=score,
            common_neighbors=common_neighbors
        )
    except Exception as e:
        return render_template('new.html', error=f"Error during edge prediction: {str(e)}")




if __name__ == '__main__':
    app.run(debug=True)