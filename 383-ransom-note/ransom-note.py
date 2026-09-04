class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}

        for i in magazine:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        for j in ransomNote:
            if j in a:
                if a[j] > 0:
                    a[j] -= 1
                else:
                    return False
            else:
                return False

        return True