mod = 1000000007


def comb(n, k):
	dp = [0] * (k + 1)
	# nC0 is 1
	dp[0] = 1

	for i in range(1, n + 1):

		# Compute next row of pascal triangle using
		# the previous row
		for j in range(min(i, k), 0, -1):
			dp[j] = (dp[j] + dp[j - 1])%mod

	return dp[k]

def catalan(n):
	if n == 0 or n == 1:
		return 1

	catalan = [0 for i in range(n + 1)]

	catalan[0] = 1
	catalan[1] = 1

	for i in range(2, n + 1):
		catalan[i] = 0
		for j in range(i):
			catalan[i] += (catalan[j] * catalan[i-j-1])%mod

	return catalan[n]

ans = []
n = int(input())
for _ in range(n):
	k = [int(x) for x in input().split()]
	s = sum(k[1:])
	rez = catalan(s)
	for i in range(1, k[0]+1):
		rez =(rez* comb(s, k[i]))%mod
		s -= k[i]
	ans.append(rez)
for a in ans:
	print(a)

