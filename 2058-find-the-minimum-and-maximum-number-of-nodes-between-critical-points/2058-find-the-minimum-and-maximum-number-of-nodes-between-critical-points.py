# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        temp=head.next
        index=1
        first=-1
        prev_critical=-1
        mini=float('inf')
        while temp.next:
            fwd=temp.next
            if (temp.val<prev.val and temp.val<fwd.val) or (temp.val>prev.val and temp.val>fwd.val):
                if first==-1:
                    first=index
                else:
                    mini=min(mini,index-prev_critical)
                prev_critical=index
                
            prev=temp
            temp=temp.next
            index+=1
        if first==-1 or first==prev_critical:
            return [-1,-1]

        last=prev_critical-first
        return [mini,last]

            
