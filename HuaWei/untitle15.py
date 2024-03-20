str1 = input()
str2 = input()
 

def getResult(str1, str2):
    n = len(str1)
    m = len(str2)
 
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
 
    maxV = 0
    ans = ""
 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
 
                if dp[i][j] > maxV:
                    maxV = dp[i][j]
                    ans = str1[(i - maxV):i]
            else:
                dp[i][j] = 0
 
    return ans
print(getResult(str1, str2))