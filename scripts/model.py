import networkx as nx
import matplotlib
import random
import numpy as np
import matplotlib.pyplot as plt


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

    initial = g.copy()

    node_lst = list(g.nodes)
    # all vertices update their states in random, asynchronous order
    # (drawing a random index and removing the corresponding node from list)
    change = True
    while change:
        while True:
            if not node_lst:
                break
            change = False
            idx = random.randint(0, len(node_lst)-1)
            node = node_lst.pop(idx)
            if g.nodes[node]["state"] != 1:
                # An individual agent observes the current states of k other agents, which we call its neighbors
                neighbours = g.adj[node]
                k = len(neighbours)
                phi = g.nodes[node]["phi"]
                # (Counting neighbours with state = 1)
                count = sum([1 for neighbour in list(neighbours) if g.nodes[neighbour]["state"] == 1])
                try:
                    # Adopts state 1 if at least a threshold fraction of its neighbors are in state 1
                    if count/k >= phi:
                        attrs = {node: {"state": 1}}
                        nx.set_node_attributes(g, attrs)
                        change = True
                except ZeroDivisionError as e:
                    pass

    return initial, g


initial, end = simple_model(100,4, 0.3, upper_phi=2)
