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
def outer(root):
    res = 0
    def dfs(root):
        if not root:
            return 0
        
        l = dfs(root.left)
        r = dfs(root.right)

        nonlocal res
        res = max(res, l + r)

        return 1 + max(l, r)

    print(dfs(root))
outer(root)