class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen = {};
        for (let num of nums){
            if(seen[num]){
                return true;
            }
            seen[num] = true;
        }
        return false;
    }
}
