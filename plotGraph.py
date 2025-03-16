"""
Courtesy of Claude, GPT and perplexity!

This is a simple script which I used to all of the graphs in all 3 assignments,
quite customizable and easy to use. I hope it helps you too!
"""
import networkx as nx
import matplotlib.pyplot as plt

# Set up the plot
plt.figure(figsize=(4, 3))


def create_graph(directed: bool = False):
    """
    Create a graph object based on the directed flag.

    Args:
        directed (bool): whether the graph is directed or not

    Retruns:
        nx.Graph object
    """
    if directed:
        return nx.DiGraph()
    return nx.Graph()


def add_nodes(G: nx.Graph, num_nodes: int):
    """
    Add nodes to the passed graph object.

    Args:
        G (nx.Graph): the Graph to add nodes to
        num_nodes (int): add `num_nodes` number of nodes to the graph (1-base-indexing)

    Retruns:
        G (nx.Graph): the Graph with added nodes
    """
    # create a simple list
    nodes = range(1, num_nodes+1)
    G.add_nodes_from(nodes)

    return G


def draw_nodes(G: nx.Graph, pos: dict, node_size: int = 300, 
               node_color: str = 'white', edgecolors: str = 'black', 
               linewidths: int = 2):
    """
    Draw nodes with the specified parameters.

    Args:
        G (nx.Graph): the Graph to draw nodes from
        pos (dict): the position of the nodes
        node_size (int, default=300): the size of the nodes
        node_color (str, default='white'): the color of the nodes
        edgecolors (str, default='black'): the color of the border of the nodes (NOT THE EDGES)
        linewidths (int, default=2): the width of the border of the nodes

    Retruns:
        None
    """
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes(), node_size=node_size, 
                           node_color=node_color, edgecolors=edgecolors, linewidths=linewidths)


def add_node_labels(G: nx.Graph, pos: dict, node_display_labels: dict, font_size: int = 12,
                    font_color: str = 'black', ha: str = 'center', va: str = 'center'):
    """
    Add labels to the nodes.

    Args:
        G (nx.Graph): the Graph to add labels to
        pos (dict): the position of the nodes
        node_display_labels (dict): the labels to display on the nodes
        font_size (int, default=12): the font size of the labels
        font_color (str, default='black'): the color of the labels
        ha (str, default='center'): horizontal alignment of the labels
        va (str, default='center'): vertical alignment of the labels

    Retruns:
        None
    """
    for node in G.nodes():
        # get position
        x, y = pos[node]
        # get label
        label = node_display_labels[node]
        plt.text(x, y, label, fontsize=font_size, color=font_color,
                 horizontalalignment=ha, verticalalignment=va)


def add_node_extra(pos: dict, node_values: dict, font_size: int = 10,
                   font_color: str = '#C84D4C', font_weight: str = 'bold'):
    """
    Add extra information to the nodes.

    NOTE: this function will always need some modification in the for-loop
    according to your needs.

    Args:
        pos (dict): the position of the nodes
        node_values (dict): the extra information to display on the nodes
        font_size (int, default=10): the font size of the extra information
        font_color (str, default='#C84D4C'): the color of the extra information (I like this color)
        font_weight (str, default='bold'): the weight of the extra information

    Retruns:
        None
    """
    for node, value in node_values.items():
        x = pos[node][0]
        y = pos[node][1] + 0.05

        plt.text(x, y, value, fontsize=font_size, color=font_color,
                 fontweight=font_weight)


def add_edges(G: nx.Graph, edges: list):
    """
    Add edges to the passed graph object.

    Args:
        G (nx.Graph): the Graph to add edges to
        edges (list): list of tuples representing edges

    Retruns:
        G (nx.Graph): the Graph with added edges
    """
    G.add_edges_from(edges)

    return G


def draw_edges(G: nx.Graph, pos: dict, edges: list, edge_rad: dict, edge_width: int = 2):
    """
    Draw edges with the specified parameters.

    Args:
        G (nx.Graph): the Graph to draw edges from
        pos (dict): the position of the nodes
        edges (list): list of tuples representing edges
        edge_rad (dict): the rotation angle of the edges
        edge_width (int, default=2): the width of the edges

    Retruns:
        None
    """
    for edge in edges:
        nx.draw_networkx_edges(G, pos, edgelist=[edge], width=edge_width, 
                               connectionstyle=f'arc3,rad={edge_rad[edge]}')


def add_edge_extra(pos: dict, edge_values: dict, font_size: int = 10,
                   font_color: str = '#C84D4C', font_weight: str = 'bold'):
     """
     Add extra information to the edges.
    
     NOTE: this function will always need some modification in the for-loop
     according to your needs.
    
     Args:
          pos (dict): the position of the nodes
          edge_values (dict): the extra information to display on the edges
          font_size (int, default=10): the font size of the extra information
          font_color (str, default='#C84D4C'): the color of the extra information
          font_weight (str, default='bold'): the weight of the extra information
    
     Retruns:
          None
     """
     for edge, value in edge_values.items():
          x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2
          y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2 + 0.05
          plt.text(x, y, value, fontsize=font_size, color=font_color,
                  fontweight=font_weight)


def main():

    # get graph object
    G = create_graph(directed=True)

    # add nodes
    G = add_nodes(G, 4)

    # draw nodes
    pos = {
        1: (0.0, 0.0),
        2: (0.3, 0.3),
        3: (0.3, -0.3),
        4: (-0.3, 0.0)
    }
    draw_nodes(G, pos, node_size=300, node_color='white', edgecolors='black', linewidths=2)

    # add node labels
    node_display_labels = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
    }
    add_node_labels(G, pos, node_display_labels, font_size=12, font_color='black', 
                    ha='center', va='center')

    # # extra node info
    # node_values = {
    #     1: "$e_A$",
    #     2: "$e_B$",
    #     3: "$e_C$",
    #     4: "$e_D$"
    # }
    # add_node_extra(pos, node_values, font_size=10, font_color='#C84D4C', font_weight='bold')
    

    # add edges
    edges = [
        (1, 2), (1, 4),
        (2, 3),
        (3, 1),
        (4, 1)
    ]
    G = add_edges(G, edges)

    # define rotation angles (can be commented out if straight edges are needed)
    edge_rad = {}
    for edge in edges:
        if edge in [(1, 2), (2, 3), (3, 1)]:
            edge_rad[edge] = -0.3  # Negative for outward arcs in this cycle
        else:
            edge_rad[edge] = 0.3   # Default for other edges

    # draw edges
    draw_edges(G, pos, edges, edge_rad, edge_width=2)

    # # extra edge info
    # edge_values = {
    #     (1, 2): "$r$", (1, 4): "$r$",
    #     (2, 3): "$r$",
    #     (3, 1): "$r$",
    #     (4, 1): "$r$"
    # }
    # add_edge_extra(pos, edge_values, font_size=10, font_color='#C84D4C', font_weight='bold')

    # # set x/y limits (might be needed if the content cuts out)
    # plt.ylim(-0.25, 0.4)
    # plt.xlim(-0.4, 0.4)

    # Remove axis
    plt.axis('off')
    # Display the graph
    plt.tight_layout()
    plt.savefig("plotGraph.png", dpi=300)

    print("Graph created and saved successfully as 'plotGraph.png'!")


if __name__ == '__main__':
    main()
