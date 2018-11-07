#! /bin/bash

commands=`ls /usr/bin | awk 'NR%101==504992428%101'`    # All commands to investigate

for command in $commands; do
    echo $command:

    ldd /usr/bin/$command | sort -u

    # To print empty new lines
    echo "-------"
    echo ""
done
