class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def hasCycle(head):
    if not head:
        return False
        
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow == fast:
            return True
    return False

#example
head = [3,2,0,-4]

n1=ListNode(3)
n2=ListNode(2)
n3=ListNode(0)
n4=ListNode(-4)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2

print(hasCycle(n1))