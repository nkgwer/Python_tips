import re
pattern = r"PPAP"
text = "PPAAPPAPAPPAPAPPAPPAPAPAPPPAPAPPAPAP"
matchOB = re.search(pattern , text)

if matchOB:
    print(matchOB)
    print(matchOB.group())
    print(matchOB.start())
    print(matchOB.end())
    print(matchOB.span())  