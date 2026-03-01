#This problwm uses Two Pointer Technique(fast and slow pointer)
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def print(self):
        curr=self
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print("None")

def removeNthFromEnd(head,n):
    dummy = Node(0) #creates a dummy node before the head
    dummy.next=head
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next #moves fast pointer one step forward each time

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next #deletion happens here
    
    return dummy.next

#example
n = 2

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

new_head=removeNthFromEnd(n1,n)
new_head.print()