class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        out=''
        for i in range(l):
            out+=word1[i]+word2[i]
        out+=word1[l:]+word2[l:]
        return out
