class Solution:
    def isValid(self, s: str) -> bool:
        # return False if has odd number of characters
        # return False if brackets do not match

        if len(s) % 2 != 0:
            return False

        brackets = []
        bracketMap = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] in bracketMap:
                targetOpen = bracketMap[s[i]]
                if len(brackets) == 0:
                    return False
                else:
                    if brackets[len(brackets) - 1] != targetOpen:
                        return False
                    else:
                        brackets.pop()
            else:
                brackets.append(s[i])
        # print(brackets)
        if len(brackets) > 0:
            return False

        return True
