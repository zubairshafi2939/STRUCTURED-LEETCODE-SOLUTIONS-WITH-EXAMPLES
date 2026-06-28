# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually creating the tree nodes
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
preorder(root)
porder = [3,9,20,15,7]
# gpt code
# i had deleted and now impleming on my own
# Visual structure created:
#         3
#        / \
#       9  20
#         /  \
#        15   7

# Ab aap is 'root' variable ko use karke apna print function likh sakte hain.