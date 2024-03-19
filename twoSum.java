//Problem 1
import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap();
        for (int i=0; i<nums.length; i++){
            int comp = target - nums[i];
            if(m.containsKey(comp)){
                return new int[] {m.get(comp) , i};
            }
            m.put(nums[i],i);
        }
        return null;
    }
}    