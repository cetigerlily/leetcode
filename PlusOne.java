class Solution {
    public int[] plusOne(int[] digits) {
        long originalNumber = 0;
        int exponent = 0;

        for(int i = digits.length - 1; i >= 0; i--) {
            originalNumber += digits[i] * Math.pow(10, exponent);
            exponent += 1;
        }

        long newNumber = originalNumber + 1;
        int length = String.valueOf(newNumber).length();
        int[] answer = new int[length];

        for(int i = length - 1; i >= 0; i--) {
            long value = newNumber % 10;
            newNumber = (newNumber - value) / 10;
            answer[i] = (int) value;
        }
        return answer;
    }
}
