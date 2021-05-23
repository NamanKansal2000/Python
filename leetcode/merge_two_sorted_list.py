# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1==None and l2 == None:
            return None
        if l1 == None and l2!= None:
            return l2
        if l1 != None and l2 == None:
            return l1
        else:
            temp = ListNode(0)
            p = temp
            while l1 != None and l2!=None:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1!=None:
                p.next = l1
            if l2!=None:
                p.next = l2
            return temp.next
