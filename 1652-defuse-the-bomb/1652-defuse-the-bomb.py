class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        ans=[0]*n
        for i in range(n):
            if k>0:
                for j in range(i+1,i+k+1):
                    ans[i]+=code[j%n]
            elif k<0:
                for j in range(i-1,i-abs(k)-1,-1):
                    ans[i]+=code[j%n]
        return ans


        