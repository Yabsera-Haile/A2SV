# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:       
        current=head
        points=[]
        start = None
        count=0
        counter=head
        while counter:
            if count==k-1:
                prev=counter
            counter=counter.next
            count+=1
                    
        for j in range(count//k):
            tail=current
            i=1
            while i <= k:
                temp = current.next
                current.next = start
                start = current
                current = temp
                i +=1
            print(start,tail)
            points.append([start,tail])
            start=None
        
        for i in range(len(points)-1):
            points[i][1].next=points[i+1][0]
            
        points[len(points)-1][1].next=current
        return points[0][0]
                
                
                
                
                
#             if j==0:
#                 prev_head=start
#             else:
#                 prev_tail.next=start
#                 prev_tail=tail
#             start=None 
        
#         temp=prev_head
#         while temp.next:
#             temp=temp.next
#         print(prev_head) 
#         temp.next=prev_tail
#         return prev_head
        