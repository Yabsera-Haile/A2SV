class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=list(count.values())
        print(freq)
        def quickSort(left,right):
            if left<right:
                pivot=partition(left,right)
                if len(freq)-pivot<k:
                    quickSort(left,pivot-1)
                elif len(freq)-pivot>k:
                    quickSort(pivot+1,right)       
        
        def partition(left,right):
            greater=left-1

            for i in range(left,right):
                if freq[i]<=freq[right]:
                    greater+=1
                    freq[i],freq[greater]=freq[greater],freq[i]

            freq[greater+1],freq[right]=freq[right],freq[greater+1]

            return greater+1
            
        quickSort(0,len(freq)-1)
        
        result=[]

        for key,value in count.items():
            if value>=freq[-k]:
                result.append(key)
        
        return result