
# This is my initial solution, while it works, it will never work of the list is longet than size
# of int, so there is a better solution using carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0

        mult = 1
        while l1:
            num1 += l1.val * mult
            mult *= 10
            l1 = l1.next

        mult = 1
        while l2:
            num2 += l2.val * mult
            mult *= 10
            l2 = l2.next

        res = num1 + num2
        head = ListNode(res % 10)
        res //= 10
        temp = head
        while res > 0:
            new_node = ListNode(res % 10)
            res //= 10
            temp.next = new_node
            temp = new_node
        
        return head


# this is neetcode's solution which is better, since it calculate the current value as we go.
# the main way to think about it is to look at it as simple as possible like doing math in 4th grade
# 123
#+
# 123
#_____
# this way its easy to understand how to deal with the carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry
            carry = value // 10
            res = value % 10
            new_node = ListNode(res)

            curr.next = new_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next