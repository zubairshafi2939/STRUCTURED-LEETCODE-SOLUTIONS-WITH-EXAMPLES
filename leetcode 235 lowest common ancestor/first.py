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
p = 20
q = 35
pdata = []
qdata = []
qhead = root
phead = root
while phead:
    pdata.append(phead.val)
    if p == phead.val:
        break
    if p > phead.val:
        phead = phead.right
    else:
        phead = phead.left
while qhead:
    qdata.append(qhead.val)
    if q == qhead.val:
        break
    if q > qhead.val:
        qhead = qhead.right
    else:
        qhead = qhead.left
print(qdata)
print(pdata)
i = 0
while i < len(pdata) and i < len(qdata):
    if pdata[i] == qdata[i]:
        lca = pdata[i]
    else:
        break
    i+=1
print(lca)

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
#         9
#        / \
#       2  20
#         /  \
#        15   35

# Ab aap is 'root' variable ko use karke apna print function likh sakte hain.