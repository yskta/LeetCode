#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

bool isPalindrome(int x) {
    char str[20]; // 十分な大きさの文字列配列を確保
    int digit;
    int i = 0;

    if (x < 0)
        return false;
    else if (0 <= x && x <= 9)
        return true;
    else {
        // snprintfを使用して整数を文字列に変換
        snprintf(str, sizeof(str), "%d", x);
        digit = strlen(str);

        while (i <= digit / 2) {
            if (str[i] != str[digit - i - 1])
                return false;
            i++;
        }
    }

    return true;
}

int main()
{
  int x = 10;
  if (isPalindrome(x))
	printf("true\n");
  else
	printf("false\n");
  return (0);
}