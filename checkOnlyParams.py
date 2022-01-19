with open("paramTest.sv") as f:
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
        print(stripedLine)
        commaSplited=stripedLine.split(",")
        print(commaSplited)
        onlyParams=True
    
        for elem in commaSplited:
            if len(elem.split())>1:
                onlyParams=False
                break
        singleLined=False
        if not onlyParams and posOfCloseParen!=1:
            singleLined=True
        print("only params:",onlyParams)
        print("single lined:", singleLined)