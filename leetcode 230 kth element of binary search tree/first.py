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

rest = []
while True:
    
# def inorder(root,n,rest,k):
#     if root:
#         n = inorder(root.left,n,rest,k)
#         n+= 1
#         if n == k:
#             rest.append(root.val)
#             return n
#         print(root.val,n)
#         n = inorder(root.right,n,rest,k)
#     return n
# inorder(root,0,rest,3)
# print(rest)
# def order(root,value,high):
#     if root:
#         value += 1
#         high = max(high, value)
#         high = order(root.left,value,high)
#         high = order(root.right,value,high)
#     return high
#     # print(value)
# print(order(root,0,0))
# gpt code
# i had deleted and now impleming on my own
# Visual structure created:
#         3
#        / \
#       1  20
#         /  \
#        15   27

# Ab aap is 'root' variable ko use karke apna print function likh sakte hain.