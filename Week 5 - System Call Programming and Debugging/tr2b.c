#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {


  //  ERROR CHECKING
  if (strlen(argv[1]) != strlen(argv[2])) {
    fprintf(stderr, "Argument lengths must match\n");
    exit(1);
  }

  for (int i = 0; i < strlen(argv[1])-1; i++) {
    for (int j = i+1; j < strlen(argv[1]); j++) {
      if (argv[1][i] == argv[1][j]) {
        fprintf(stderr, "The first argument cannot have duplicate bytes\n");
        exit(1);
      }
    }
  }
  //  END OF ERROR CHECKING

  char ch;
  int i;
  int flag = 0;

  while (!feof(stdin)) {
    flag = 0;
    ch = getchar();
    if (ch == EOF){
      break;
    }

    for (i = 0; i < strlen(argv[1]); i++) {
      if (argv[1][i] == ch) {
        putchar(argv[2][i]);
        flag++;
        break;
      }
    }
    if (!flag) {
      putchar(ch);
    }

  }
  return 0;
}
