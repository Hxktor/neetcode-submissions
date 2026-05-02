class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const indicies = {}; 
        for (let i = 0; i < nums.length; i++){
            indicies[nums[i]] = i; 
    
        }
        for( let i = 0; i < nums.length; i++){
            let diff = target - nums[i]; 
            if (indicies[diff]!== undefined && indicies[diff]!== i)
            return [i, indicies[diff]]; 
        }
        return [];
    }
}
