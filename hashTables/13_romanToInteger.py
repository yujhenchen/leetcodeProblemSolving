class Solution:
    def romanToInt(self, s: str) -> int:
        # A map to keep the symbol and the corresponding value
        # A map to keep the symbol and the six instances value
        # A window to look at 2 chars if contain six instances value

        symbolValueMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sixSymbolValueMap = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        if len(s) == 1:
            return symbolValueMap[s]

        result = 0
        preIndex = 0

        while preIndex < len(s):
            currentIndex = preIndex + 1
            if currentIndex < len(s):
                combinedSymbol = s[preIndex] + s[currentIndex]
                # print(combinedSymbol)
                if combinedSymbol in sixSymbolValueMap:
                    result += sixSymbolValueMap[combinedSymbol]
                    preIndex += 2
                    currentIndex += 2
                else:
                    result += symbolValueMap[s[preIndex]]
                    preIndex += 1
                    currentIndex += 1
            else:
                result += symbolValueMap[s[preIndex]]
                preIndex += 1
                currentIndex += 1
        return result
