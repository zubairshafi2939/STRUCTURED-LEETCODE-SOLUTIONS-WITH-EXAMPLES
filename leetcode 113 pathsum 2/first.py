# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result = [0]
        def order(root,targetSum,result,value):
            if root:
                value += str(root.val)
                if not root.left and not root.right:
                        result[0] += int(value)
                order(root.left,targetSum,result,value)
                order(root.right,targetSum,result,value)
                value = value[:len(value)-1]
        order(root,targetSum,result,"")
        return result[0]

                
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        