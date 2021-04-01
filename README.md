# Hashing Host Integrity Checker

This program will, when run, check hashes of file contents on OS against previously saved hashes. It will alert the user of any new or changed files.

## Usage

To run the code, you will first need to create an empty file called lastHash.txt. This file and the program will need to be run from the base directory of the file system. 

```bash
touch lastHash.txt
```
Then, you can run the program as follows.

```bash
python3 hash.py
```

## Output

On the first run, messages will appear notifying user that baseline is being established. 
On runs after the initial, the program will output changed or new files and their paths. 

## Dependecies 

To run this code, please ensure python 3 is installed and updated. 
