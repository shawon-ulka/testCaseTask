with open("test2.sv") as f:
    lines=f.readlines()
f.close()

for eachLine in lines:
    stripedLine=eachLine.strip()
    if stripedLine.startswith("module"):
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

