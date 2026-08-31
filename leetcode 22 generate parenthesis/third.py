class Solution(object):
    def isDigitorialPermutation(self, n):
        real = n
        data = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
        total = 0
        rest = []
        while n >= 1:
            temp = n%10
            rest.append(temp)
            n = n//10
            total += data[temp]
        check = []
        while total >= 1:
            temp = total%10
            check.append(temp)
            total = total //10
        rest.sort()
        check.sort()
        return rest == check
            
            
        """
        :type n: int
        :rtype: bool
        """

sol = Solution()
print(sol.isDigitorialPermutation(415))