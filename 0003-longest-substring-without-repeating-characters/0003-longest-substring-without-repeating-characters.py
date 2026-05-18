class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        count=0
        maxi=0
        left=0
        right=0
        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                count-=1
                left+=1
            
            count+=1
            seen.add(s[right])
            right+=1
            maxi=max(count,maxi)
        return maxi