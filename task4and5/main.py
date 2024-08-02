import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, color_map=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [color_map[node] for node in tree.nodes()] if color_map else [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_to_tree(heap):
    nodes = [Node(val) for val in heap]
    
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    
    return nodes[0]

# task 5 -----------------------------
def generate_color_map(nodes):
    n = len(nodes)
    cmap = plt.get_cmap("Blues")
    colors = [mcolors.rgb2hex(cmap(i / n)) for i in range(n-1, -1, -1)]
    return {node.id: colors[i] for i, node in enumerate(nodes)}

def bfs(root):
    queue = [root]
    visited = []
    while queue:
        current = queue.pop(0)
        visited.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited

def dfs(root):
    stack = [root]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return visited

# task 4 ---------------------------------
heap = [3, 1, 6, 5, 2, 4]
heapq.heapify(heap)

root = heap_to_tree(heap)
draw_tree(root)

# task 5 ---------------------------------
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в ширину
bfs_nodes = bfs(root)
bfs_color_map = generate_color_map(bfs_nodes)
draw_tree(root, bfs_color_map)

# Обхід в глибину
dfs_nodes = dfs(root)
dfs_color_map = generate_color_map(dfs_nodes)
draw_tree(root, dfs_color_map)
