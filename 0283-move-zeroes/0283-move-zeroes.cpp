class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    int n=nums.size();
    int i=0,j=i+1;
    while(j<nums.size() && i<nums.size()){
    if(nums[i]==0 && nums[j]!=0){
    swap(nums[i],nums[j]);
    i++;
    j++;
    }
    else if(nums[j]==0 && nums[i]!=0){
    i++;
    j++;
    }else if(nums[i]==0 && nums[j]==0){
    j++;
    }else{
    i++;
    j++;
    }
    }
    }
};