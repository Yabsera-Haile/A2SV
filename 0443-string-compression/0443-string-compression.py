class Solution:
    def compress(self, chars: List[str]) -> int:
        prev=chars[0]
        counter = 0
        chars.append("")
        i=0
        for char in chars:
            if prev==char:
                counter+=1
            else:
                if counter==1:
                    chars[i]=prev
                    i+=1
                else:
                    chars[i]=prev
                    i+=1
                    for count in str(counter):
                        chars[i]=count
                        i+=1
                prev=char
                counter=1
        return i