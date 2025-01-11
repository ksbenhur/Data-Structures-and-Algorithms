class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        if len(s)==k:
            return True
        freq=[0]*26
        oddcount=0
        for i in s:
            freq[ord(i)-ord("a")]+=1
        for i in freq:
            if i%2!=0:
                oddcount+=1
        if oddcount<=k:
            return True
        return False

        
