import csv
import os
import copy

def find_unique_id(inCsv):
    file1 = open(inCsv,'r')
    content1 = csv.reader(file1)

    l1 = []
    first = True
    for row in content1:
        if row[0] not in l1 and not first:
            l1.append(row[0])

        first = False

    file1.close()

    return l1

def create_dict(inCsv, inlist):
    file1 = open(inCsv,'r')
    content1 = csv.reader(file1)
    
    first = True
    dict = {}
    for element in inlist:
        dict[element] = 0

    for row in content1:
        if not first:
            dict[row[0]]+=1
        
        if first:
            first = False
    
    file1.close()

    return dict

def create_finallist(IDdict, SUVRdict):
    l1 = []
    count = 0
    for key in IDdict:
        if key[6:8] == '00':
            SUVRkey = key[8:]
        elif key[6] == '0':
            SUVRkey = key[7:]
        else:
            SUVRkey = key[6:]
        try:
            if IDdict[key] == SUVRdict[SUVRkey]:
                l1.append(key)
        except:

            count +=1
    
    return l1, count

def find_SUVRs(inCsv, inlist):
    file1 = open(inCsv,'r')
    content1 = csv.reader(file1)

    convertedlist = convert_fulllist(inlist)
    dict = {}
    for row in content1:
        key = copy.deepcopy(row[0])
        if key in convertedlist and key not in dict:
            dict[key] = row[16]
        elif key in convertedlist:
            antecedent = 222
            while (key + str(antecedent)) in dict:
                antecedent += 111
            dict[(key + str(antecedent))] = row[16]
    
    lol = []
    for pointer in dict:
        lol.append([pointer, dict[pointer]])

    return lol

def convert_fulllist(inlist):
    l1 = []
    for key in inlist:
        if key[6:8] == '00':
            SUVRkey = key[8:]
        elif key[6] == '0':
            SUVRkey = key[7:]
        else:
            SUVRkey = key[6:]
        l1.append(SUVRkey)
    
    return l1

def extract_clinicals(inCsv):
    file1 = open(inCsv,'r')
    content1 = csv.reader(file1)
    
    lol = []
    ID = []
    for row in content1:
        key = row[0]
        newkey = copy.deepcopy(key[6:])
        if row[1] == 'M':
                Gender = 1
        else:
                Gender = 0
        if newkey in ID:
            antecedent = 222
            while (newkey + str(antecedent)) in ID:
                antecedent += 111
            newkey += str(antecedent)
            x = [newkey, Gender, row[2], row[3], row[4], row[5], row[6], row[7]]
            ID.append(newkey)
            lol.append(x)
        else:
            x = [newkey, Gender, row[2], row[3], row[4], row[5], row[6], row[7]]
            ID.append(newkey)
            lol.append(x)

    return lol

IDpath = "...\\idaSearch_8_03_2022.csv"

SUVRpath = "...\\UCBERKELEYAV45_04_26_22 - UCBERKELEYAV45_04_26_22.csv"

SUVRoutpath = "...\\AllAmyloidTarget.csv"

IDoutpath = "...\\AllAmyloidIDs.csv"


IDlist = find_unique_id(IDpath)
SUVRlist = find_unique_id(SUVRpath)

IDdict = create_dict(IDpath, IDlist)
SUVRdict = create_dict(SUVRpath, SUVRlist)

finallist, notcommoncount = create_finallist(IDdict, SUVRdict)

finalSUVRlol = find_SUVRs(SUVRpath, finallist)
print(len(finalSUVRlol))

outFile = open(SUVRoutpath,'w',newline="")
with outFile:
    write = csv.writer(outFile)
    write.writerows(finalSUVRlol)

outFile.close()

finalIDlol = []
for element in finallist:
    finalIDlol.append([element + ','])

outFile2 = open(IDoutpath,'w',newline="")
with outFile2:
    write = csv.writer(outFile2)
    write.writerows(finalIDlol)

outFile2.close()


clinicalpath = "...\\idaSearch_8_11_2022.csv"
clinicaloutpath = "...\\AllAmyloidClinicals.csv"

clinicallol = extract_clinicals(clinicalpath)

outFile3 = open(clinicaloutpath,'w',newline="")
with outFile3:
    write = csv.writer(outFile3)
    write.writerows(clinicallol)

outFile3.close()
