class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Easy Test Case
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
to_delete1 = [3, 5]

# Hard Test Case — 12 nodes
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
root2.left.left.left = TreeNode(8)
root2.left.left.right = TreeNode(9)
root2.right.left.left = TreeNode(10)
root2.right.left.right = TreeNode(11)
root2.right.right.left = TreeNode(12)
to_delete2 = [2, 6, 7]
# Easy Tree (root1):          to_delete = [3, 5]

#         1
#        / \
#       2   3
#      / \
#     4   5


# Hard Tree (root2):          to_delete = [2, 6, 7]

#            1
#           / \
#          2   3
#         / \ / \
#        4  5 6  7
#         / \  /
#        8  9 10 11
#              \
#              12
class Solution(object):
    def delNodes(self, root, to_delete):
        data = set(to_delete)
        res = []
        def order(root,res,data):
            if root:
                templ = root.left
                tempr = root.right
                if root.left and root.left.val in data:
                    if root.left.left:
                        res.append(root.left.left)
                    if root.left.right:
                        res.append(root.left.right)
                if root.right and root.right.val in data:
                    if root.right.left:
                        res.append(root.right.left)
                    if root.right.right:
                        res.append(root.right.right)
                order(templ,res,data)
                order(tempr,res,data)
        order(root,res,data)
        return res
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
sol = Solution()
# rest = sol.delNodes(root1, to_delete1)

print("break here")
rest = sol.delNodes(root2, to_delete2)
for x in rest:
    print(x.val)