
# this was very hard.
# basically we know the algo for reversing a list.
# so what we need is to get the node before the k group, the node after the k group
# and play with the pointers so after reversing we keep it proper in the list

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next


            prev, curr = group_next, group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
    
        return dummy.next

    def get_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node