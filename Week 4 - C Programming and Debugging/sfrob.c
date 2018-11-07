#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int cmp(const void* a, const void* b);

int main() {
  //  Takes the entire input stream
  char *input, *tempInput;

  //  Stores individual words
  char *item, *temp;

  //  Stores an array of words
  char **itemArray, **temp2;

  char currentChar;
  char ch;
  int i = 0;    //  Counter for the number of characters in the input
  int j = 0;    //  Counter for the number of words
  int k = 0;
  int l = 0;    //  Represents the characters in each word


  char* memError = "Memory Allocation Failed.";
  char* ioError = "I/O Error";
  char* remError = "Memory Reallocation Failed.";


  input = (char*)malloc(sizeof(char));
  item = (char*)malloc(sizeof(char));
  itemArray = (char**)malloc(sizeof(char*));

  if (input == NULL || item == NULL || itemArray == NULL) {
    fprintf(stderr, "%sError:%d\n",memError, errno);
    exit(1);
  }

  while (!feof(stdin)) {
    currentChar = getchar();
    if (ferror(stdin)) {
      fprintf(stderr, "%sError:%d\n",ioError, errno);
      exit(1);
    }
    if (currentChar == EOF)
      break;

    input[i++] = currentChar;
    tempInput = realloc(input, (i+1)*sizeof(char));
    if (tempInput == NULL) {
      fprintf(stderr, "%sError:%d\n",remError, errno);
      free(input);
      exit(1);
    }
    input = tempInput;
  }

  if (i > 0 && input[i - 1] != ' ')
    input[i++] = ' ';

  for (k = 0; k < i; k++) {
    ch = input[k];
    item[l++] = ch;
    temp = realloc(item, (l+1)*sizeof(char));
    if (temp == NULL) {
      fprintf(stderr, "%s Error:%d\n",remError, errno);
      free(input);
      free(item);
      exit(1);
    }
    item = temp;

    if (ch == ' ') {
      l = 0;
      itemArray[j++] = item;
      temp2 = realloc(itemArray, (j+1)*sizeof(char*));
      if (temp2 == NULL) {
        fprintf(stderr, "%sError:%d\n",remError, errno);
        free(input);
        free(item);
        exit(1);
      }
      itemArray = temp2;
      item = NULL;
      item = (char*)malloc(sizeof(char));
      if (item == NULL) {
        fprintf(stderr, "%sError:%d\n",memError, errno);
        free(input);
        free(item);
        exit(1);
      }
    }
  }

  //   Function to pass to qsort
  int (* toPass)(const void*, const void*);
  toPass = &cmp;
  qsort(itemArray,j, sizeof(char*), toPass);

  // print the words
  for (int g = 0; g < j; g++) {
    printf("%s", itemArray[g]);
  }

  free(item);
  free(itemArray);
  return 0;
}


int frobcmp(char const* a, char const* b) {
  while (*a == *b) {
    if (*a == ' ')
      return 0;
    a++;
    b++;
  }
  return (*a ^ 42) - (*b ^ 42);
}

int cmp(const void* a, const void* b) {
 return frobcmp(*((const char**) a), *((const char**) b));
}
