class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dp=[0]*(len(num1)+len(num2))
        res=0
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                tmp=dp[i+j+1]+int(num1[i])*int(num2[j])
                dp[i+j+1]=(tmp)%10
                dp[i+j]=dp[i+j]+(tmp)//10
        for v in dp:
            res*=10
            res+=v
        return str(res)
a=Solution()

print(a.multiply(num1 = "123", num2 = "456"))
