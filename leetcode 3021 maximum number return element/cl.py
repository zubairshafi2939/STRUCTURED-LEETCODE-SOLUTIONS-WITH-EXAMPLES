class Solution(object):
    def maximumLength(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        result = 1
        for x in range(1,len(nums)):
            if nums[x-1] == nums[x]:
                score = 2
                i = x+1
                ptr = nums[x]*nums[x]
                data = set()
                while i < len(nums):
                    print(f"i={i}, nums[i]={nums[i]}, ptr={ptr}, score={score}")  # debug
                    if ptr == nums[i]:
                        if nums[i] == nums[i-1] and nums[i] not in data:
                            score += 2
                            data.add(nums[i])
                        result = max((score+1), result)
                        print(f"match! score={score}, result={result}")  # debug
                    if ptr < nums[i]:
                        ptr *= ptr
                    i += 1
        return result
sol = Solution()
print(sol.maximumLength([2,2,4,4,16,16,256]))