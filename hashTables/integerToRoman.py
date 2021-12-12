class Solution:
    def intToRoman(self, num: int) -> str:
        # A map to keep all the value as key, and symbol as value
        # Sort the map by key descending
        # Find the maximun divided result which is no 0, repeat the symbol by divided result
        # Subtract the number by divided result, until reach the min key of the map

        valSymbolMap = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        valSymbolLs = sorted(valSymbolMap, reverse=True)
        result = ""

        for i in range(len(valSymbolLs)):
            currentKey = valSymbolLs[i]
            dividedResult = num // currentKey
            # print(dividedResult)
            if dividedResult is not 0:
                result += dividedResult * valSymbolMap[currentKey]
                num = num % currentKey
                # print(num)
            # print()
        return result
