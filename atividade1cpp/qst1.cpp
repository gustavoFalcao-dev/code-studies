#include <iostream>
#include "questions.h"
#include "utils.h"


int add(int num1, int num2) {
    std::cout << "The addition of " << num1 << " and " << num2 << " is esquals to " << num1 + num2 << "\nPress ENTER to continue...";
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

int qst1() {
    int answer1, answer2, opr;
    std::cout << R"(Two number calculator
You'll be prompted to enter two numbers
and after that you should select which
operator you wish to use.
Press ENTER to continue...)";
    std::cin.ignore();
    std::cin.get();
    std::cout << "Type the first number: ";
    std::cin >> answer1;
    std::cout << "Type the second number: ";
    std::cin >> answer2;
    std:: cout << R"(1 - Add
2 - Sub
3 - Mult
4 - Div
5 - Res div
Answer: )";
    std::cin >> opr;
    using funcPtr = int(*)(int, int);
    funcPtr funcs[5] = {add, sub, mult, divs, resDiv};
    std::cout << funcs[opr - 1](answer1, answer2);
    return 0;
}