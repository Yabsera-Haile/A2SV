class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        count=defaultdict(int)
        ing=defaultdict(list)
        supplies=set(supplies)
        queue=deque()

        for i in range(len(recipes)):
            for ingrediant in ingredients[i]:
                if ingrediant not in supplies:
                    ing[ingrediant].append(recipes[i])
                    count[recipes[i]]+=1
                
            if count[recipes[i]]==0:
                queue.append(recipes[i])

        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr)

            for neigh in ing[curr]:
                count[neigh]-=1
                if count[neigh]==0:
                    queue.append(neigh)
        
        return result