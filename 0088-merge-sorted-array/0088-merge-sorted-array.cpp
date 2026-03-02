class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int p=m+n-1,q=m-1,r=n-1;
    while(p>=0 && q>=0 && r>=0){
    if(nums1[q]>nums2[r]){
    nums1[p--]=nums1[q--];
    }else{
    nums1[p--]=nums2[r--];
    }
    }
    while(r>=0){
    nums1[p--]=nums2[r--];
    }
    }
};