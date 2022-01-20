def bitAddressSize(bitAddress):
    size=1
    for index,address in enumerate(bitAddress):
        if index==1:
            size+=int(address)
    return size

def infoSort(splitedLine):
    direction=["inout","input","output"]
    if splitedLine[0] in direction:
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
        port_dict={}
        if len(splitedLine)==1:
            port_dict["name"]=splitedLine[0]
        return port_dict

def sortData(impData):
    info=[]
    for data in impData:
        splitted=data.split()
        if len(splitted)==1:
            port_dict={}
            if len(info):
                lastInserted=info[-1]
                port_dict["direction"]=lastInserted["direction"]
                port_dict["size"]=lastInserted["size"]
                port_dict["type"]=lastInserted["type"]
                port_dict["name"]=splitted[0]
                info.append(port_dict)
            continue
        sorted=infoSort(splitted)
        info.append(sorted)
    for elem in info:
        print(elem)