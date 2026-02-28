class Solution {
public:
    int Bsearch(vector<int>& nums,int s,int e,int k){
    int mid=s+(e-s)/2;
    if(s>e){
    return -1;
    }
    if(nums[mid]==k){
    return mid;
    }
    else if(nums[mid]>k){
    return Bsearch(nums,s,mid-1,k);
    }
    else{
    return Bsearch(nums,mid+1,e,k);
    }
    }
    int search(vector<int>& nums, int target) {
    int s=0,e=nums.size()-1;
    return Bsearch(nums,s,e,target);
    }
};