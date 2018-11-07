#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <ctype.h>

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

int frobcmp2(char const* a, char const* b) {
  while (toupper(*a) == toupper(*b)) {
    if (*a == ' ')
      return 0;
    a++;
    b++;
  }
  return (toupper(*a) ^ 42) - (toupper(*b) ^ 42);
}

int cmp2(const void* a, const void* b) {
 return frobcmp2(*((const char**) a), *((const char**) b));
}

int main(int argc, char **argv){

    int c = getopt (argc, argv, "f");
    struct stat info;

    char currentCH;
    char *input, *temp, *item;
    char **itemArray;

    int itemNum = 0, itemSize = 0, bufferSize = 0, endOfFile = 0;
    int fileSize, errorChecker;

    char* memError = "Memory Allocation Failed.";
    char* ioError = "I/O Error";
    char* remError = "Memory Reallocation Failed.";

    errorChecker = fstat(0, &info);

    if (errorChecker < 0) {
      fprintf(stderr, "%sError:%d\n",ioError, errno);
      exit(1);
    }

    fileSize = info.st_size + 1;
    input = (char*)malloc(fileSize*sizeof(char));
    if (input == NULL) {
      fprintf(stderr, "%sError:%d\n",memError, errno);
      exit(1);
    }
    item = input;
    char store[1];

    while (!endOfFile) {
      errorChecker = read(0, store, 1);
      if (errorChecker < 0) {
        fprintf(stderr, "%sError:%d\n",ioError, errno);
        free(item);
        exit(1);
      }

      currentCH = *store;
      endOfFile = !errorChecker;

      if (!itemSize && currentCH == ' ')
        continue;

      if (bufferSize == fileSize) {
        fileSize = fileSize + 10;
        temp = (char*) realloc(input, fileSize*sizeof(char));
        if (temp == NULL) {
          fprintf(stderr, "%sError:%d\n",memError, errno);
          free(input);
          exit(1);
        }
        input = temp;
      }

      if (!endOfFile){
        input[bufferSize++] = currentCH;
        itemSize++;
        if (currentCH != ' ')
          continue;
      }
      else {
        if (input[bufferSize-1] != ' ')
            input[bufferSize++] = ' ';
        if (!itemSize)
            break;
      }
      itemSize = 0;
      itemNum++;
    }

  itemArray = (char**)malloc(itemNum*sizeof(char*));
  if (itemArray == NULL) {
    fprintf(stderr, "%sError:%d\n",memError, errno);
    free(item);
    exit(1);
  }

  int k = 0, l = 0;
  char* x = input;
  for (; k < bufferSize; k++){
    if (input[k] == ' '){
        itemArray[l++] = x;
        x = input+k+1;
    }
  }

  if (c == -1) {
    int (* toPass) (const void*, const void*);
    toPass = &cmp;
    qsort(itemArray, itemNum, sizeof(char*), toPass);
  }
  else {
    int (* toPass) (const void*, const void*);
        toPass = &cmp2;
        qsort(itemArray, itemNum, sizeof(char*), toPass);
  }

  for (int i = 0; i < itemNum; i++) {
    while(1){
	     if (write(1,itemArray[i], 1) < 0) {
          fprintf(stderr, "%sError:%d\n",ioError, errno);
          free(itemArray);
          free(input);
          exit(1);
        }
        if (*(itemArray[i])++ == ' ')
	       break;
      }
    }

    free(itemArray);
    free(input);
    return 0;
}
