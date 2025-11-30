#include <iostream>
#include "questions.h"

int add(int num1, int num2) {
    std::cout << "The addition of " << num1 << " and " << num2 << " = " << num1 + num2 << "\nPress ENTER to continue...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

int sub(int num1, int num2) {
    std::cout << "The subtraction of " << num1 << " and " << num2 << " is equals to " << num1 - num2 << "\nPress ENTER to continue...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

int mult(int num1, int num2) {
    std::cout << "The product of " << num1 << " and " << num2 << " is " << num1 * num2 << "\nPress ENTER to continue...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

int divs(int num1, int num2) {
    std::cout << "The division of " << num1 << " for " << num2 << " is equals to " << num1 / num2 << "\nPress ENTER to continue...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

int resDiv(int num1, int num2) {
    std::cout << "The rest of the division of " << num1 << " for " << num2 << " is equals to " << num1 % num2 << "\nPress ENTER to continue...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

int qst1(int num1, int num2) {
    std::cout << R"(Two number calculator
Select the operation you wish to use
with the two numbers typed previously 
1 - Add
2 - Sub
3 - Mult
4 - Div
5 - Res div)";
    int opr;
    std::cin >> opr;
    using funcPtr = int(*)(int, int);
    funcPtr funcs[5] = {add, sub, mult, divs, resDiv};
    std::cout << funcs[opr - 1](num1, num2);
    return 0;
}