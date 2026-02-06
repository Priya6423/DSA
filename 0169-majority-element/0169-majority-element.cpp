class Solution {
public:
    int majorityElement(vector<int>& nums) {
    int count=0,major=0;
    for(int i=0;i<nums.size();i++){
    if(count==0){
    major=nums[i];
    }
    if(major==nums[i]){
    count++;
    }else{
    count--;
    }
    }
    return major;
    }
};