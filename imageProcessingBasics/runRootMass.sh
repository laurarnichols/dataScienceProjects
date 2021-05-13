#!/bin/bash
# Run calculateRootMass.py on all trial*.jpg images

# Remove existing binary images
rm *_binary.jpg

# Execute program on trial images
for f in trial-*.jpg
do
  python3 calculateRootMass.py $f 1.5
done

