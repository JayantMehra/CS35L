#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

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
  //  END OF ERROR CHECKING                                                                                                       \

  char* ch = (char*)malloc(sizeof(char));
  int i;
  int flag = 0;

  while (read(0,ch,1) > 0) {
    flag = 0;
    if (*ch == EOF)
      break;

    for (i = 0; i < strlen(argv[1]); i++) {
      if (argv[1][i] == *ch) {
        char *temp = (char*)malloc(sizeof(char));
        *temp = argv[2][i];
        write(1,temp,1);
        flag++;
        free(temp);
        break;
      }
    }
    if (!flag) {
      write(1,ch,1);
    }
    free(ch);
    ch = (char*)malloc(sizeof(char));
  }
  free(ch);
  return 0;
}
