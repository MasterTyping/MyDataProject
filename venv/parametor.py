global info
global serverId
global ItemInfo
global ItemS
global ItemImageData
global ItemImageURL
global Main
global SwitchWindow
global SWITCHLV


ItemImageData = list()
ItemImageURL = list()
ItemInfo = list()
ItemS = list()
SWITCHLV = 0

def GetServerId(str):
    serverId = str
    if (serverId == "카인"):
        serverId = "cain"
    elif (serverId == "카시야스"):
        serverId = "casillas"
    elif (serverId == "안톤"):
        serverId = "anton"
    elif (serverId == "바칼"):
        serverId = "bakal"
    elif (serverId == "디레지에"):
        serverId = "diregie"
    elif (serverId == "힐더"):
        serverId = "hilder"
    elif (serverId == "프레이"):
        serverId = "prey"
    elif (serverId == "시로코"):
        serverId = "siroco"
    print(serverId)
    return serverId

global skill

