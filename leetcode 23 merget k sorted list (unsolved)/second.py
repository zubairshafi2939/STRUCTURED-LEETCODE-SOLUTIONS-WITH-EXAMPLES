class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# List 1: [1, 4, 5]
head1 = ListNode(1)
temp = head1
temp.next = ListNode(4)
temp = temp.next
temp.next = ListNode(5)

# List 2: [1, 3, 4]
head2 = ListNode(1)
temp = head2
temp.next = ListNode(3)
temp = temp.next
temp.next = ListNode(4)

# List 3: [2, 6]
head3 = ListNode(2)
temp = head3
temp.next = ListNode(6)

lists = [head1, head2, head3]
rest = ListNode(-1)

for x in lists:
    print(x.val)