class Solution(object):
    def dailyTemperatures(self, temperatures):
        temp = temperatures
        stk = [(temp[0],0)]
        temp[0] = 0
        for x in range(1,len(temp)):
            if temp[x] > stk[-1][0]:
                while stk and stk[-1][0] < temp[x]:
                    index = stk[-1][1]
                    temp[index] = x - index
                    stk.pop()
            stk.append((temp[x],x))
            temp[x] = 0
        return temp
                
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures))
