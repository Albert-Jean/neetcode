public class Solution {
    public bool hasDuplicate(int[] nums) {
        Array.Sort(nums);
        bool result=false;
        int i=0;
        for(i; i<nums.Length;i++){
            if(nums[i]==nums[i+1]){
                result=true;
            }
        }
        return result;
    }
}