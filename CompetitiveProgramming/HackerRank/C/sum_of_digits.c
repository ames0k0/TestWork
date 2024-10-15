#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
  int n = 99999;
  // scanf("%d", &n);
  //Complete the code to calculate the sum of the five digits on n.
  // char str[6];
  // itoa(n, str, 10);

  // sprintf(str, "%d", n);
  // printf("%s\n", str);
  //sprintf()
  int i = 0;
  // printf("%s\n", str);

  for (int j = 0;; j++) {
    int k = (n % 10);

    // printf("%d - %d\n", n, k);

    // printf("n=%d, k=%d, i=%d\n", n, k, i);

    if (k == 0) {
      n /= 10;

      if (n == 10) {
        i += 1;
        break;
      }

    } else {
      i += k;
      n -= k;
    }

    if (n == 0) {
      break;
    }


    // char s[1] = &str[j];
    // printf("s=%c\n", s);
    // int b = atoi(s);
    // printf("b=%d\n", b);
    // i += b;
    // if (str[j] != '0') {
    //     printf("(%c<%d>)|", str[j], atoi(&s));
    // }
  }
  printf("%d\n", i);
  return 0;
}
