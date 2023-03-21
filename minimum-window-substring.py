class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        found = Counter()
        target = Counter(t)
        left, right = 0, 0

        for right in range(len(s)):
            currentChar = s[right]
			
            if currentChar in list(target.keys()):
                found[currentChar] += 1

            while (found & target) == target:
                currentWindow = right - left + 1
                if currentWindow < len(result) or result == "":
                    result = s[left:right + 1]
                found[s[left]] -= 1
                left += 1

        return result