class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> loc;
        int n=nums.size();
        for (int i=0;i<n;i++){
            if(loc.contains(nums[i])){
                if (abs(loc[nums[i]]-i)<=k){return true;}
            }
            loc[nums[i]]=i;
        }
        return false;
    }
};