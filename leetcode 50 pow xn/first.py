class Solution(object):
    def myPow(self, x, n):
        real = n
        n = abs(n)
        binary_array = [int(bit) for bit in bin(n)[2:]]
        binary_array = binary_array[::-1]
        result = 1
        for y in binary_array:
            if y == 1:
                result *= x
            x *= x
        return result if real >=0 else 1/result



sol = Solution()
print(sol.myPow(2,16))
print(sol.myPow(2,-2))