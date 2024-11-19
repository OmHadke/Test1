#updated
from flask import Flask, request, render_template, redirect, url_for
import networkx as nx
import community.community_louvain as community_louvain
import matplotlib.pyplot as plt
import os


app = Flask(__name__)
#
STATIC_FOLDER = 'static'
#
UPLOAD_FOLDER = 'uploads'
#
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#
os.makedirs(STATIC_FOLDER, exist_ok=True)
#
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load a default graph (for Mutual Friends functionality)
default_file = "./synthetic_data.edgelist"  # Replace with your file path
graph = nx.read_edgelist(default_file, create_using=nx.Graph())

# Function for Mutual Friends
def find_mutual_friends(graph, node1, node2):
    neighbors1 = set(graph.neighbors(node1))
    neighbors2 = set(graph.neighbors(node2))
    mutual_friends = neighbors1.intersection(neighbors2)
    return list(mutual_friends)

# Function for Community Detection
def detect_communities(graph):
    #partition = community_louvain.best_partition(graph)
    return community_louvain.best_partition(graph)

# Function to visualize communities
def visualize_communities(graph, partition, filename='static/community_graph.png'):
    pos = nx.spring_layout(graph)
    cmap = plt.cm.get_cmap('viridis', max(partition.values()) + 1)
    colors = [cmap(partition[node]) for node in graph.nodes()]
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, node_color=colors, with_labels=True, node_size=50, font_size=8)
    plt.title("Community Detection Visualization")
    plt.savefig(filename)
    plt.close()

# Function for Centrality Measures
def calculate_centrality_measures(graph):
    # 1. Degree Centrality
    degree_centrality = nx.degree_centrality(graph)

    # 2. Betweenness Centrality
    betweenness_centrality = nx.betweenness_centrality(graph)

    # 3. Closeness Centrality
    closeness_centrality = nx.closeness_centrality(graph)

    # 4. Eigenvector Centrality
    eigenvector_centrality = nx.eigenvector_centrality(graph)

    return {
        "Degree Centrality": degree_centrality,
        "Betweenness Centrality": betweenness_centrality,
        "Closeness Centrality": closeness_centrality,
        "Eigenvector Centrality": eigenvector_centrality,
    }


def visualize_top_centralities(graph, centrality, top_n=5):
    top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:top_n]
    top_node_list = [node for node, _ in top_nodes]
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, with_labels=True, node_size=50 , font_size=8)
    nx.draw_networkx_nodes(graph, pos, nodelist=top_node_list, node_color='red', node_size=250)
    plt.title("Top Nodes by Centrality")
    filename = "centrality_graph.png"
    filepath = os.path.join(STATIC_FOLDER,filename)
    plt.savefig(filepath)
    #plt.show()
    plt.close()
    return filepath

# Example: Visualize Top Degree Centrality Nodes
#visualize_top_centralities(graph, calculate_centrality_measures["Degree Centrality"])



# Routes
# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Mutual Friends Route
@app.route('/mutual_friends', methods=['POST'])
def mutual_friends():
    node1 = request.form['node1']
    node2 = request.form['node2']
    if node1 in graph and node2 in graph:
        mutual = find_mutual_friends(graph, node1, node2)
        return render_template('index.html', mutual_friends=mutual, node1=node1, node2=node2)
    else:
        return render_template('index.html', error="One or both nodes not found in the graph.")

# Community Detection Route
@app.route('/community_detection', methods=['POST'])
def community_detection():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        uploaded_graph = nx.read_edgelist(filepath, create_using=nx.Graph())
        partition = detect_communities(uploaded_graph)
        visualize_communities(uploaded_graph, partition ,filename='static/community_graph.png')
        return render_template('index.html', communities=partition, image=url_for('static',filename= 'community_graph.png'))

# Centrality Measures Route
@app.route('/centrality_measures', methods=['POST'])
def centrality_measures():
    centrality_measures = calculate_centrality_measures(graph)
    selected_measure = request.form.get('centrality_measure')
    top_n = int(request.form.get('top_n', 5))  # Default to top 5 nodes

    # Validate the selected measure
    if selected_measure not in centrality_measures:
        return render_template('index.html', error="Invalid centrality measure selected!")

    # Get the centrality data and visualize it
    centrality_data = centrality_measures[selected_measure]
    image_path = visualize_top_centralities(graph, centrality_data, top_n=top_n)

    # Sort top nodes and format for display
    top_nodes = sorted(centrality_data.items(), key=lambda x: x[1], reverse=True)[:top_n]
    formatted_top_nodes = [(node, round(value, 4)) for node, value in top_nodes]

    return render_template(
        'index.html',
        selected_measure=selected_measure,
        top_nodes=formatted_top_nodes,
        image=image_path
    )





#2
# @app.route('/centrality_measures', methods=['POST'])
# def centrality_measures():
#      centrality_measures = calculate_centrality_measures(graph)
# selected_measure = request.form['centrality_measure']
# top_n = int(request.form.get('top_n', 5))  # Default to top 5 nodes

# # Validate the selected measure
# if selected_measure not in centrality_measures:
#      render_template('index.html', error="Invalid centrality measure selected!")

# # Get the centrality data and visualize it
# centrality_data = centrality_measures[selected_measure]
# image_path = visualize_top_centralities(graph, centrality_data, top_n=top_n)

# # Display the results
# top_nodes = sorted(centrality_data.items(), key=lambda x: x[1], reverse=True)[:top_n] 
# return render_template(
#         'index.html',
#         selected_measure=selected_measure,
#         top_nodes=top_nodes,
#         image=image_path )



#1
    # if 'file' not in request.files:
    #     return redirect(url_for('index'))
    # file = request.files['file']
    # if file.filename == '':
    #     return redirect(url_for('index'))
    # if file:
    #     filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #     file.save(filepath)
    #     uploaded_graph = nx.read_edgelist(filepath, create_using=nx.Graph())
    #     centrality = calculate_centrality_measures(uploaded_graph)

    #     # Get top nodes for each centrality measure
    #     top_centralities = {
    #         measure: sorted(values.items(), key=lambda x: x[1], reverse=True)[:5]
    #         for measure, values in centrality.items()
    #     }
    #     return render_template('index.html', centralities=top_centralities)


if __name__ == '__main__':
    app.run(debug=True)
