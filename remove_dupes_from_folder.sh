#!/bin/bash
# rmove files in folder not on list
# run the diff command to create a edit a list of unique files you want to save
# cd to directory you want to clean up.
cd ../IG-Sampler/pages/_includes
# Exit if the directory isn't found.
# if (($?>0)); then
#    echo "Can't find work dir... exiting"
#    exit
# fi

for i in *; do
    if ! grep -qxFe "$i" ../../../duplicate.txt; then
        echo "Deleting: $i"
        # the next line is commented out.  Test it.  Then uncomment to removed the files
        # rm "$i"
    fi
done
