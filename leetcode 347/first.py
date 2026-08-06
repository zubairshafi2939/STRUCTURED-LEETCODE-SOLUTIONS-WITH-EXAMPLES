class Solution(object):
    def topKFrequent(self, nums, k):
        data = {}
        for x in nums:
            data[x] = data.get(x,0)+1
        bucket = ([[99999]]*len(nums))+1
        for x,y in data.items():
            bucket[y].append(x)
        rest = []
        for i in range(len(bucket)-1,-1,-1):
            if len(bucket[i]) > 1:
                for m in range(1,len(bucket[i])):
                    if len(rest) >= k:
                        return rest
                    rest.append(bucket[i][m])


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))
