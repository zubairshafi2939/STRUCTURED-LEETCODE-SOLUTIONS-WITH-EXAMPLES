class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#[1,2,3,4,5], n = 2 ,[1,2,3,5]
head = ListNode(16) #0
temp = head
temp.next = ListNode(12)
temp = temp.next
temp.next = ListNode(22)
temp = temp.next
temp.next = ListNode(2)
temp = temp.next
temp.next = ListNode(2)#4
temp = temp.next
temp.next = ListNode(54)#4
temp = temp.next
temp.next = ListNode(1)#4
print("dh")
fake = ListNode(-5001)
fake.next = head
head = fake
temp = head
prev = temp

while temp:
    if prev.val > temp.val:
        print("If condition True")
        prev.next = prev.next.next
        start = head
        find = start
        while start.val < temp.val:
            find = start
            start = start.next
        findnext = find.next
        find.next = temp
        temp.next = findnext
        temp = prev.next
    else:
        print("else condition true")
        prev = temp
        temp = temp.next
while head:
    print(head.val)
    head = head.next

    

    
    






























# while temp:
#     start = head
#     if prev.val > temp.val:
#         faketemp = temp
#         find = start
#         while start.val < faketemp.val:
#             find = start
#             start = start.next
#         tempo = find.next
#         find.next = faketemp
#         temp = faketemp.next
#         faketemp.next = start
#     else:
#         temp = temp.next
# while head:
#     head = head.next
