# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Manually creating the tree nodes
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(27)

stack = []
curr = root
k = 2
trigger = False
while curr or stack:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    k -= 1
    if k == 0:
        print("don and found here", curr.val)
        trigger = True
        break
    if trigger:
        break
    curr = curr.right
    