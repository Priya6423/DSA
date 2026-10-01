class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif not stack or mapp[stack[-1]]!=i:
                return False
            else:
                stack.pop()
        return len(stack)==0