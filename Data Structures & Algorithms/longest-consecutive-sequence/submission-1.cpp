class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> store(nums.begin(), nums.end());

        int longest = 0;

        for (int num : nums) {
            if (store.find(num - 1) == store.end()) {
                int streak = 0, curr = num;

                while (store.find(curr) != store.end()) {
                    streak++;
                    curr++;
                }

                longest = max(longest, streak);
            }
        }
        
        return longest;
    }
};
