#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        # code here
        graph=defaultdict(set)
        count=defaultdict(int)
        
        for i in range(1,len(alien_dict)):
            prev=alien_dict[i-1]
            curr=alien_dict[i]
     
            for j in range(min(len(prev),len(curr))):
                if prev[j]!=curr[j] :
                    if curr[j] not in graph[prev[j]]:
                        graph[prev[j]].add(curr[j])
                        count[curr[j]]+=1
                    break
        
        queue=deque()
        for i in range(K):
            letter=chr(97+i)
            if count[letter]==0:
                queue.append(letter)
         
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr)
            
            for neigh in graph[curr]:
                count[neigh]-=1
                if count[neigh]==0:
                    queue.append(neigh)
                    
        return result
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends