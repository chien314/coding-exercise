from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):

        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))

        while not q.empty():
#             cnt+=1
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node)) ## note: put tuple in 
        return head.next
