class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            reminder = columnNumber%26
            result.append(chr(65 + reminder))
            columnNumber = columnNumber // 26
        
        return "".join(reversed(result))