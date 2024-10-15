#include <stdio.h>
#define NO_SEMICOLON printf("%s-%s\n", __DATE__, __TIME__)
int main(void) {if (NO_SEMICOLON) {}}
