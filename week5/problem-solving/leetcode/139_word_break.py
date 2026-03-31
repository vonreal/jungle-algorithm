class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True

        return dp[len(s)]

'''
- 음.. leet가 있으면 나머지 요소인 code가 사전에 있어야하는건가? 아니면 co, de

0:3

0:3 = True
3:8 = True

dp[i] = i까지 쪼갰을 때 그게 사전에 존재하는지?
ex) leetcode


i
아
word[0:1]: l
word[0~:2]: le ,(X) e
word[0~:3]: lee, (X)ee, e
word[0~:4]: leet(존재!), eet, et, t
5: leetc, eetc, etc, tc, c
6: leetco, eetco, etco, tco, co, o
7: leetcod, eetcod, etcod, tocd, ocd
8: leetcode, eetcode, etcode, tcode, code(존재!), ode, de, e


word[0:1]: l, e, e, c, o, d, e
word[0~:2]: le , ee, et, tc, co, od, de
word[0~:3]: lee, ee, e
word[0~:4]: leet(존재!), eet, et, t
5: leetc, eetc, etc, tc, c
6: leetco, eetco, etco, tco, co, o
7: leetcod, eetcod, etcod, tocd, ocd
8: leetcode, eetcode, etcode, tcode, code(존재!), ode, de, e
'''