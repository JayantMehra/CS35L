#! /bin/sh

#----------------------------------------
#  sameln.sh
#  CS35L/Week2
#
#  Created by Jayant Mehra on 1/22/18
#
#----------------------------------------

#So that file with spaces are not treated as separate files
IFS=$'\n'

#Stores hidden files
DotFiles=$(ls -a $1 -p | grep -v / | grep ^[\.] | sort -u)

#Stores non-hidden files
NotDotFiles=$(ls $1 -p | grep -v / |  sort -u)

#Concatenates dot and notdot files such that dot files are at the top
hold=$DotFiles$'\n'$NotDotFiles

for l in $hold; do

    #Makes sure the file is not a symbolic link
    test -L "$1/$l"
    if [ $? -eq 0 ]; then
        continue
    else
        for k in $hold; do
            #Makes sure the file is not a symbolic link
            test -L "$1/$k"
            if [ $? -eq 0 ]; then
                continue

            #Makes sure both the files are not the same
            elif [ "$l" == "$k" ]; then
                continue

            #Makes sure the files are not hardlinked already
            elif [ "$1/$l" -ef "$1/$k" ]; then
                continue
            else
                #Compares the files
                cmp -s "$1/$l" "$1/$k"
                if [ $? -eq 0 ]; then
                    #Stores the name of the file2
                    name="$1/$k"

                    #Removes file2
                    rm "$1/$k"

                    #Makes a hardlink to the firstfile and names it 'name'
                    ln "$1/$l" $name
                fi
            fi
         done
    fi
done
