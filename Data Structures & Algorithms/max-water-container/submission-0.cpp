class Solution {
public:
    int maxArea(vector<int>& heights) {
        int L = 0, R = heights.size() - 1;
        int width = R - L, height = min(heights[L], heights[R]), maxArea = 0;

        while (L < R) {
            int currArea = height * width;
            maxArea = max(currArea, maxArea);

            if (heights[L] < heights[R]) {
                L++;
            } else {
                R--;
            }

            height = min(heights[L], heights[R]);
            width = R - L;
        }
        return maxArea;
    }
};
