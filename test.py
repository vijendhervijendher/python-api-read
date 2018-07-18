import requests
import sys
first = sys.argv[1]
second = sys.argv[2]
r = requests.get('https://s3.amazonaws.com/challenge.getcrossbeam.com/public/' + first + '.json')
s = requests.get('https://s3.amazonaws.com/challenge.getcrossbeam.com/public/' + second + '.json')
fCount = 0
sCount = 0
iCount = 0
fSet = set()
sSet = set()
firstList = r.json()['companies']
secondList = s.json()['companies']
for elem in firstList:
    if not elem['domain'] in fSet:
        fSet.add(elem['domain'])
        fCount += 1
for elem in secondList:
    if not elem['domain'] in sSet:
        sSet.add(elem['domain'])
        sCount += 1
        if elem['domain'] in fSet:
            iCount += 1



print(fCount)
print(sCount)
print(iCount)



