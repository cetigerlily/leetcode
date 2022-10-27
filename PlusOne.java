class Solution {
    public int[] plusOne(int[] digits) {
        for(int i = digits.length - 1; i >= 0; i--) {
            if(digits[i] != 9) {
                digits[i] += 1;
                break;
            } else {
                digits[i] = 0;
            }
        }

        int[] answer = new int[digits.length + 1];
        if(digits[0] == 0) {
            answer[0] = 1;
            for(int i = 1; i < answer.length; i++) {
                answer[i] = 0;
            }
            return answer;
        } else {
            return digits;
    
        }
    }
}
