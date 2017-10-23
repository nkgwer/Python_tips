import re
pattern = r"PPAP"
text = "PPAAPPAPAPPAPAPPAPPAPAPAPPPAPAPPAPPAP"
matchOB = re.search(pattern , text)

if matchOB:
    print(matchOB)
    print(matchOB.group())
    print(matchOB.start())
    print(matchOB.end())
    print(matchOB.span())


pattern = r"yes"
text = "oh, yeah yes! yes! yess!"

matchedList = re.findall(pattern,text)
if matchedList:
    print(matchedList)