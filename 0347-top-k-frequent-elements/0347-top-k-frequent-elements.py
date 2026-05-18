class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        sorted_list=sorted(freq.items(),key=lambda pair:pair[1], reverse=True)
        for i in range(k):
            ans.append(sorted_list[i][0])
        return ans
        