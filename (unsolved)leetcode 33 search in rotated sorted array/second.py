# nums = [4,5,6,7,0,1,2]
# l = 0
# h = len(nums)-1
# target = 2
# while(l<=h):
#     print("just")
#     mid = int((l+h)/2)
#     if nums[mid] == target:
#         print("Find at index", mid)
#         break
#     if nums[mid] >= nums[l]:
#         if target > nums[mid] or target < nums[l]:
#             l = mid+1
#         else:
#             h = mid-1

#     else:
#         # print("found in non sorted")
#         if target < nums[mid] or target > nums[h]:
#             h = mid -1
#         else:
#             l = mid + 1

# print("nothing found")