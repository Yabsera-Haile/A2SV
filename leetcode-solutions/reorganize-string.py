class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        counts = Counter(s)
        freq, letter = 0, ''
        for char, count in counts.items():
            if count > freq:
                freq = count
                letter = char

        if freq > (n + 1) // 2:
            return ""
        result = [''] * n
        index = 0

        while counts[letter] != 0:
            result[index] = letter
            index += 2
            counts[letter] -= 1

    
        for char, count in counts.items():
            while count > 0:
                if index >= n:
                    index = 1
                result[index] = char
                index += 2
                count -= 1

        return ''.join(result)