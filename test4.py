from utils import specialityCheck
from utils import infoForArgumentDeclartion
with open("test4.sv") as f:
    lines=f.readlines()
f.close()

direction=["inout","input","output"]

for eachLine in lines:
    stripedLine=eachLine.strip()
    if stripedLine.startswith("module"):
        speciality=specialityCheck(stripedLine)
        break
print(speciality)
if speciality["onlyParams"]:
    info=infoForArgumentDeclartion(lines)
