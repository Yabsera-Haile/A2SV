class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        evens=Counter([nums[i] for i in range(n) if i%2==0])
        odds=Counter([nums[i] for i in range(n) if i%2!=0])
        result=n
        even_max=evens.most_common(1)[0]
        odd_max=odds.most_common(1)[0] if odds else (0,0)
        
        if even_max[0]!=odd_max[0]:
            result-=(even_max[1]+odd_max[1])
        else:
            even_second=evens.most_common()[1] if len(evens)>1 else (0,0)
            odd_second=odds.most_common()[1] if len(odds)>1 else (0,0)
            result-=max(even_max[1]+odd_second[1],odd_max[1]+even_second[1])
        
        return result