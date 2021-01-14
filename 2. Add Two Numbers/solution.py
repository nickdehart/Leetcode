# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = str(int(self.combine(l1)) + int(self.combine(l2)))
        return self.separate(ans, len(ans) - 1)

    def combine(self, lst):
        if lst.next:
            return self.combine(lst.next) + str(lst.val)
        else:
            return str(lst.val)
        
    def separate(self, string, i):
        if i < 1:
            return ListNode(int(string[0]), None)
        else:
            return ListNode(int(string[i]), self.separate(string, i-1))
        


        