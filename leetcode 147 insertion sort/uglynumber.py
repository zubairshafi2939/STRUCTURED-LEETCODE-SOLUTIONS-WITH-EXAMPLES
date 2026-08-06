class Solution(object):
    def isUgly(self, n):
        mainn = n
        result = []
        dataset = set()
        n = 0
        while len(result) < mainn:
            n += 1
            if n <= 0:
                return False
            rest = n
            data = [2,3,5]
            i = 0
            while i <3:
                if rest in dataset:
                    dataset.add(n)
                    result.append(n)
                    break
                if rest%data[i]==0:
                    rest = rest//data[i]
                else:
                    i+=1
                if rest == 1:
                    result.append(n)
                    dataset.add(n)
                    break
        return result
        """
        :type n: int
        :rtype: bool
        """
sol = Solution()
print(sol.isUgly(15))
        