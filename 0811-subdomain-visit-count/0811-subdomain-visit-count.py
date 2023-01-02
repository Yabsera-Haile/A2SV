class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitors={}
        for domain in cpdomains:
            current=domain.split(" ")
            count=current[0]
            sub=current[1].split(".")
            for i in range(0,len(sub)):
                prev=visitors.get(".".join(sub[i:]),0)
                visitors[".".join(sub[i:])]=prev+int(count)
        result =[" ".join([str(value),key]) for key,value in visitors.items()]
        return result
            