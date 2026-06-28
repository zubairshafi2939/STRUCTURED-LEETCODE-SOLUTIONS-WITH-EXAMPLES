# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually creating the tree nodes
root = TreeNode(9)
root.left = TreeNode(2)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(35)

def order(root,rest):
    if root:
        rest = rest + str(root.val) + ","
        rest = order(root.left,rest)
        rest = order(root.right,rest)
    else:
        rest = rest + "#"
    return rest
rest = ""

rest = order(root,rest)
print(rest)
# Visual structure created:
#         9
#        / \
#       2  20
#         /  \
#        15   35

# Ab aap is 'root' variable ko use karke apna print function likh sakte hain.