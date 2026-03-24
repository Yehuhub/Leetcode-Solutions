
# this is my solution, it runs in O(n * k), basically we merge two lists at a time
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            dummy= ListNode()
            temp = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            
            if l1:
                temp.next = l1
            else:
                temp.next = l2
            return dummy.next 

        res = None
        for i in range(len(lists)):
            res = merge(res, lists[i])
        return res



# This is another solution, more efficient in O(nlogk) we maintain a min heap and always insert the next
# node to the heap, it is in nlogk since there are never more than k elements in the heap.
# we maintain a wrapper since we can't maintain a heap of nodes since heap doesnt know how to compare it
# so we use a wrapper that can compare

# this class is necessary so we can store a node in the heap
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        res = ListNode()
        temp = res

        for lst in lists:
            if lst:
                heapq.heappush(heap, NodeWrapper(lst))

        while heap:
            node_wrapper = heapq.heappop(heap)
            temp.next = node_wrapper.node
            temp =  temp.next

            if node_wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(node_wrapper.node.next))


        return res.next
