class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)

        @cache
        def checkInter(index1,index2,index3):
            if index1==n1 and index2==n2 and index3==n3:
                return True

            return index3<n3 and (index1<n1 and s1[index1]==s3[index3] and checkInter(index1+1,index2,index3+1) or index2<n2 and s2[index2]==s3[index3] and checkInter(index1,index2+1,index3+1))

        return checkInter(0,0,0)
        