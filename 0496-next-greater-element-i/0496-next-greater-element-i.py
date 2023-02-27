class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ref={}
        
        for num in nums2:
            while stack and stack[-1]<num:
                ref[stack.pop()]=num
            stack.append(num)
        result=[]    
        for num in nums1:
            if num in ref:
                result.append(ref[num])
            else:
                result.append(-1)
        return result
                
        
        
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # result=[-1]*len(nums1)
        # dict={}
        # m_stack=[]
        # for i in range(len(nums1)):
        #     dict[nums1[i]]=i
        # for num2 in nums2:
        #     if num2 in dict:
        #         while m_stack and  m_stack[-1]<num2:
        #             new = m_stack.pop()
        #             result[dict[new]] = num2
        #         m_stack.append(num2)
        #     else:
        #         while m_stack and  m_stack[-1]<num2:
        #             new = m_stack.pop()
        #             result[dict[new]] = num2
        # return result

        
