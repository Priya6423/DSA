class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        mul=1
        num=n
        while num:
            digit=num%10
            mul*=digit
            summ+=digit
            num=num//10
        ans=mul+summ
        if n%ans==0:
            return True
        return False