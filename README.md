# Computing_JPEG_Hashes 

This script computes the SHA256 hash of JPEG image files after it verifies that a file is a JPEG by scanning its header and not relying on its extension. 

## Description

This script will traverse a directory and its subdirectories and examine the files within them looking for .JPEG files. This will be done by examining each file's header and not by scanning the extension. Once .JPEG files are found, the script will compute the SHA256 hash of the file, get the files' MAC times, and store them in output.txt. This script is useful in finding .JPEG's based on their file headers, in case original file extensions have been tampered.

## Getting Started

### Dependencies

pip install hashlib

### Executing program

Run from terminal then choose the target directory. The target directory and its subdirectories will be traversed. 

## Modifications 
You can edit the script to compute a different hash other than SHA256. 

You can edit the script to look for a different type of file other than JPEG by inputting a different first four bytes value. 