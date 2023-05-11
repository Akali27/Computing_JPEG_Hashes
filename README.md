# JPEG File Analyzer

This Python script traverses a specified directory and its subdirectories, identifies JPEG files, and generates a report containing each file's name, SHA-256 hash, and last modified, accessed, and created times.

## Features

- Traverses a user-specified directory and its subdirectories.
- Identifies JPEG files by comparing the first four bytes of each file to the JPEG header bytes \xff\xd8\xff\xe0.
- Computes the SHA-256 hash of each JPEG file.
- Retrieves the last modified, accessed, and created times of each JPEG file.
- Generates a CSV report containing the file information.

## Requirements

Python 3.x

pip install hashlib

### Executing program

Run from terminal then choose the target directory. The target directory and its subdirectories will be traversed. 

## Modifications 

You can edit the script to compute a different hash other than SHA256. 

You can edit the script to look for a different type of file other than JPEG by inputting a different first four bytes value. 
