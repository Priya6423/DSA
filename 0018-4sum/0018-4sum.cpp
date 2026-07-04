class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
    int n=nums.size();
    sort(nums.begin(),nums.end());
    set<vector<int>> set;
    vector<vector<int>> ans;
    for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
    int k=j+1,l=n-1;
    while(k<l){
    long long sum=nums[i];
    sum+=nums[j];
    sum+=nums[k];
    sum+=nums[l];
    if(sum==target){
    set.insert({nums[i],nums[j],nums[k],nums[l]});
    k++;
    l--;
    }else{
    if(sum<target){
    k++;
    }
    else
    l--;
    }
    }
    }
    }
    for(auto it:set){
    ans.push_back(it);
    }
    return ans;  
    }
};