class Solution(object):
    def nextGreaterElement(self, n):
        realn = n
        result = []
        while n > 9:
            temp = n%10
            result.append(temp)
            n = n//10
        result.append(n)
        max_val = -1
        for x in range(len(result)):
            done = False
            if result[x] < max_val:
                for y in range(x):
                    if result[y] > result[x]:
                        # print("True as fuck", result[y], result[x],y,x)
                        print(result[y],result[x])
                        temp = result[y]
                        result[y] = result[x]
                        result[x] = temp
                        print(result[y],result[x])
                        sortable = result[:x]
                        print(sortable)
                        sortable.sort()
                        result = sortable[::-1]+result[x:] 
                        done = True
                        break
            else:
                max_val = max(max_val,result[x])
            if done:
                break
        print(result)
        first = 0
        for x in result[::-1]:
            first *= 10
            first += x
        Int_max = 2**31-1
        return first if first != realn else -1

        """
        :type n: int
        :rtype: int
        """
sol = Solution()
print(sol.nextGreaterElement(230241))