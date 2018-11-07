#!/usr/bin/python

"""
Compares two sorted or unsorted files and outputs a column of lines unique to file1,
a column of lines unique to file2, and a column of lines common to both files.
"""

import random, sys
from optparse import OptionParser

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
    usage_msg = """%prog [OPTION] ... FILE1 FILE2
    Compares two FILE1 and FILE2 for lines common to both files, and
    unique to each file
    """

    parser = OptionParser(version=version_msg, usage=usage_msg)

    parser.add_option("-1", action="store_true", dest="one")
    parser.add_option("-2", action="store_true", dest="two")
    parser.add_option("-3", action="store_true", dest="three")
    parser.add_option("-u", action="store_true", dest="unsorted_option")

    options, args = parser.parse_args(sys.argv[1:])

    if len(args) != 2:
        parser.error("wrong number of operands")

    input_file_1 = args[0]
    input_file_2 = args[1]

    if options.unsorted_option:
        unsorted_option = True
    else:
        unsorted_option = False

    try:
        compare = comm(input_file_1, input_file_2)
        compare.compareFiles(unsorted_option)
    except IOError as (errno, strerror):
        parser.error("I/O error({0}): {1}".
                     format(errno, strerror))

if __name__ == "__main__":
    main()
