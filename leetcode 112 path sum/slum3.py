class Solution(object):
    def getSum(self, nums):
        max_result = 0
        def get_pairs(arr):
            n = len(arr)
            result = []
            for i in range(n):
                for j in range(i + 1, n):
                    result.append((arr[i], arr[j]))
            return result
        freq = {}
        for x in range(len(nums)):
            if nums[x] not in freq:
                freq[nums[x]] = [x]
            else:
                freq[nums[x]].append(x)
        max_length = max(len(v) for v in freq.values())
        if max_length == 1:
            nums.sort()
            return nums[-1]
        for x,y in freq.items():
            if len(y) >= 2:
                pairs = get_pairs(y)
                for temp in pairs:
                    l = temp[0]
                    r = temp[1]
                    point = 0
                    status = True
                    while nums[l] == nums[r] and l < r:
                        point += (nums[l] + nums[r])
                        if r-l == 1:
                            # print("True")
                            max_result = max(max_result,point)
                            break
                        l += 1
                        r -= 1
                        if l == r:
                            point += nums[l]
                            max_result = max(max_result, point)
                            # print(temp[0],temp[1])
                            break

        return max_result



        # return freq


        
        """
        :type nums: List[int]
        :rtype: int
        """
sol = Solution()
print(sol.getSum([2,3,4,5]))


