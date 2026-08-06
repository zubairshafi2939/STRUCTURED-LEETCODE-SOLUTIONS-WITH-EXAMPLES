# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def order(root,value,target,result):
            if len(result) == 1:
                return
            if root:
                value += root.val
                if not root.left and not root.right:
                    if value == target:
                        result.append(True)
                        return
                order(root.left,value,target,result)
                order(root.right,value,target,result)
        result = []
        order(root,0,targetSum,result)
        return True if result else False
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        