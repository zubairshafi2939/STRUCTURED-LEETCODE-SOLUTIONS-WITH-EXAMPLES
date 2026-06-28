# Definition for a binary tree node.
# this is leetcode 98 validate binary tree. and now its done. with iterative approach and according to 
# claude this is optimal actually i come to this logic on own. as i had solved the return the kth smallest earlier
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
prev = float('-inf')
while curr or stack:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    value = curr.val
    if value < prev:
        print("fuck yes")
    prev = value
    print(curr.val)
    curr = curr.right
    