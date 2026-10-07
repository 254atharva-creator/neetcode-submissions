class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        vector<int> a;
        for (int i=0;i<n;i++){
            if (nums[i]!=val){
                a.push_back(nums[i]);
            }
        }
        nums=a;
        return a.size();
    }
};