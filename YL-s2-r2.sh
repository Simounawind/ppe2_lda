#!/bin/bash

cd Corpus

# Remove newlines from all files in directory
for file in *
do
    tr -d '\n' < "$file" > "$file.tmp"
    echo >> "$file.tmp"
    mv "$file.tmp" "$file"

done
