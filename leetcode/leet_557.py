class Solution:
    def reverseWords(self, s: str) -> str:
       words = [x[::-1] for x in s.split()]
       return " ".join(words)