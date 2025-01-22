# 1. Find the Longest Palindromic Substring
s = "babad"
res = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1] and len(sub) > len(res):
            res = sub
print(res)

# 2. Spiral Matrix Traversal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = []
while matrix:
    res += matrix.pop(0)
    matrix = list(zip(*matrix))[::-1]
print(res)

# 3. Detect a Cycle in a Directed Graph Using DFS
from collections import defaultdict
def has_cycle(v, visited, stack, graph):
    visited[v] = True
    stack[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor] and has_cycle(neighbor, visited, stack, graph):
            return True
        elif stack[neighbor]:
            return True
    stack[v] = False
    return False
graph = defaultdict(list)
graph[0].extend([1, 2])
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(3)
visited = [False] * 4
stack = [False] * 4
print(any(has_cycle(i, visited, stack, graph) for i in range(4)))

# 4. Minimum Number of Coins for a Given Amount
coins = [1, 2, 5]
amount = 11
dp = [float('inf')] * (amount + 1)
dp[0] = 0
for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x - coin] + 1)
print(dp[amount] if dp[amount] != float('inf') else -1)

# 5. Find All Anagrams of a String in Another String
s, p = "cbaebabacd", "abc"
from collections import Counter
p_count = Counter(p)
s_count = Counter()
res = []
for i in range(len(s)):
    s_count[s[i]] += 1
    if i >= len(p):
        if s_count[s[i - len(p)]] == 1:
            del s_count[s[i - len(p)]]
        else:
            s_count[s[i - len(p)]] -= 1
    if s_count == p_count:
        res.append(i - len(p) + 1)
print(res)
