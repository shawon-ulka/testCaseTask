from gettext import find
from sortData import sortData
from utils import specialityCheck
from utils import infoForArgumentDeclartion
import re
with open("test5.sv") as f:
    lines=f.readlines()
f.close()

impData=[]
for eachLine in lines:
    if eachLine.startswith("module"):
        brac_splited=eachLine.split("(")[1]
        splited=re.split('[,;]+', brac_splited)
        for elem in splited:
            elem=elem.strip()
            elem=elem.replace(")","")
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

sorted=sortData(impData)