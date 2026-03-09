class Solution {
public:
    int firstpos(vector<int> nums,int low,int high,int target){
    int ans=-1;
    while(low<=high){
     int mid=low+(high-low)/2;
    if(nums[mid]==target){
    ans=mid;
    high=mid-1;
    }else if(nums[mid]>target){
    high=mid-1;
    }else{
    low=mid+1;
    }
    }
    return ans;
    }
    int lastpos(vector<int> nums,int low,int high,int target){
    int ans=-1;
    while(low<=high){
     int mid=low+(high-low)/2;
    if(nums[mid]==target){
    ans=mid;
    low=mid+1;
    }else if(nums[mid]>target){
    high=mid-1;
    }else{
    low=mid+1;
    }
    }
    return ans;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
   
    int k=firstpos(nums,0,nums.size()-1,target);
    int l=lastpos(nums,0,nums.size()-1,target);
    return {k,l};
    }
};