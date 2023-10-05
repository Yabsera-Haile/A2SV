class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name=list(name)
        typed=list(typed)
        last=""
        while name:
            if not typed:
                return False
            if typed[-1] == name[-1]:
                last=typed.pop()
                name.pop()
            elif typed[-1] == last:
                while typed[-1]==last:
                    typed.pop()
            else:
                return False
        
        while typed:
            if typed[-1]==last:
                typed.pop()
            else:
                return False
        return True