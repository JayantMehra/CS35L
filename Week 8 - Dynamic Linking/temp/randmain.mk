gcc -c randlibhw.c -o randlibhw.o
gcc -c -fpic randlibsw.c -o randlibsw.o
gcc -c -fpic randcpuid.c -o randcpuid.o

ar -cvq randcpuid.a randcpuid.o
gcc -shared -fpic -o randlibhw.so randlibhw.o
gcc -shared -fpic -o randlibsw.so randlibsw.o

-ldl -Wl, -rpath=$PWD
