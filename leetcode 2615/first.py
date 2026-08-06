class Solution(object):
    def distance(self, nums):
        data = {}
        prefix = {}
        result = []
        for x in range(len(nums)):
            if nums[x] not in data:
                data[nums[x]] = [x]
                prefix[nums[x]] = [x]
            else:
                data[nums[x]].append(data[nums[x]][-1]+x)
                prefix[nums[x]].append(x)
        ptr = {}
        for x in range(len(nums)):
            if nums[x] not in ptr:
                ptr[nums[x]] = 0
            else:
                ptr[nums[x]] += 1
            pointer = ptr[nums[x]]
            mainDigit = data[nums[x]][pointer]
            firstHalf = (mainDigit*(pointer+1))-data[nums[x]][pointer]
            print("remaing from", pointer+1, " for ", nums[x] ," is ", len(data[nums[x]])-(pointer+1))
            secondHalf = (data[nums[x]][-1]-data[nums[x]][pointer])-(mainDigit*(len(data[nums[x]])-(pointer+1)))
            result.append(firstHalf+secondHalf)
        return result
    
        """
        :type nums: List[int]
        :rtype: List[int]
        """

sol = Solution()
print(sol.distance([1,3,1,1,2]))