# Better Approach — O(n) only
# Key insight: k rotations = sirf last k nodes ko front pe lagao
def rotateRight(self, head, k):
    if not head or not head.next:
        return head

    # Step 1: Length nikalo + tail find karo
    tail = head
    n = 1
    while tail.next:
        tail = tail.next
        n += 1

    # Step 2: Actual rotations
    k = k % n
    if k == 0:
        return head  # No rotation needed

    # Step 3: New tail find karo (n-k-1 steps)
    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next

    # Step 4: Pointers update karo
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head