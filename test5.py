from gettext import find
from utils import specialityCheck
from utils import infoForArgumentDeclartion
import re
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
            if elem=="" or elem=="\n":
                continue
            impData.append(elem)
        continue
    if eachLine.startswith("endmodule"):
        continue
    eachLine=eachLine.strip()
    if eachLine=="" or eachLine=="\n":
        continue
    splitted=re.split('[,;]+', eachLine)
    for elem in splitted:
        elem=elem.strip()
        elem=elem.replace(")","")
        if elem=="" or elem=="\n":
            continue
        impData.append(elem)
