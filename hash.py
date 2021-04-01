import os
import hashlib
import time


prevHashFile = open('lastHash.txt', 'r')
lastHash = prevHashFile.read()
if (lastHash) != "":
    hashFile = open('currentHash.txt', 'w')
    newRun = False
else:
    print('No previous hash file found, generating baseline.')
    prevHashFile.close()
    hashFile = open('lastHash.txt', 'w')
    newRun = True

hashList = []

for root, dirs, files in os.walk('.', topdown=True):
    for name in files:
        item = (os.path.join(root, name))
        if './sys' in item or './dev' in item or './proc' in item or './run' in item or './tmp' in item or './var/lib' in item or './var/run' in item:
            continue
        else:
            try:
                File = open(item, 'r').read()
                hashedFile = hashlib.sha256(File.encode('utf-8')).hexdigest()
                timeStamp = time.time()
                hashList.append(str(timeStamp) + ':' + item + ':' + str(hashedFile))
            except:
                continue
    for name in dirs:
        item = (os.path.join(root, name))
        if './sys' in item or './dev' in item or './proc' in item or './run' in item or './tmp' in item or './var/lib' in item or './var/run' in item:
            continue
        else:
            try:
                File = open(item, 'r').read()
                hashedFile = hashlib.sha256(File.encode('utf-8')).hexdigest()
                timeStamp = time.time()
                hashList.append(str(timeStamp) + ':' + item + ':' + str(hashedFile))
            except:
                continue
for item in hashList:
    hashFile.write(item)
    hashFile.write('\n')
if newRun:
    print("Baseline established, program will now compare future runs with this.")
    hashFile.close()
else:
    oldHashList = lastHash.split('\n')
    fileDict = {}
    for i in oldHashList[0:-1]:
        fileDict[i.split(':')[1]] = i.split(':')[2]
    newFileDict = {}
    for j in hashList[0:-1]:
        newFileDict[j.split(':')[1]] = j.split(':')[2]
    for key in newFileDict:
        if key not in fileDict:
            print('New File ' + str(key) + ' found.')
            continue
        elif newFileDict[key] != fileDict[key]:
            print('File ' + str(key) + ' modified.')
            continue
        else:
            continue
    prevHashFile.close()
    prevHashFile = open('lastHash.txt', 'w')
    for item in hashList:
        prevHashFile.write(item)
        prevHashFile.write('\n')
    hashFile.close()
    prevHashFile.close()
            
