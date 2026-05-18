class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        ans=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                ans.append(i)
            elif i==")":
                if ans and ans[-1]=="(":
                    ans.pop()
                else:
                    return False
            elif i=="}":
                if ans and ans[-1]=="{":
                    ans.pop()
                else:
                    return False
            elif i=="]":
                if ans and ans[-1]=="[":
                    ans.pop()
                else:
                    return False
        return len(ans)==0
            
        