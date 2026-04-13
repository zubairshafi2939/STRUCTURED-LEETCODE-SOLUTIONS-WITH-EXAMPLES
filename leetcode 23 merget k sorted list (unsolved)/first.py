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
for link in lists:
    templist = ListNode(-1)
    thead = templist
    s = thead
    while rest or link:
        while rest and link:
            if rest.val < link.val:
                templist.next = rest
                rest = rest.next
                templist = templist.next
            else:
                templist.next = link
                link = link.next
                templist = templist.next
        while rest:
            templist.next = rest
            rest = rest.next
            templist = templist.next
        while link:
            templist.next = link
            link = link.next
            templist = templist.next
    rest = thead.next
    s = rest
    print("-----")
    while s:
        print(s.val)
        s = s.next
    