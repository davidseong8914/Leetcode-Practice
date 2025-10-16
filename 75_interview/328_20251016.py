# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenHead = None
        oddHead = None
        evenTail = None
        oddTail = None
        even = True

        while head:
            # even
            if even == True:
                if evenHead == None:
                    evenHead = head
                    evenTail = head
                else: 
                    evenTail.next = head
                    evenTail = evenTail.next

            # when it's odd
            else:
                if oddHead == None:
                    oddHead = head
                    oddTail = head
                else:
                    oddTail.next = head
                    oddTail = oddTail.next

            even = not even
            head = head.next
        
        if oddTail:
            oddTail.next = None
        if evenTail:
            evenTail.next = oddHead

        return evenHead