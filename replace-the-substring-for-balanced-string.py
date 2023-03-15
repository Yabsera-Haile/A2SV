from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        result = n = len(s)
        i = 0
        for index, letter in enumerate(s):
            count[letter] -= 1
            while i < n and all(n / 4 >= count[letter] for letter in 'QWER'):
                result = min(result, index - i + 1)
                count[s[i]] += 1
                i += 1
        return result