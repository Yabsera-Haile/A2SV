class Solution:
    def maxProduct(self, words: List[str]) -> int:
        nums=[]

        for word in words:
            num=0
            for letter in word:
                num|=(1<<(ord(letter)-97))
            nums.append(num)

        pairs=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i].bit_count()+nums[j].bit_count())==(nums[i]^nums[j]).bit_count():
                    pairs.append((i,j))
        result=0
        for pair in pairs:
            word1=len(words[pair[0]])
            word2=len(words[pair[1]])
            result=max(result,(word1*word2))
        
        return result