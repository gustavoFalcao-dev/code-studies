#include <iostream>
#include <cstdlib>
#include <array>
#include "questions.h"
#include "utils.h"


int main() {
    int answer1, answer2, answerQst;
    std::cout << "Type the first number: ";
    std::cin >> answer1;
    std::cout << "Type the second number: ";
    std::cin >> answer2;
    std::cout << R"(Choose a question:
Question 1 - Two number calc
Answer: )";
    std::cin >> answerQst;
    using funcPtr = int(*)(int, int);
    funcPtr funcs[7] = {qst1, qst2, qst3, qst4, qst5, qst6, qst7};
    std::cout << funcs[answerQst -1](answer1, answer2);
    return 0;
}