#include <stack>

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stk;

        for (char c : s) {

            if (c == '(' || c == '[' || c == '{') {
                stk.push(c);

            } else {

                if (stk.empty()) {
                    return false;
                }

                char top = stk.top();

                if ((top == '{' && c == '}') ||
                    (top == '[' && c == ']') ||
                    (top == '(' && c == ')')) {

                    stk.pop();

                } else {
                    return false;
                }
            }
        }

        if (stk.size()) {
            return false;
        }

        return true;
    }
};
