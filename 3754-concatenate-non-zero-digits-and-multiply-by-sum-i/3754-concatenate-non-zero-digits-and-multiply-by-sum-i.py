class Solution:
    def sumAndMultiply(self, n: int) -> int:
        cnt=0
        rev=0
        while n:
            digit=n%10
            if digit!=0:
                rev=rev*10+digit
            cnt+=digit
            n=n//10
        ans=0
        while rev:
            num=rev%10
            ans=ans*10+num
            rev=rev//10
        return ans*cnt

        