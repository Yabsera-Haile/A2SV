class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        election={}
        max=0
        freq={}

        for i in range(len(persons)):
            freq[persons[i]]=freq.get(persons[i],0)+1
            if freq[persons[i]]>=freq.get(max,0):
                max=persons[i]
            election[i]=max
        self.election=election
        self.times=times
        
    def q(self, t: int) -> int:
        curr=bisect_right(self.times,t)
        return self.election[curr-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)