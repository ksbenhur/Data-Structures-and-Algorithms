class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels=["a","e","i","o","u"]
        res=[0]*len(queries)
        prefixarr=[0]*len(words)
        sum=0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                sum+=1
            prefixarr[i]=sum
        for j in range(len(queries)):
            res[j]=prefixarr[queries[j][1]]-(0 if queries[j][0]==0 else prefixarr[queries[j][0]-1])
            
        return res
        
