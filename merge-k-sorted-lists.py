# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        heapq.heapify(heap)

        for i,_list in enumerate(lists):
            if _list:
                heapq.heappush(heap,(_list.val,i))
        
        result=dummy=ListNode()

        while heap:
            curr=heapq.heappop(heap)
            dummy.next=ListNode(curr[0])
            dummy=dummy.next
            lists[curr[1]]=lists[curr[1]].next
            if lists[curr[1]]:
                heapq.heappush(heap,(lists[curr[1]].val,curr[1]))
            
        
        return result.next