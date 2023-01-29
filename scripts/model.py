import networkx as nx
import random


def simple_model(n, z, phi, upper_phi):
    # uniform random graph
    g = nx.fast_gnp_random_graph(n, z/n)
    # population is initially all-off
    nx.set_node_attributes(g, 0, "state")

    # each agent is assigned a threshold  drawn at random from a distribution
    for i in list(g.nodes):
        attrs = {i: {"phi": phi}}
        nx.set_node_attributes(g, attrs)

    # at time t = 0 a small fraction of vertices is switched on, fraction equals uppercase phi
    innovators = random.choices(list(g.nodes), k=upper_phi)
    attrs = {i: {"state": 1} for i in innovators}
    nx.set_node_attributes(g, attrs)

    # all vertices update their states in random, asynchronous order
    # (drawing a random index and removing the corresponding node from list)
    iter_lst = []
    while True:
        count = 0
        lst = []
        node_lst = list(g.nodes)
        while True:
            if not node_lst:
                break
            idx = random.randint(0, len(node_lst)-1)
            node = node_lst.pop(idx)
            if g.nodes[node]["state"] != 1:
                # An individual agent observes the current states of k other agents, which we call its neighbors
                neighbours = g.adj[node]
                k = len(neighbours)
                phi = g.nodes[node]["phi"]
                # (Counting neighbours with state = 1)
                state_count = sum([1 for neighbour in list(neighbours) if g.nodes[neighbour]["state"] == 1])
                try:
                    # Adopts state 1 if at least a threshold fraction of its neighbors are in state 1
                    if state_count/k >= phi:
                        attrs = {node: {"state": 1}}
                        nx.set_node_attributes(g, attrs)
                        count += 1
                except ZeroDivisionError as e:
                    pass
            lst.append(g.copy())
        iter_lst.append(lst)
        if count == 0:
            break

    return iter_lst


