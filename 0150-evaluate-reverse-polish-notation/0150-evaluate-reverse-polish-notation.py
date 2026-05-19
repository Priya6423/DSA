class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        ans=[]
        for i in tokens:
            if i in ("+","-","*","/"):
                b=ans.pop()
                a=ans.pop()
            if i=="+":
                ans.append(a+b)
            elif i=="-":
                ans.append(a-b)
            elif i=="*":
                ans.append(a*b)
            elif i=="/":
                ans.append(int(a/b))
            else:
                ans.append(int(i))
        return ans[-1]

        