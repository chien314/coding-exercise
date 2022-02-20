# part 1
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
  def reverse(self, head):

    prev = None
    node = head
    while node:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt
    return prev


# part 2
# reverse even sublist

def reverse_even(head):
#      [even -> even -> odd)
#       start          end
#        cur   nxt     pre
#               pre    cur
    def reverse(start, end):
        pre = end
        cur = start
        while cur != end:
          nxt = cur.next
          cur.next = pre
          pre = cur
          cur = nxt
      return pre

    # in the case of all odd
    
    fh = ListNode(None)
    fh.next = head
    pre = fh
    cur = head
    
#     odd - [even - even - odd)
#     prev  start          cur
    while cur:
        
        start = cur
        
        while cur and cur.val % 2 == 0:
            cur = cur.next
            
        if start != cur:
         pre.next = reverse(start, cur)
        
        if cur:
            pre = cur
            cur = cur.next

    return fh.next
