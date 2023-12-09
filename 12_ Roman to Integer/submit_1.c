int romanToInt(char* s) {
  int result = 0;
  while (*s != '\0')
  {
    if (*s == 'I')
    {
      if (*(s + 1) == 'V'){
        result += 4;
        s++;
      }
      else if (*(s + 1) == 'X'){
        result += 9;
        s++;
      }
      else
        result += 1;
    }
    else if (*s == 'V')
      result += 5;
    else if (*s == 'X'){
      if (*(s + 1) == 'L'){
        result += 40;
        s++;
      }
      else if (*(s + 1) == 'C'){
        result += 90;
        s++;
      }
      else
      result += 10;
    }
    else if (*s == 'L')
      result += 50;
    else if (*s == 'C'){
      if (*(s + 1) == 'D'){
        result += 400;
        s++;
      }
      else if (*(s + 1) == 'M'){
        result += 900;
        s++;
      }
      else
      result += 100;
    }
    else if (*s == 'D')
      result += 500;
    else if (*s == 'M')
      result += 1000;
    s++;
  }
  return (result);
}