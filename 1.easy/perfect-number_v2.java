class Solution {
    public boolean checkPerfectNumber(int num) {

        if (num % 2 != 0) {
            return false;
        }
        
        int n = 1;
        while ((1 << n) - 1 <= num) {
            if ((1 << (n - 1)) * ((1 << n) - 1) == num) {
                if (isMersenne((1 << n) - 1)) {
                    return true;
                }
            }
            n++;
        }

        return false;
    }

    private boolean isMersenne(int num) {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;

        for (int i = 3; i * i <= num; i += 2) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }
}