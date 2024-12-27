class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        maxLeftScore=[0]*n
        maxLeftScore[0]=values[0]
        maxScore=0
        for i in range(1,n):
            currRightScore=values[i]-i
            maxScore=max(maxScore,maxLeftScore[i-1]+currRightScore)
            currLeftScore=values[i]+i
            maxLeftScore[i]=max(maxLeftScore[i-1],currLeftScore)
        return maxScore    
