class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxi=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if stack!=[]:
                    rangee=i-stack[-1]
                    maxi=max(maxi,rangee)
                else:
                    stack.append(i)
        return maxi