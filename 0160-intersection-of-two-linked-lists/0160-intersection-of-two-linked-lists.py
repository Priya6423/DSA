# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1=0
        len2=0
        temp1=headA
        temp2=headB
        while temp1:
            temp1=temp1.next
            len1=len1+1
        while temp2:
            temp2=temp2.next
            len2=len2+1
        a=headA
        b=headB
        if len1>len2:
            diff=len1-len2
            while diff:
                a=a.next
                diff=diff-1
        else:
            diff=len2-len1
            while diff:
                b=b.next
                diff=diff-1
        while a and b:
            if a==b:
                return a
            a=a.next
            b=b.next
        return a

                
        
        