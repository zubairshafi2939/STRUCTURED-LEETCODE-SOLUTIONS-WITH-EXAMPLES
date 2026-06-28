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
res = 0

def order(root):
    if not root:
        return 0
    
    l = order(root.left)
    r = order(root.right)
    
    res 

# def diam(root,value,high):
#     if root:
#         value += 1
#         high = max(high,value)
#         high = diam(root.left,value,high)
#         high = diam(root.right,value,high)
#     return high
# diam(root,0,0)


# def preorder(root,value,rest):
#     if root:
#         if value < len(rest):
#             rest[value].append(root.val)
#         else:
#             rest.append([root.val])
#         value += 1
#         print(root.val, value)
#         preorder(root.left,value,rest)
#         preorder(root.right,value,rest)
# result = []
# preorder(root,0,result)
# print(result)
# Visual structure created:
#         9
#        / \
#       2  20
#         /  \
#        15   35

# Ab aap is 'root' variable ko use karke apna print function likh sakte hain.