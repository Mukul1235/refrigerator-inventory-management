#include <bits/stdc++.h>
using namespace std;

class Solution {
    stack<long long> numbers; 
    stack<char> operators;   
    unordered_map<char, long long> precedence{ {'+', 1}, {'-', 1}, {'*', 2}, {'/', 2} };

    void evaluateTop() {
        long long rightOperand = numbers.top(); numbers.pop();
        char operatorSymbol = operators.top(); operators.pop();
        switch (operatorSymbol) {
            case '+': numbers.top() += rightOperand; break;
            case '-': numbers.top() -= rightOperand; break;
            case '*': numbers.top() *= rightOperand; break;
            case '/': numbers.top() /= rightOperand; break;
        }
    }

public:
    int calculate(string expression) {
        for (int i = 0, length = expression.size(); i < length; ++i) {
            if (expression[i] == ' ') continue;
            if (isdigit(expression[i])) {
                long long currentNumber = 0;
                while (i < length && isdigit(expression[i])) 
                    currentNumber = currentNumber * 10 + expression[i++] - '0';
                --i;
                numbers.push(currentNumber);
            } else if (expression[i] == '(') {
                operators.push(expression[i]);
            } else if (expression[i] == ')') {
                while (operators.top() != '(') 
                    evaluateTop();
                operators.pop();
            } else {
                while (!operators.empty() && operators.top() != '(' && 
                       precedence[operators.top()] >= precedence[expression[i]]) 
                    evaluateTop();
                operators.push(expression[i]);
            }
        }
        while (!operators.empty()) 
            evaluateTop();
        return numbers.top();
    }
};

int main() {
    Solution soln;

    // Examples
    string exp1 = "25+5-(4*5-5)";         // Mixed operations with parentheses
    string exp2 = "24-8+9*2-10/5";        // Simple operations without parentheses
    string exp3 = "(10+5)*3";             // Parentheses changing order of operations
    string exp4 = "100/(2+3)";            // Division with parentheses
    string exp5 = "50-10*5/2+1";          // Complex expression with all operations
    string exp6 = "42";                   // Single number
    string exp7 = "(50+25)-25";           // Nested parentheses
    string exp8 = "((3+5)*2)-8/2";        // Deeply nested parentheses
    string exp9 = "100-((2+3)*4)";        // Complex expression with subtraction and parentheses
    string exp10 = "12+(18/(9-(2+1)))";   // Division with nested parentheses

    vector<string> expressions = {exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10};

    for (int i = 0; i < expressions.size(); ++i) {
        cout << "Expression " << i + 1 << ": " << expressions[i] << endl;
        cout << "Result: " << soln.calculate(expressions[i]) << endl;
        cout << "--------------------" << endl;
    }

    return 0;
}
