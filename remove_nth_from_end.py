#!/usr/bin/env python
#encoding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		cur = ListNode(0)
		cur.next = head
		slow = fast = cur;
		while (fast.next is not None):
			print "***", fast.val
			if (n <= 0):
				slow = slow.next
			n -= 1
			fast = fast.next
		print "remove val: ", slow.next.val
		slow.next = slow.next.next
		return cur.next

class SolutionV2(object):

	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		slow = fast = head;
		while (n > 0):
			n -= 1
			fast = fast.next
		if fast is None:
			return head.next
		
		while (fast.next is not None):
			fast = fast.next
			slow = slow.next
		print "remove val: ", slow.next.val
		slow.next = slow.next.next
		return head

if __name__ == '__main__':
	ln = ListNode(1)
	ln.next = ListNode(2)
	ln.next.next = ListNode(3)
	ln.next.next.next = ListNode(4)
	ln.next.next.next.next = ListNode(5)
	s = SolutionV2()
	l = s.removeNthFromEnd(ln, 1)
	#l = ln
	while l.next is not None:
		print l.val
		l = l.next
		if l.next is None:
			print l.val
