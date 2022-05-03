# [2021-06-28] Challenge #395 [Intermediate] Phone drop
# https://www.reddit.com/r/dailyprogrammer/comments/o9k0p0/20210628_challenge_395_intermediate_phone_drop/
import sys
MAX_RECURSION = 3000
# A Dynamic Programming based Python
def phonedrop(n, h, memo={}):
	if n == 1 or h == 1:
		return h
	if memo.get(h): # could use functools functools.lru_cache like in redit post
		if memo[h].get(n):
			return memo[h][n]
	else:
		memo[h] = {}
	memo[h][n] = 0
	for i in range(1,h):
		x = phonedrop(n-1, i)
		y = phonedrop(n, h-i)
		memo[h][n] = max(memo[h][n], min(x,y)+1)
	return memo[h][n]


if __name__ == '__main__':

    # Driver program to test to printDups
	n = 4
	k = 2000
	sys.setrecursionlimit(MAX_RECURSION)
	print(phonedrop(n, k))
