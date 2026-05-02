class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i =0; i < nums.size(); i ++){  // brute force method checking every possibility
            for(int j = i + 1; j < nums.size(); j++) // that adds up to target and returns indicies 
            if (nums [i] + nums[j] == target){
                return {i,j}; // returns indicies of the target
            }

        }
    return {};

    }
};
