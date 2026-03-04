# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        back = head
        front = head

        # move front pointer n steps forward
        for _ in range(n):
            front = front.next

        # edge case if we remove the first node of the list, meaning n is at the size of the list.
        if not front:
            return head.next
        
        # while we still havent reach the last node in the front pointer we move them together
        while front.next:
            back = back.next
            front = front.next

        # remove the nth node from the list
        back.next = back.next.next
        return head
