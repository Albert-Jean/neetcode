public class Solution {
    public int[] TwoSum(int[] nums, int target) {
      for(int i = 0; i < nums.Length; i++){
        int pos = Array.IndexOf(nums, target - nums[i]);
        if(pos > -1 && pos != i){
            return new int[]{i, pos};
        }
      }
      return new int[0];
    }
}
