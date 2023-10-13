class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lps = [0] * len(b)
        prev, i = 0, 1
        while i < len(b):
            if b[prev] == b[i]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev - 1]
                    

        j=i=result=0
        while j < len(b):
            if i == len(a):
                result += 1
                i = 0

            if a[i] == b[j]:             
                j += 1
                i += 1
            else:
                if result > 1:
                    return -1
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

        return result+1