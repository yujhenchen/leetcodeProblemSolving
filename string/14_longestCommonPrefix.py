from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        # My attempt
        # add = True
        # stop = False
        # firstStr = strs[0]
        # for i in range(len(firstStr)):
        #     for j in range(len(strs)):
        #         currentStr = strs[j]
        #         if i > len(currentStr) - 1:
        #             stop = True
        #             break
        #         if firstStr[i] != currentStr[i]:
        #             add = False
        #     if stop:
        #         break
        #     if add != False:
        #         result += firstStr[i]

        # Cool solution use zip, tuple, and set
        firstStr = strs[0]
        for charTuple in zip(*strs):
            if len(set(charTuple)) == 1:
                result += charTuple[0]
            else:
                break

        return result
