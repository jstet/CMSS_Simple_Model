def col_nodes_state(g):
    # create empty list for node colors
    node_color = []
    # for each node in the graph
    for node in g.nodes(data=True):
        # if the node has the attribute group1
        if node[1]["state"] == 1:
            node_color.append('blue')
        else:
            node_color.append('red')
    return node_color


def col_nodes_phi(g):
    # create empty list for node colors
    node_color = []
    # for each node in the graph
    for node in list(g.nodes):
        if g.nodes[node]["state"] != 1:
            # if the node has the attribute group1
            if len(g.adj[node]) == 0:
                node_color.append('red')
                continue
            if g.nodes[node]["phi"] < 1/len(g.adj[node]):
                node_color.append('green')
            else:
                node_color.append('red')
        else:
            node_color.append('blue')
    return node_color
