class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for c in columnTitle:
            value = ord(c) - ord('A') + 1
            result = result * 26 + value

        return result