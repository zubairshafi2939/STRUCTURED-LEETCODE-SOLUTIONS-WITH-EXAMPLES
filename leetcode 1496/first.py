class Solution(object):
    def isPathCrossing(self, path):
        datax = {'N':1,'S':-1}
        datay = {'E':1,'W':-1}
        x = set()
        realx = 0
        realy = 0
        for i in path:
            x.add((realx,realy))
            if i in datax:
                realx += datax[i]
            else:
                realy += datay[i]
            if (realx,realy) in x:
                return True
        return False

        """
        :type path: str
        :rtype: bool
        """
        
sol = Solution()
print(sol.isPathCrossing("NESW"))
