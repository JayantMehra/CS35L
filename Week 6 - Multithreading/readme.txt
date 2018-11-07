1. Issues I ran into:

The provided baseline.ppm files contains a number of whitelines here and there.
My multithreaded implementation did not output any whitelines except at the end.
Therefore, the 'make clean check' command always exited with a return status of
1 because diff produced an output.

Therefore, I ran the following commands to remove all whitelines from baseline.ppm:

cat baseline.ppm | sed '/^$/d' > x.txt
cp x.txt baseline.ppm
rm x.txt

And then I manually added a whiteline at the end.

make clean check works well after that and the output produced is in the
make-log.txt file of the homework.

2. My SRT implementation

As it is evident by the time calls recorded in make-log.txt, the multithreaded
implementation of SRT is extremely fast. Each new thread makes the implementation
faster by 'number_of_threads_added' times faster. That is, an 8 thread
implementation is 8 times faster.
