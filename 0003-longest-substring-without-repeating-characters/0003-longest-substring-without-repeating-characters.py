class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=set()
        left=0
        maxi=0
        for right in range(len(s)):
            while s[right] in ans:
                ans.remove(s[left])
                left+=1
            ans.add(s[right])
            maxi=max(maxi,right-left+1)
                
        return maxi

        