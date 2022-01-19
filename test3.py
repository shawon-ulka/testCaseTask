with open("test3.sv") as f:
    lines=f.readlines()
f.close()

direction=["inout","input","output"]

for eachLine in lines:
    stripedLine=eachLine.strip()
    if stripedLine.startswith("module"):
        continue
        print(stripedLine)
        posOfOpenParen=stripedLine.find("(")
        posOfCloseParen=stripedLine.find(")")
        if posOfCloseParen==-1:
            stripedLine=stripedLine[posOfOpenParen+1:]
        else:
            stripedLine=stripedLine[posOfOpenParen+1:posOfCloseParen]
        commaSplited=stripedLine.split(",")
        print(commaSplited)
        for elem in commaSplited:
            splited=elem.split()
            print(splited)
            # print(len(splited))
    print(stripedLine)
    splited=stripedLine.split()
    if not len(splited):
        continue
    if len(splited) and splited[0] in direction:
        commaSeparated=stripedLine.split(',')
        if len(commaSeparated)>1:
            print(commaSeparated)
