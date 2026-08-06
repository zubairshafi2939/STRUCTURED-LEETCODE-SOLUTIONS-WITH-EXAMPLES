class Solution(object):
    def arrayRankTransform(self, arr):
        copy = list(arr)
        copy.sort()
        data = {}
        i = 1
        for x in copy:
            if x not in data:
                data[x] = i
                i += 1
        for x in range(len(arr)):
            arr[x] = data[arr[x]]
        return arr

        """
        :type arr: List[int]
        :rtype: List[int]
        """

sol = Solution()
print(sol.arrayRankTransform([2,35,6]))
