class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            num=i
            pro=1
            while num:
                digi=num%10
                pro*=digi
                num=num//10
            if pro%t==0:
                return i
        return -1



        