import networkx as nx
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from scripts.helpers import col_nodes_current
from scripts.model import simple_model


def animate_g(lst, fps):
    lst = [item for sublist in lst for item in sublist]
    pos = nx.nx_agraph.graphviz_layout(lst[0], prog="dot")
    fig, ax = plt.subplots(figsize=(6,4))
    plt.axis('off')

    def init():
        nx.draw(lst[0], pos= pos, node_color=col_nodes_current(lst[0]))

    def update(i):
        ax.clear()
        nx.draw(lst[i], pos=pos, node_color=col_nodes_current(lst[i]))

    ani = animation.FuncAnimation(fig, update, init_func=init, interval=1000, frames=len(lst))
    ani.save('animations/animation.gif', writer='imagemagick', savefig_kwargs={'facecolor':'white'}, fps=fps)


# lst = simple_model(n=10, z=4, phi=0.3, upper_phi=1)
# pos = nx.nx_agraph.graphviz_layout(lst[0][0], prog="dot")
# nx.draw(lst[0][0], pos=pos, node_color=col_nodes_current(lst[0][0]))

