#include <immintrin.h>
#include "randlib.h"


__attribute__((constructor))
static void
hardware_rand64_init (void)
{
}

extern unsigned long long rand64 (void) {
  unsigned long long int x;
  while (! _rdrand64_step (&x))
    continue;
  return x;
}


__attribute__((destructor))
static void
hardware_rand64_fini (void)
{
}
