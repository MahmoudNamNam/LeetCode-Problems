from typing import Optional
import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left, root.right = right, left
        
        return root

def draw_tree(tree, ax, title):
    """ Visualize the binary tree using matplotlib and networkx. """
    def add_edges(G, node, pos, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.val, pos=(x, y))
            if node.left:
                G.add_edge(node.val, node.left.val)
                add_edges(G, node.left, pos, x - 1 / layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.val, node.right.val)
                add_edges(G, node.right, pos, x + 1 / layer, y - 1, layer + 1)
    
    G = nx.DiGraph()
    add_edges(G, tree, pos={})  # Pass the root directly
    pos = nx.get_node_attributes(G, 'pos')
    
    nx.draw(G, pos, with_labels=True, node_size=600, node_color='lightblue', font_size=10, font_weight='bold', arrows=False, ax=ax)
    ax.set_title(title, size=15)

# Create the binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the tree


# Set up the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Visualize the original and inverted trees
draw_tree(root, axs[0], "Original Tree")
solution = Solution()
solution.invertTree(root)
draw_tree(root, axs[1], "Inverted Tree")

# Show the plot
plt.show()
