from utils import specialityCheck
from utils import infoForArgumentDeclartion
with open("test5.sv") as f:
    lines=f.readlines()
f.close()

direction=["inout","input","output"]
impData=[]
for eachLine in lines:
    if eachLine.startswith("module"):
        brac_splited=eachLine.split("(")[1]
        commaSplited=brac_splited.split(",")
        for elem in commaSplited:
            impData.append(elem)
        continue
    commaSplited=eachLine.split(",")
    print(commaSplited)
    for elem in commaSplited:
        print(elem)
        semiSplited=eachLine.split(";")
        print(semiSplited)


# for eachLine in lines:
#     stripedLine=eachLine.strip()
#     if stripedLine.startswith("module"):
#         speciality=specialityCheck(stripedLine)
#         break

# if speciality["onlyParams"]:
#     info=infoForArgumentDeclartion(lines)
# if not speciality["singleLined"]:
#     print("hello ")