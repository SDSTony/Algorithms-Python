N, M = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

"""
단위가 동적으로 들어온다 
"""

dp = [10001] * 10001

# init
for coin in coins:
    dp[coin] = 1

for coin in coins:
    for i in range(coin + 1, M + 1): 
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[M] != 10001:
    print(dp[M])

else:
    print(-1)
