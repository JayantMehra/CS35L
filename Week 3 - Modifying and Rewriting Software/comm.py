#!/usr/bin/python

"""
Compares two sorted or unsorted files to produce a column containing lines
unique to the first file, a column containing lines unique to the second line, and
a column containing common lines.

Created by Jayant Mehra on 1/25/18.
Copyright  2018 Jayant Mehra. All rights reserved
"""

import random, sys
import argparse

class comm:
    def __init__(self, filename1, filename2):
        if (filename2 == "-"):
            f_1 = open(filename1, 'r')
            self.lines_1 = f_1.readlines()
            self.lines_2 = []

            for line in sys.stdin:
                self.lines_2.append(line)

            f_1.close()

        elif (filename1 == "-"):
            f_2 = open(filename2, 'r')
            self.lines_1 = []

            for line in sys.stdin:
                self.lines_1.append(line)

            self.lines_2 = f_2.readlines()
            f_2.close()

        else:
            f_1 = open(filename1, 'r')
            f_2 = open(filename2, 'r')
            self.lines_1 = f_1.readlines()
            self.lines_2 = f_2.readlines()
            f_2.close()
            f_1.close()

    def stripLines(self):
        for i in range(len(self.lines_1)):
            self.lines_1[i] = self.lines_1[i].rstrip('\n')

        for j in range(len(self.lines_2)):
            self.lines_2[j] = self.lines_2[j].rstrip('\n')

    def compareFiles(self, unsorted_option, one, two, three):
        self.stripLines()
        counter_for_file_1 = 0
        counter_for_file_2 = 0

        #If the files are sorted
        if not unsorted_option:
            for i in range(len(self.lines_1)):
                if counter_for_file_2 == len(self.lines_2):
                    break

                j = 0
                while j <  len(self.lines_2) - counter_for_file_2:
                    if (self.lines_1[i] > self.lines_2[j + counter_for_file_2]):
                        if two:
                            counter_for_file_2 += 1
                        elif one:
                            sys.stdout.write(self.lines_2[j + counter_for_file_2] + "\n")
                            counter_for_file_2 += 1
                        else:
                            sys.stdout.write("\t" + self.lines_2[j + counter_for_file_2] + "\n")
                            counter_for_file_2 += 1

                    elif (self.lines_1[i] == self.lines_2[j + counter_for_file_2]):
                        if three:
                            counter_for_file_2 += 1
                            counter_for_file_1 += 1
                            break
                        elif two and not one or one and not two:
                            sys.stdout.write("\t" + self.lines_2[j + counter_for_file_2] + "\n")
                            counter_for_file_2 += 1
                            counter_for_file_1 += 1
                            break
                        elif one and two:
                            sys.stdout.write(self.lines_2[j + counter_for_file_2] + "\n")
                            counter_for_file_2 += 1
                            counter_for_file_1 += 1
                            break
                        else:
                            sys.stdout.write("\t\t" + self.lines_2[j + counter_for_file_2] + "\n")
                            counter_for_file_2 += 1
                            counter_for_file_1 += 1
                            break

                    else:
                        if one:
                            counter_for_file_1 += 1
                            break
                        else:
                            sys.stdout.write(self.lines_1[i] + "\n")
                            counter_for_file_1 += 1
                            break

            if counter_for_file_1 != len(self.lines_1):
                for k in range(len(self.lines_1) - counter_for_file_1):
                    if one:
                        continue
                    else:
                        sys.stdout.write(self.lines_1[k + counter_for_file_1] + "\n")

            if counter_for_file_2 != len(self.lines_2):
                for l in range(len(self.lines_2) - counter_for_file_2):
                    if two:
                        continue
                    elif one:
                        sys.stdout.write(self.lines_2[l + counter_for_file_2] + "\n")
                    else:
                        sys.stdout.write("\t" + self.lines_2[l + counter_for_file_2] + "\n")

        #If the files are unsorted i.e. -u is turned on
        else:
            for i in range(len(self.lines_1)):
                found = 0
                for j in range(len(self.lines_2)):
                    if self.lines_1[i] == self.lines_2[j]:
                        if three:
                            del self.lines_2[j]
                            found = 1
                            break
                        elif two and not one or one and not two:
                            sys.stdout.write("\t" + self.lines_1[i] + "\n")
                            del self.lines_2[j]
                            found = 1
                            break
                        elif one and two:
                            sys.stdout.write(self.lines_1[i] + "\n")
                            del self.lines_2[j]
                            found = 1
                            break
                        else:
                            sys.stdout.write("\t\t" + self.lines_1[i] + "\n")
                            del self.lines_2[j]
                            found = 1
                            break

                if not found:
                    if one:
                        continue
                    else:
                        sys.stdout.write(self.lines_1[i] + "\n")

            if not two:
                for k in range(len(self.lines_2)):
                    if one:
                        sys.stdout.write(self.lines_2[k] + "\n")
                    else:
                        sys.stdout.write("\t" + self.lines_2[k] + "\n")


def main():
    version_msg = "%prog 1.0"

    parser = argparse.ArgumentParser(usage="""%(prog)s [-123u] FILE1 FILE2
    Compares FILE1 and FILE2 for lines common to both files, and unique to each file
    """)

    parser.add_argument("-1", action="store_true", dest="one", help='Supresses column one')
    parser.add_argument("-2", action="store_true", dest="two", help='Supresses column two')
    parser.add_argument("-3", action="store_true", dest="three", help='Supresses column three')
    parser.add_argument("-u", action="store_true", dest="unsorted_option", help='Compares unsorted files')

    args, extras = parser.parse_known_args(sys.argv[1:])

    if len(extras) != 2:
        parser.error("wrong number of operands")

    if extras[0] == "-" and extras[1] == "-":
        parser.error("Expecting a filename")

    input_file_1 = extras[0]
    input_file_2 = extras[1]

    if args.unsorted_option:
        unsorted_option = True
    else:
        unsorted_option = False

    if args.one:
        one = True
    else:
        one = False

    if args.two:
        two = True
    else:
        two = False

    if args.three:
        three = True
    else:
        three = False

    try:
        compare = comm(input_file_1, input_file_2)
        compare.compareFiles(unsorted_option, one, two, three)
    except IOError as xxx_todo_changeme:
        (errno, strerror) = xxx_todo_changeme.args
        parser.error("I/O error({0}): {1}".
                     format(errno, strerror))

if __name__ == "__main__":
    main()
