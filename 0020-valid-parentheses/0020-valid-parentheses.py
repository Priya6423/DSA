class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        ans=[]
        for i in s:
            if i in "{([":
                ans.append(i)
            else:
                if not ans:
                    return False
                if i=='}' and ans[-1]=='{':
                    ans.pop()
                elif i==']' and ans[-1]=='[':
                    ans.pop()
                elif i==')' and ans[-1]=='(':
                    ans.pop() 
                else:
                    return False  

        return not ans
                 

        