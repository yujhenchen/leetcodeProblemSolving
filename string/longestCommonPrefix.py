class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        add = True
        stop = False
        firstStr = strs[0]
        for i in range(len(firstStr)):
            for j in range(len(strs)):
                currentStr = strs[j]
                if i > len(currentStr) - 1:
                    stop = True
                    break
                if firstStr[i] != currentStr[i]:
                    add = False
            if stop:
                break
            if add != False:
                result += firstStr[i]

        return result
