class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        closers={"}":"{",
                 ")":"(",
                 "]":"[",}
        for letter in s:
            if letter in closers:
                if result and result[-1]==closers[letter]:
                    result.pop()
                else:
                    return False
            else:
                result.append(letter)
        return True if not result else False
        
        