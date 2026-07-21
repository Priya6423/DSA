class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        freqp={}
        freqs={}
        left=0
        for ch in p:
            if ch in freqp:
                freqp[ch]+=1
            else:
                freqp[ch]=1
        
        for right in range(len(s)):
            if right-left>len(p)-1:
                freqs[s[left]]-=1
                if freqs[s[left]]==0:
                    del freqs[s[left]]
                left+=1
                if s[right] in freqs:
                    freqs[s[right]]+=1
                else:
                    freqs[s[right]]=1
            else:
                if s[right] in freqs:
                    freqs[s[right]]+=1
                else:
                    freqs[s[right]]=1
            if freqs==freqp:
                ans.append(left)
        return ans

            
        
            

        
        
        

    
        