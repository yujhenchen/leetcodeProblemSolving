class Solution:
    def addBinary(self, a: str, b: str) -> str:
        addDigit = 0
        addedS = str(int(a) + int(b))
        # print(addedS)
        result = [None] * len(addedS)

        for i in range(len(addedS) - 1, -1, -1):
            # print(addedS[i])
            value = int(addedS[i]) + addDigit
            result[i] = str(value % 2)
            if value >= 2:
                addDigit = 1
            else:
                addDigit = 0
        if addDigit == 1:
            return str(addDigit) + "".join(result)
        else:
            return "".join(result)
