class Solution(object):
    def topKFrequent(self, nums, k):
        data = {}
        for x in nums:
            data[x] = data.get(x,0)+1
        bucket = [[] for _ in range(len(nums)+1)]
        # print(data)
        for x,y in data.items():
            bucket[y].append(x)
        rest = []
        print(bucket)
        for i in range(len(bucket)-1,-1,-1):
            print("working")
            if bucket[i]:
                print("Workingtoo")
                for number in bucket[i]:
                    if len(rest)>=k:
                        return rest
                    rest.append(number)
        # return data

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

sol = Solution()
# print(sol.topKFrequent([1,1,1,2,2,3],2))
print(sol.topKFrequent([1],1))
       