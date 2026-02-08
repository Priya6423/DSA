class Solution {
public:
    int fibo(int n){
    if(n<2) return n;
    int prev1=0;
    int prev2=1;
    int curr=0;
    int count=1;
    while(count<n){
    curr=prev2+prev1;
    prev1=prev2;
    prev2=curr;
    count++;
    }
    return curr;
    }
    int fib(int n) {
    int ans=fibo(n);
    return ans;

    }
};