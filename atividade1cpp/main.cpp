#include <iostream>
#include <cstdlib>
#include <array>
#include "questions.h"
#include "utils.h"


int main() {
    int answerQst;
    std::cout << R"(Choose a question:
Question 1 - Two number calc
Answer: )";
    std::cin >> answerQst;
    using funcPtr = int(*)();
    funcPtr funcs[7] = {qst1, qst2, qst3, qst4, qst5, qst6, qst7};
    std::cout << funcs[answerQst -1]();
    return 0;
}