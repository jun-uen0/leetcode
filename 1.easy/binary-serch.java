class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1; // 5

        while (left <= right) {
            int middle = (left + right) / 2;

            if(nums[middle] == target) {
                return middle;
            } else if (target > nums[middle]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return -1;
    }
}

for (int i = 0; i < 配列の長さ -1; i++) {
    // iが5783だったらtrue、もしくはインデックス番号を返す
}

