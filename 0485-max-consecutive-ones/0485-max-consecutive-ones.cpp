class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int left=0;
        int max_count=0;
        for(int right=0;right<nums.size();right++){
            if(nums[right]!=0 && right>=left) max_count=max(right-left+1,max_count);
            else{
                left=right+1;
            }
        }
        return max_count;
        
    }
};