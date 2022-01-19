with open("test1.sv") as f:
    lines=f.readlines()
f.close()

for eachLine in lines:
    stripedLine=eachLine.strip()
    if stripedLine.startswith("module"):
        print(stripedLine)
        posOfOpenParen=stripedLine.find("(")
        posOfCloseParen=stripedLine.find(")")
        if posOfCloseParen==-1:
            print("not single lined verilog")
            stripedLine=stripedLine[posOfOpenParen+1:]
        else:
            print("single lined verilog")
            stripedLine=stripedLine[posOfOpenParen+1:posOfCloseParen]
        commaSplited=stripedLine.split(",")
        print(commaSplited)
