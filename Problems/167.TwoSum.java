//Problem 167
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap <Integer, Integer> m = new HashMap();
        for(int i=0; i<numbers.length; i++){
            int comp = target - numbers[i];
            if(m.containsKey(comp)){
                return new int[] {m.get(comp)+1, i+1};
            }
            m.put(numbers[i], i);
        }
        return null;
    }
}