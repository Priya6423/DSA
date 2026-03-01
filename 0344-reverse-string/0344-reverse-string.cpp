class Solution {
public:
vector<char> rev(vector<char>& s,int st,int e){
if(st>=e){
return s;
}else{
swap(s[st],s[e]);
}
return rev(s,st+1,e-1);
}
void reverseString(vector<char>& s) {
    int st=0,e=s.size()-1;
    rev(s,st,e);
    }
};