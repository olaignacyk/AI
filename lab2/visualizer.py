import networkx as nx
import matplotlib.pyplot as plt

def visualize_plan_only(initial_state, plan, filename="plan_tree.png"):
    G = nx.DiGraph()
    states = []
    
    current_state = frozenset(initial_state)
    states.append((0, current_state, "START"))

    for i, action in enumerate(plan):
        next_state = frozenset(action.apply(current_state))
        states.append((i + 1, next_state, str(action)))
        current_state = next_state

    for i in range(len(states) - 1):
        id1, _, label1 = states[i]
        id2, _, label2 = states[i + 1]
        G.add_node(id1, label=label1)
        G.add_node(id2, label=label2)
        G.add_edge(id1, id2)

    pos = hierarchy_pos(G, 0)
    labels = nx.get_node_attributes(G, 'label')
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000,
            node_color="lightgreen", font_size=9, font_weight='bold', arrows=True)
    plt.title("Plan – Ścieżka do celu")
    plt.savefig(filename)
    plt.close()
    print(f"📄 Plan zapisany do pliku: {filename}")

def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}
    def _hierarchy_pos(G, root, left, right, vert_loc, xcenter, pos):
        children = list(G.successors(root))
        if len(children) == 0:
            pos[root] = (xcenter, vert_loc)
        else:
            dx = (right - left) / len(children)
            nextx = left + dx / 2
            for child in children:
                pos = _hierarchy_pos(G, child, nextx - dx/2, nextx + dx/2,
                                     vert_loc - vert_gap, nextx, pos)
                nextx += dx
            pos[root] = (xcenter, vert_loc)
        return pos

    return _hierarchy_pos(G, root, 0, width, vert_loc, xcenter, pos)
