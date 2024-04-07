class Solution:
    def checkValidString(self, s: str) -> bool:
        _min=0
        _max=0

        for char in s:
            if char=="(":
                _min,_max=_min+1,_max+1
            elif char == ")":
                _min,_max=_min-1,_max-1
            else:
                _min,_max=_min-1,_max+1
            if _max<0:
                return False
            _min=max(0,_min)
        
        return _min==0

        