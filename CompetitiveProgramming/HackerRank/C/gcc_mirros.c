#include <stdio.h>


int main (void) {
  char *dig_str[9] = {
    "one", "two", "three", "four", "five", "eight", "nine"
  };

  int n = 44;

  printf("%s \n", dig_str[(n - 1)]);
  return 0;

}
