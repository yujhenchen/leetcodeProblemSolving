class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # remove all spaces from right
        # get the first space index from right
        # count length from the index to the end

        result = s.rstrip()

        if " " not in result:
            return len(result)

        lastSpaceIndex = result.rindex(" ")
        # print(lastSpaceIndex)
        # print("test="+result[lastSpaceIndex+1:]+"=test")
        return len(result[lastSpaceIndex + 1 :])
