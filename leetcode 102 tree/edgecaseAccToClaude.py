class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree structure:
#       1
#      / \
#     2   3
#    /
#   4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

def preorder(root, value, rest):
    if root:
        if value < len(rest):
            rest[value].append(root.val)
        else:
            rest.append([root.val])
        value += 1
        print(root.val, value)
        preorder(root.left, value, rest)
        preorder(root.right, value, rest)

result = []
preorder(root, 0, result)
print("Your output:   ", result)
print("Expected output:", [[1], [2, 3], [4]])