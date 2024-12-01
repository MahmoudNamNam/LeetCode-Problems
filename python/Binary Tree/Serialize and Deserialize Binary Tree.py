from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "" 
        queue= deque([root])
        result= []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('#')
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data =='':
            return None
        nodes =data.split(',')
        root = TreeNode(int(nodes[0]))
        queue =deque([root])
        idx=1
        while queue:
            parent=queue.popleft()
            if nodes[idx] != "#":
                parent.left =TreeNode(int(nodes[idx]))
                queue.append(parent.left)
            idx+=1
            if nodes[idx] != "#":
                parent.right =TreeNode(int(nodes[idx]))
                queue.append(parent.right)
            idx+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
"""
       1
      / \
     2   3
        / \
       4   5

"""

# Instantiate Codec and test
ser = Codec()
deser = Codec()

serialized_data = ser.serialize(root)
print("Serialized:", serialized_data)  # Output: "1,2,3,#,#,4,5"

deserialized_tree = deser.deserialize(serialized_data)
print("Root value after deserialization:", deserialized_tree.val)  # Output: 1
