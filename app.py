import os
import hashlib
import time

# Compute SHA256 hash of the file
def sha256HashFunc(content):
    return hashlib.sha256(content).hexdigest()

if __name__ == '__main__':
    # Ask the user for directory to be traversed
    print('Please define the directory to be traversed:')
    directory = input()

    # Status message
    print('I will traverse: ' + directory + ' and its subdirectories')

    # All jpeg files will be stored here
    jpeg_files = dict()

    # Traverse the subdirectory 
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            fullFilePath = os.path.join(dirpath, file)
            try:
                with open(fullFilePath, 'rb') as f:
                    # Read all the content of the file
                    content = f.read()
                    # Compare the first four bytes with ffd8ffe0
                    if(content[:4] == b'\xff\xd8\xff\xe0'):
                        # Append to the dictionary, name of file, sha256 hash, last modified time
                        # Last access time and creation time, use full file path as key
                        jpeg_files[fullFilePath] = [file, sha256HashFunc(content),
                                           time.ctime(os.path.getmtime(fullFilePath)),
                                           time.ctime(os.path.getatime(fullFilePath)),
                                           time.ctime(os.path.getctime(fullFilePath))]
            except:
                print ("File", fullFilePath, "can not be read, ignoring it")

if len(jpeg_files) == 0:
    print ("No JPEG files found")
else:
    try:
        # Dump all the information in comma separated format
        # With each line representing one jpeg file
        with open("output.txt", 'w') as f:
            # Traverse each element of list
            for jpeg_file in jpeg_files:
                fileData = jpeg_files[jpeg_file]
                # Traverse all but last data of jpeg_file
                for i in range(len(fileData) - 1):
                    f.write('%s,' % fileData[i])
                # Print the last data point in jpeg_file
                f.write(fileData[-1])
                f.write('\n')
    except:
        print ("File writing failed")

print ("The script was completed at", time.ctime())
