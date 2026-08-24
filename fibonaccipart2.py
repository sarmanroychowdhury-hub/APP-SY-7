n = int(input("Enter number of terms :"))
dp = [0]*n

if n>0:
    dp[0] = 0
if n > 1:
    dp[1] = 1
    
for i in range(2,n):
    dp[i]= dp[i-1] + dp[i -2] 
    
print(dp)       