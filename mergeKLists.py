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
 
  
class Solution(object):
    def mergeKLists(self, lists):
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
