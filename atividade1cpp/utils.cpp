#include <iostream>
#include "utils.h"
//TODO Test this, dont really know if it works


void clear() {
    #ifdef _WIN32
        system("cls")
    #else
        system("clear")
    #endif
}