class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count=0
        stack=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack!=[]:
                    pos=i-stack[-1]
                    count=max(count,pos)
                else:
                    stack.append(i)

        return count
