class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=len(a)
        m=len(b)
        aa=0
        bb=0
        for i in range(n-1,-1,-1):
            aa+=int(a[i])*2**(n-i-1)
        for i in range(m-1,-1,-1):
            bb+=int(b[i])*2**(m-i-1)
        ans=aa+bb
        if ans==0:
            return '0'
        fans=""
        while ans>0:
            fans=str(ans%2)+fans
            ans//=2
        return fans



        

        