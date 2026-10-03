class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        n=len(s)
        maxi=0
        for i in range(n):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack!=[]:
                    pos=i-stack[-1]
                    maxi=max(maxi,pos)
                else:
                    stack.append(i)
        return maxi
