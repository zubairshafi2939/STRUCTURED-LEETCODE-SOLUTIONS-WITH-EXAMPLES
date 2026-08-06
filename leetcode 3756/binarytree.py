from collections import deque
class Solution(object):
    def minDepth(self, root):
        data = deque([root])
        result = []
        point = 1
        rest = 1
        while data:
            level = []
            if len(data) != point:
                return rest
            for i in range(len(data)):
                node = data.popleft()
                level.append(node.val)
                if node.left: data.append(node.left)
                if node.right: data.append(node.right)
            result.append(float(sum(level))/len(level))
            point *= 2
            rest += 1
        return rest