class Node:
 def __init__(self,val):
    self.val = val
    self.next = None

#revursion function for reversing the node
def reverseList(head):
   if head is None or head.next is None:
      return head
   
   new_head = reverseList(head.next)

   head.next.next = head
   head.next = None

   return new_head

def print_linked_list(head): 
   curr = head 
   while curr:
      print(curr.val,end="->")
      curr = curr.next
   print("None")

def create_linked_list(arr):

    if not arr:
        return None
    head=Node(arr[0])
    curr=head

    for val in arr[1:]:
       curr.next = Node(val)
       curr = curr.next
    return head

#example
arr = [1,2,3,4,5]

head = create_linked_list(arr)

print("Original")
print_linked_list(head)

head = reverseList(head)
print("Reversed list")
print_linked_list(head)

