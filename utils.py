import json
import re
def bitAddressSize(bitAddress):
    size=1
    for index,address in enumerate(bitAddress):
        if index==1:
            size+=int(address)
    return size
    
def specialityCheck(line):
    speciality={
        "onlyParams":True,
        "singleLined":False
    }
    stripedLine=line
    posOfOpenParen=stripedLine.find("(")
    posOfCloseParen=stripedLine.find(")")
    if posOfCloseParen==-1:
        stripedLine=stripedLine[posOfOpenParen+1:]
    else:
        stripedLine=stripedLine[posOfOpenParen+1:posOfCloseParen]
    commaSplited=stripedLine.split(",")
    for elem in commaSplited:
        if len(elem.split())>1:
            speciality["onlyParams"]=False
            break
    if not speciality["onlyParams"] and posOfCloseParen!=-1:
        speciality["singleLined"]=True
    return speciality

def infoSort(splitedLine):
    direction=["inout","input","output"]
    if len(splitedLine) and splitedLine[0] in direction:
        port_dict={}
        port_dict["direction"]=splitedLine[0]
        port_dict["size"]=1
        if len(splitedLine)>=4:
            port_dict["type"]=splitedLine[1]
            if splitedLine[2].startswith("[") and splitedLine[2].endswith("]"):
                size=bitAddressSize(splitedLine[2])
                port_dict["size"]=size
            name=splitedLine[3].replace(';','')
            port_dict["name"]=name
        elif len(splitedLine)==2:
            port_dict["type"]="wire"
            name=splitedLine[1].replace(';','')
            port_dict["name"]=name
        elif len(splitedLine)==3:
            if splitedLine[1].startswith("[") and splitedLine[1].endswith("]"):
                port_dict["type"]="wire"
                size=bitAddressSize(splitedLine[1])
                port_dict["size"]=size
            else:
                port_dict["type"]=splitedLine[1]
            name=splitedLine[2].replace(';','')
            port_dict["name"]=name
        
        return port_dict
    else:
        return None

def infoForArgumentDeclartion(lines):
    lines=lines
    info={
        "module name":"",
        "timescale":""
    }
    allPortInfo={}
    for line in lines:
        modifiedLine=line.strip()
        if modifiedLine.startswith("module"):
            splitedLine=modifiedLine.split()
            moduleName=splitedLine[1].split("(")[0]
            info["module name"]=moduleName
            continue
        if modifiedLine.startswith("`timescale"):
            splitedLine=modifiedLine.split()
            info["timescale"]=splitedLine[1]
            continue
        splitedLine=modifiedLine.split()
        port_dict=infoSort(splitedLine)
        if port_dict is not None:
            nameSeperation=port_dict["name"].split(',')
            for name in nameSeperation:
                portDetails={"direction":port_dict["direction"],"type":port_dict["type"],"size":port_dict["size"]}
                allPortInfo[name]=portDetails

    info["allPortInfo"]=allPortInfo


    portData=json.dumps(info, indent=4)
    with open ("portData","w") as f:
        f.write(portData)
    return(info)