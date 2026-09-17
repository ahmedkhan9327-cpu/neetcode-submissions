class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int T = 0;
        int B = matrix.size() - 1;

        int L = 0;
        int R = matrix[0].size() - 1;

        int row = -1;

        while (T <= B) {
            int RM = T + (B - T) / 2;

            if (matrix[RM][0] > target) {
                B = RM - 1;
            } else if (matrix[RM][R] < target) {
                T = RM + 1;
            } else {
                row = RM;
                break;
            }
        }

        if (row == -1) {
            return false;
        }

        while (L <= R) {
            int CM = L + (R - L) / 2;

            if (matrix[row][CM] < target) {
                L = CM + 1;
            } else if (matrix[row][CM]> target) {
                R = CM - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
