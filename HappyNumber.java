class Solution {
    public boolean isHappy(int n) {
        ArrayList<Integer> digits = new ArrayList<>();
        while(n > 0) {
            digits.add(n % 10);
            n = (n - (n % 10)) / 10;
        }

        int result = 0;
        for(int i = 0; i < digits.size(); i++) {
            result += Math.pow(digits.get(i), 2);
        }

        if(result == 1) {
            return true;
        } else {
            return isHappy(result);
        }
    }
}
