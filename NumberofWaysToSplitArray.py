class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        prefixarr=[0]*n
        s=0
        c=0
        for i in range(n):
            s+=nums[i]
            prefixarr[i]=s
        for i in range(n):
            if i<n-1 and prefixarr[i]>=(total-prefixarr[i]):
                c+=1
        return c
