import os
import shutil
import copy

masterDrive = "C:\\"
masterPath = os.path.join(masterDrive, "Users", "sumad", "Downloads", "AllAmyloidProcessed")

outDrive = "C:\\"
outPath = os.path.join(outDrive, "Users", "sumad", "OneDrive - San José Unified School District", "Documents", "AMYLOID DATASET COMPLETE ALL", "AllAmyloidProcessedSeperated")

y = []
for root, dirs, files in os.walk(masterPath):
    for x in dirs:
        if x[0] == 'I':
            y.append(root + '\\' + x)

imageDirs = {}
imageNames = {}
for path in y:
    print(path)
    c = True
    for root, dirs, files in os.walk(path):
        if not c:
            break
        else:
            imageDirs[path] = []
            found = False
            superior = ""
            print(path)
            if path[45:55] in imageNames:
                antecedent = 222
                while path[45:55] + str(antecedent) in imageNames:
                    antecedent += 111
                superior = path[45:55] + str(antecedent)
                imageNames[superior] = []
            else:
                superior = path[45:55]
                imageNames[superior] = []
            for image in files:
                if image[97:99] == '48' or image[97:99] == '60' or image[97:99] == '36':
                    imageDirs[path].append(root + '\\' + image)
                    imageNames[superior].append(image[97:99])
            c = False

IDs = []
for ID in imageNames:
    key = ID[6:]
    if key[0:2] == '00':
        x = key[2:]
    elif key[0] == '0':
        x = key[1:]
    else:
        x = copy.deepcopy(key)
    IDs.append(x)

dirs = []
for dir_ in imageDirs:
    dirs.append(dir_)

os.chdir(outPath)

for ID in IDs:
    os.makedirs(ID)
    index = IDs.index(ID)
    full = dirs[index]
    for image in imageDirs[full]:
        shutil.copy(image, outPath + "\\" + ID)