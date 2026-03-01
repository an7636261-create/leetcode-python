class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def __str__(self):
        res = []
        curr = self
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return "->".join(res) + "-> None"

def mergeTwoLists(list1,list2):
    dummy = Node(-1)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next

        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next
    
#example
# list1 = [1,2,4]

n1=Node(1)
n2=Node(2)
n3=Node(4)

n1.next=n2
n2.next=n3

# list2 = [1,3,4]

n4=Node(1)
n5=Node(3)
n6=Node(4)

n4.next=n5
n5.next=n6

print(mergeTwoLists(n1,n4))
