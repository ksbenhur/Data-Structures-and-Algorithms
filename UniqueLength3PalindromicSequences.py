class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters=set(s)
        
        ans=0
        for letter in letters:
            between=set()
            i,j=s.index(letter),s.rindex(letter)
            for k in range(i+1,j):
                between.add(s[k])
            ans+=len(between)
        return ans
