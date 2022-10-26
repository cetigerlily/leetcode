public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, ArrayList<Integer>> numInput = new HashMap<>(); // <index, value>
        for(int i = 0; i < nums.length; i++) {
            if(numInput.containsKey(nums[i])) {
                numInput.get(nums[i]).add(i);
            } else {
                numInput.put(nums[i], new ArrayList<>());
                numInput.get(nums[i]).add(i);
            }
        }

        int[] answer = new int[2];
        for(int i = 0; i < nums.length; i++) {
            int currentValue = nums[i];
            int difference = target - currentValue;

            if(numInput.containsKey(difference)) {                
                if((currentValue == difference) && (numInput.get(difference).size() >= 2)) { // when more than one of the value
                    answer[0] = numInput.get(difference).get(0);
                    answer[1] = numInput.get(difference).get(1);

                } else if(currentValue != difference) {
                    answer[0] = i;
                    answer[1] = numInput.get(difference).get(0);
                } else {
                    continue;
                }
                break;
            }
        }
        return answer;
    }
}
