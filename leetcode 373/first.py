nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

def print_number(n):
    if n == 0:
        return
    print_number(n-1)
    print(n)
print(print_number(2))