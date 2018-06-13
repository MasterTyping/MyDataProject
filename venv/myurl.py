import json
import urllib.parse
import sys
import httplib2
import urllib.request
from PIL import Image
import io
import base64
import string
#http function
H = httplib2.Http()
U = urllib.request

def DownLoadURLImage(str):
    image_url = str
    image_byt = U.urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)
    return image_b64
#Get Data from URL
def RequestURL(str):
    a,content=H.request(str,'GET')
    result = json.loads(content.decode('utf-8'))
    return result
#incode utf-8 to url
def Incoding(str):
    str = urllib.parse.quote(str)
    return str
#Set search range Max = 200
def SetLimit(limit):
    temp = '&limit='+str(limit)
    return temp
#Set Matching WordType
def SetWordType(wordtype):
    temp= '&wordType='+str(wordtype)
    return temp
#Get char unique code from url
def GetCharID(server,id):
    temp = RequestURL(GetURL['url']+GetURL['servers']+server+GetURL['char']+id+SetLimit(200)+'&'+GetURL['apikey'])
    completeURL = GetURL['url']+GetURL['servers']+server+GetURL['char']+id+SetLimit(200)+'&'+GetURL['apikey']
    print(completeURL)
    return temp
#Get char Status from url need unique code
def GetCharStatus(server,id):
    temp = RequestURL(GetURL['url'] + GetURL['servers'] + server + '/characters/'+id+GetURL['status'] + GetURL['apikey'])
    completeURL =  GetURL['url'] + GetURL['servers'] + server + '/characters/'+id+GetURL['status'] + GetURL['apikey']
    print(completeURL)
    return temp
#Get char Status from url need unique code
def GetSwitchinfo(server,id):
    temp = RequestURL(GetURL['url'] + GetURL['servers'] + server + '/characters/' + id + '/skill/buff/equip/equipment?' + GetURL['apikey'])
    completeURL = GetURL['url'] + GetURL['servers'] + server + '/characters/' + id + '/skill/buff/equip/equipment?' + GetURL['apikey']
    print(completeURL)
    return temp
def GetCharEquip(server,id):
    temp = RequestURL(GetURL['url'] + GetURL['servers'] + server + '/characters/' + id + GetURL['equip']+GetURL['apikey'])
    completeURL = GetURL['url'] + GetURL['servers'] + server + '/characters/' + id + GetURL['equip']+GetURL['apikey']
    print(completeURL)
    return temp
def GetCharimage(server,id):
    temp = GetURL['img']+GetURL['servers']+server+'/characters/'+id+'?zoom=1'
    print(temp)
    return temp
#Get img from url need unique item code
def Getitemimage(itemid):
    temp=GetURL['img']+'items/'+itemid
    print(temp)
    return temp
#Get Item Infomation from url
def GetitemInfo(itemid):
    temp=GetURL['url']+'items/'+itemid +'?'+GetURL['apikey']
    print(temp)
    return temp
def GetSkillinfo(serverId,charId):
    temp = RequestURL(GetURL['url'] + GetURL['servers'] + serverId + '/characters/' + charId + GetURL['skill'] + GetURL['apikey'])
    completeURL = GetURL['url'] + GetURL['servers'] + serverId + '/characters/' + charId + GetURL['skill'] + GetURL['apikey']
    print(completeURL)
    return temp
#Get Url Definition by Dictionary
GetURL={
        'img':'https://img-api.neople.co.kr/df/',
        'url':'https://api.neople.co.kr/df/',
        'apikey':'apikey=Hm51PVr2RIHKDjrzi8X0RBlSX0TnVluI',
		'servers':'servers/',
        'char':'/characters?characterName='
        ,'job':'jobs?'
        ,'item':'items?itemName='
        ,'itemdetail': 'items/'
        ,'status':'/status?'
        ,'equip':'/equip/equipment?'
        ,'skill':'/skill/style?'
        }


