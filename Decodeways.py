#91. Decode Ways
#A message containing letters from A-Z can be encoded into numbers using the following mapping:
#Input: s = "226"
#Output: 3
#Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Decodeways():
    def decodeway(self,s):
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if(s[i]=='0'):
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            if(i+1<len(s) and (s[i]=='1' or s[i]=='2' and (s[i+1] in '0123456'))):
                dp[i]=dp[i]+dp[i+2]
        return(dp[0])

d=Decodeways()
print(d.decodeway("06"))
