class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> stk,stk2;
        vector<int> res;
        int i=0;
        while (i<asteroids.size()){
            if (asteroids[i]>0){
                stk.push(asteroids[i]);
                i++;
            }
            else{
                if(!stk.empty() and stk.top()>0){
                int cur=stk.top();
                if (cur>-asteroids[i]){
                    i++;
                }
                else if (cur==-asteroids[i]){
                    stk.pop();
                    i++;
                }
                else{
                    stk.pop();
                }}
                else{
                    stk.push(asteroids[i]);
                    i++;
                }
            }
        }
    int n=stk.size();
    for (int i=0;i<n;i++){
        stk2.push(stk.top());
            stk.pop();
    }
    for (int i=0;i<n;i++){
        res.push_back(stk2.top());
        stk2.pop();
    }
    return res;

    
}};