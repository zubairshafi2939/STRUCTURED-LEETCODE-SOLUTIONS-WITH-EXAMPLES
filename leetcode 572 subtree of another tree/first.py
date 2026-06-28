def same(p,q):
    pstack = [p]
    qstack = [q]
    while pstack and qstack:
        pnode = pstack.pop()
        qnode = qstack.pop()
        if pnode.val != qnode.val:
            return False
        if pnode.right or qnode.right:
            if pnode.right and qnode.right:
                pstack.append(pnode.right)
                qstack.append(qnode.right)
            else:
                return False
        if pnode.left or qnode.left:
            if pnode.left and qnode.left:
                pstack.append(pnode.left)
                qstack.append(qnode.left)
            else:
                return False
    return True
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
q1 = TreeNode(20)
q1.left = TreeNode(15)
q1.right = TreeNode(35)
stack = [root]
result = []

while stack:
    node = stack.pop()        # root process karo
    if q1.val == node.val:
        q = q1
        p = node
        if same(p,q):
            print("True")
    
    if node.right:            # pehle right push karo
        stack.append(node.right)
    if node.left:             # phir left push karo (taake pehle niklega)
        stack.append(node.left)

print(result)


# Visual structure created:
#         9
#        / \
#       2  20
#         /  \
#        15   35

# Ab aap is 'root' variable ko use karke apna print function likh sakte hain.