class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        player=trainer=0
        
        while player < len(players) and trainer < len(trainers):
            if players[player] <= trainers[trainer]:
                player+=1
                trainer+=1
            else:
                trainer+=1
        return player
                