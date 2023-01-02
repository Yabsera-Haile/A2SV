class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #initialize hashmap
        players={}
        
        
        #iterate
        for match in matches:
            winner=players.get(match[0],[0,0])
            winner=[winner[0]+1,winner[1]]
            loser=players.get(match[1],[0,0])
            loser=[loser[0],loser[1]+1]
            players[match[0]]=winner
            players[match[1]]=loser

        #add to list
        no_lose=[]
        one_lose=[]
        for key,value in players.items():
            if value[0]>0 and value[1]==0:
                no_lose.append(key)
            if value[1]==1:
                one_lose.append(key)
        
        return [sorted(no_lose),sorted(one_lose)]
        

            

            
        