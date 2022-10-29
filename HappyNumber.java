class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> alreadyFound = new HashSet<>();

        while(n != 1) {
            ArrayList<Integer> digits = new ArrayList<>();
            while(n > 0) {
                digits.add(n % 10);
                n = (n - (n % 10)) / 10;
            }
    
            int result = 0;
            for(int i = 0; i < digits.size(); i++) {
                result += Math.pow(digits.get(i), 2);
            }

            if(alreadyFound.contains(result)) {
                return false;
            } else {
                alreadyFound.add(result);
                n = result;
            }
        }
        return true;
    }  
}
