class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIPv4(s):
            address=s.split(".")
            if len(address)!=4:
                return False

            for num in address:
                if (not num.isdigit()) or (num[0]=="0" and len(num)>1):
                    return False
                if int(num)<0 or int(num)>255:
                    return False
            return True

        valid=set(['a','b','c','d','e','f','A','B','C','D','E','F'])
        def checkIPv6(s):
            address=s.split(":")
            if len(address)!=8:
                return False
            
            for num in address:
                if len(num)<1 or len(num)>4:
                    return False

                for letter in num:
                    if not letter.isdigit() and letter not in valid:
                        return False
                    if letter.isdigit() and int(letter) not in range(10):
                        return False
            return True

        if checkIPv4(queryIP):
            return "IPv4"
        if checkIPv6(queryIP):
            return "IPv6"
        return "Neither"