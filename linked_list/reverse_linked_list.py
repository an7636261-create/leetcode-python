class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

#example

def create_linked_list(arr):
    if not arr:
        return None
    head=Node(arr[0])
    curr=head

    for val in arr[1:]:
        curr.next=Node(val)
        curr=curr.next
    return head
    
def print_linked_list(head):
    curr=head
    while curr:
        print(curr.val,end="->")
        curr=curr.next
    print("None")

arr=[1,2,3,4]

head=create_linked_list(arr)
print("Original")
print_linked_list(head)

reversed_head=reverseList(head)
print("Reversed")
print_linked_list(reversed_head)
