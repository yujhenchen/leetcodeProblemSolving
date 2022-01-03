class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        signed = ""
        if "-" == strX[0]:
            signed = strX[0]
            strX = strX.replace("-", "")
        
        strResult = ""
        result = 0
        for i in range(len(strX)-1, -1, -1):
            if strX[i] != 0:
                strResult += strX[i]
        result = int( signed + strResult)
        
        if result < -pow(2, 31) or result > pow(2, 31):
            return 0
        return result