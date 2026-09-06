class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        vector<int> maxsuf(n,0);
        int maxer=0;
        if (n==1){
            return 0;
        }
        for (int i=n-2;i>=0;i--){
            maxsuf[i]=max(prices[i+1],maxsuf[i+1]);
            maxer=max(maxer,maxsuf[i]-prices[i]);
        }
        return maxer;
    }
};
