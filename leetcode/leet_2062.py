class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for l in range(n):
            vowels_sub = {k: 0 for k in vowels}
            for r in range(l, n):
                if s[r] in vowels:
                    vowels_sub[s[r]] += 1
                    for val in vowels_sub.values():
                        if val == 0:
                            break
                    else:
                        cnt += 1
                else:
                    vowels_sub = {k: 0 for k in vowels}
                    break
            else:
                continue
            if vowels_sub.get(s[l], 0) > 0:
                vowels_sub[s[l]] -= 1
        return cnt