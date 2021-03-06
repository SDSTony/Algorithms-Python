N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796 #여기에서 나눠주면 저장공간 메모리 줄일 수 있다

print(dp[N])

"""
i-1(counting unit)까지 채워진 경우와
i-2(counting unit)까지 채워진 경우를 잘 살펴보자 
"""