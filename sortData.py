def bitAddressSize(bitAddress):
    #need to fix the bug.
    size=1
    for index,address in enumerate(bitAddress):
        if index==1:
            size+=int(address)
    return size

def infoSort(splitedLine):

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


def sortData(impData):
    direction=["inout","input","output"]
    net_type=["wire","reg","logic"]
    info=[]
    allPortInfo={}
    for index,data in enumerate(impData):
        splitted=data.split()
        if len(splitted)==1:
            port_dict={}
            name=splitted[0]
            for back in range(1,10):
                if len(info)==0:
                    break
                prev_data=impData[index-back]
                if prev_data.split()[0] not in direction:
                    continue
            # if len(info) and impData[index-1].split()[0] in direction:
                lastInserted=info[-1]
                port_dict["direction"]=lastInserted["direction"]
                port_dict["size"]=lastInserted["size"]
                port_dict["type"]=lastInserted["type"]
                port_dict["name"]=name
                info.append(port_dict)
                allPortInfo[port_dict["name"]]={"direction":port_dict["direction"],"type":port_dict["type"],"size":port_dict["size"]}
                break

            for back in range(1,10):
                if len(info)==0:
                    break
                prev_data=impData[index-back]
                if prev_data.split()[0] in direction:
                    break
                elif prev_data.split()[0] in net_type:
                    prev_data=prev_data.split()
                    if len(prev_data)==2:
                        updated_type=prev_data[0]
                        allPortInfo[name]["type"]=updated_type
                        break
                    if len(prev_data)==3:
                        updated_type=prev_data[0]
                        updated_size=bitAddressSize(prev_data[1])
                        allPortInfo[name]["type"]=updated_type
                        allPortInfo[name]["size"]=updated_size
                        break
        if len(splitted)>1 and splitted[0] in direction:
            sorted=infoSort(splitted)
            name=sorted["name"]
            details={"direction":sorted["direction"],"type":sorted["type"],"size":sorted["size"]}
            allPortInfo[name]=details
            info.append(sorted)
        if len(splitted)>1 and splitted[0] in net_type:
            if len(splitted)==2:
                name=splitted[1]
                updated_type=splitted[0]
                allPortInfo[name]["type"]=updated_type
            if len(splitted)==3:
                name=splitted[2]
                updated_type=splitted[0]
                updated_size=bitAddressSize(splitted[1])
                allPortInfo[name]["type"]=updated_type
                allPortInfo[name]["size"]=updated_size

    return allPortInfo