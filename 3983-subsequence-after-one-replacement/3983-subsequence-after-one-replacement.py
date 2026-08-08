class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n,m=len(s),len(t)
        if n>m: return False
        pre=[0]*(n+1)
        j=0
        INF=m+1
        for i in range(n):
            while j<m and s[i]!=t[j]:
                j+=1
            if j<m:
                j+=1
                pre[i+1]=j
            else:
                pre[i+1]=INF
        if pre[n]<=m:
            return True
        suf=[0]*(n+1)
        j=m-1
        for i in range(n-1,-1,-1):
            while j>=0 and s[i]!=t[j]:
                j-=1
            if j>=0:
                suf[i]=m-j
                j-=1
            else:
                suf[i]=INF
        for k in range(n):
            if pre[k]<INF and suf[k+1]<INF and pre[k]+suf[k+1]<m:
                return True
        return False

        