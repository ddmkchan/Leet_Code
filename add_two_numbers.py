#!/usr/bin/env python
#encoding : utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        pass


if __name__ == '__main__':
    ln = ListNode(2)
    ln.next = ListNode(4)
    ln.next.next = ListNode(3)
    ln2 = ListNode(5)
    ln2.next = ListNode(6)
    ln2.next.next = ListNode(4)
