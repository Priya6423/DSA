class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=len(arr)
        array=[0]*n
        count=1
        for i in range(n):
            array[i]=arr[i]
        array.sort()
        freq={}
        for i in range(n):
            if array[i] in freq:
                continue
            else:
                freq[array[i]]=count
                count+=1
        ans=[]
        for i in range(n):
            ans.append(freq[arr[i]])
        return ans

        