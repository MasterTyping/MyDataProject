from Tkcontrol import *
from parametor import *
from myurl import *
from tkinter import *
from tkinter import messagebox

def Getinfo(Main):
    temp = list()
    serverId = GetServerId(Main.TextBox['서버'].get())
    info = GetCharID(serverId, Main.TextBox['닉네임'].get())
    temp.append(serverId)
    temp.append(info['rows'][0]['characterId'])
    return temp
def CalcDamageRate(Main):
    #[최종 스킬계수] x [1 + {힘or지능 x (스탯%)}/250] x [공격력의 합] x [1+ 공격력 % 증가] x [크리티컬 1.5]
    #  x [카운터 1.25] x [1+ {속강-속저+11}/222] x [1- 방어율] x [1+ 증뎀 + 추증뎀] x [1+ 크증뎀 + 크증추뎀] x [1+ 모공] x [스킬 공격력 증가 곱연산] x [1 + 추뎀]
    ADamage = float()
    AddDamage = float()
    SDamage = float()
    CDamage = float()
    DefenceRate = float()
    TotalDamage = 0
    DamageWindow = Toplevel(Main.Window)
    DamageWindow.title("데미지 계산")
    DamageWindow.geometry("170x300+%d+%d"%(Main.w+Main.x,Main.y))
    DamageWindow.configure(bg='black')

    #증가 데미지 수치
    DamageUpLabel = Label(DamageWindow,text="증뎀 : ",bg='black',fg="yellow")
    DamageUpLabel.place(x=10,y=20)
    DamageUp = Entry(DamageWindow,width=10)
    DamageUp.place(x=50,y=20)
    Label(DamageWindow, text="%",bg='black',fg="yellow").place(x=130, y=20)

    #크리티컬 증가 데미지
    CDamageUpLabel = Label(DamageWindow, text="크증 : ",bg='black',fg="yellow")
    CDamageUpLabel.place(x=10, y=60)
    CDamageUp = Entry(DamageWindow,width=10)
    CDamageUp.place(x=50, y=60)
    Label(DamageWindow, text="%",bg='black',fg="yellow").place(x=130, y=60)

    #스킬 공격력 증가
    SDamageUpLabel = Label(DamageWindow, text="스증 : ",bg='black',fg="yellow")
    SDamageUpLabel.place(x=10, y=100)
    SDamageUp = Entry(DamageWindow,width=10)
    SDamageUp.place(x=50, y=100)
    Label(DamageWindow, text="%",bg='black',fg="yellow").place(x=130, y=100)

    #모든 공격력 증가
    ADamageUpLabel = Label(DamageWindow, text="모공 : ",bg='black',fg="yellow")
    ADamageUpLabel.place(x=10, y=140)
    ADamageUp = Entry(DamageWindow,width=10)
    ADamageUp.place(x=50, y=140)
    Label(DamageWindow, text="%",bg='black',fg="yellow").place(x=130, y=140)

    #추가 데미지 증가
    AddDamageUpLabel = Label(DamageWindow, text="추뎀 : ",bg='black',fg="yellow")
    AddDamageUpLabel.place(x=10, y=180)
    AddDamageUp = Entry(DamageWindow, width=10)
    AddDamageUp.place(x=50, y=180)
    Label(DamageWindow, text="%",bg='black',fg="yellow").place(x=130, y=180)

    # 모든 공격력 증가
    DefenceLabel = Label(DamageWindow, text="방어 : ", bg='black', fg="yellow")
    DefenceLabel.place(x=10, y=220)
    Defence = Entry(DamageWindow, width=10)
    Defence.place(x=50, y=220)
    Label(DamageWindow, text="%", bg='black', fg="yellow").place(x=130, y=220)

    charinfo = Getinfo(Main)
    Status = GetCharStatus(charinfo[0], charinfo[1])
    Damage = float()

    def Skillinfo():
        charinfo = Getinfo(Main)
        skillinfo = GetSkillinfo(charinfo[0],charinfo[1])
        skill = dict()
        damagelist = list()
        ADamage = 1 + float(ADamageUp.get()) * 0.01
        AddDamage = 1 + float(AddDamageUp.get()) * 0.01
        SDamage = 1 + float(SDamageUp.get()) * 0.01
        CDamage = 1 + float(CDamageUp.get()) * 0.01
        DefenceRate = float(Defence.get()) * 0.01
        SkillWindow = Toplevel(DamageWindow)
        SkillWindow.geometry("300x750+%d+%d"%(Main.x+Main.w+170,Main.y))
        SkillWindow.configure(bg="black")
        for i in range(len(skillinfo['skill']['style']['active'])):
            skill[skillinfo['skill']['style']['active'][i]['name']]= skillinfo['skill']['style']['active'][i]['requiredLevel']*1200
            damagelist.append(Click(Status,skill))
            Label(SkillWindow,text=skillinfo['skill']['style']['active'][i]['name']+" : "+str(int(damagelist[i]))+"K",bg='black',fg='yellow').place(x=0,y=i*30)
        Label(SkillWindow, text="방어: " + str(DefenceRate)+" "+"증뎀: " + str(ADamage)+" "+"추뎀: " + str(AddDamage)+" "
                                + "스증: " + str(SDamage) +" "+"크증: " + str(SDamage), bg='black', fg='yellow').place(x=0, y=720)
    Total = Button(DamageWindow, text='계산시작', bg='black', fg="yellow")
    Total.place(x=50, y=250)
    Total.configure(command=lambda: Skillinfo())

    def Click(Status,skill):
        ADamage = 1+float(ADamageUp.get())*0.01
        AddDamage = 1+float(AddDamageUp.get())*0.01
        SDamage = 1+float(SDamageUp.get())*0.01
        CDamage = 1+float(CDamageUp.get())*0.01
        DefenceRate= float(Defence.get())*0.01
        temp = list()
        for i in range(len(skill)):
            temp = i
        if (Status['status'][2]['value'] > Status['status'][3]['value']):
            TotalDamage = temp * SDamage * 0.01 * (Status['status'][2]['value'] * 0.004 * Status['status'][6]['value']) * (
                    Status['status'][23]['value'] - 20) * 0.0045 * (1.5 + CDamage) * (1+ADamage) * (1+AddDamage) * (1-DefenceRate)
        if (Status['status'][3]['value'] > Status['status'][2]['value']):
            TotalDamage = temp * SDamage * 0.01 * (Status['status'][3]['value'] * 0.004 * Status['status'][7]['value']) * (
                    Status['status'][23]['value'] - 20) * 0.0045 * (1.5 * CDamage) *(1+ADamage) * (1+AddDamage) * (1-DefenceRate)

        return TotalDamage

def itemImageSet(Main):
    serverId = GetServerId(Main.TextBox['서버'].get())
    info = GetCharID(serverId, Main.TextBox['닉네임'].get())
    Equip = GetCharEquip(serverId,info['rows'][0]['characterId'])

    CharImageData = DownLoadURLImage(GetCharimage(serverId, info['rows'][0]['characterId']))
    Charimg = PhotoImage(data=CharImageData)
    Main.Labels['Character'].configure(image=Charimg)
    Main.Labels['Character'].image = Charimg
    #Set ImgData & Draw
    for i in range(len(Equip['equipment'])):
        ItemImageURL.insert(i,Getitemimage(Equip['equipment'][i]['itemId']))
        ItemImageData.insert(i,DownLoadURLImage(ItemImageURL[i]))
        ItemInfo.insert(i,RequestURL(GetitemInfo(Equip['equipment'][i]['itemId'])))
        tempImg = PhotoImage(data = ItemImageData[i])
        Main.Labels[Equip['equipment'][i]["slotName"]].configure(image = tempImg)
        Main.Labels[Equip['equipment'][i]["slotName"]].image = tempImg
    for i in range(len(Equip['equipment'])):
        Main.Labels[Equip['equipment'][i]["slotName"]+"강화"].configure(text = "+"+str(Equip['equipment'][i]['reinforce']))
        Main.Labels[Equip['equipment'][i]["slotName"]+"강화"].text = "+"+str(Equip['equipment'][i]['reinforce'])


def Switcinginfo(Main):
    serverId = GetServerId(Main.TextBox['서버'].get())
    info = GetCharID(serverId, Main.TextBox['닉네임'].get())
    Equip = GetSwitchinfo(serverId, info['rows'][0]['characterId'])
    SwitchWindow = Toplevel(Main.Window)
    SwitchWindow.geometry("300x360+%d+%d"%(Main.x,Main.y+Main.h+30))
    SwitchWindow.title("스위칭정보")
    SwitchWindow.configure(bg='black')
    #SwitchWindow.iconbitmap("icon.ico")
    switchlabels = list()
    switchtextlabels = list()
    for i in range(len(Equip['skill']['buff']['equipment'])):
        #print(Equip['skill']['buff']['equipment'][i]['itemId'])
        ItemImageURL.insert(i, Getitemimage(Equip['skill']['buff']['equipment'][i]['itemId']))
        ItemImageData.insert(i, DownLoadURLImage(ItemImageURL[i]))
        ItemInfo.insert(i, RequestURL(GetitemInfo(Equip['skill']['buff']['equipment'][i]['itemId'])))
        tempImg = PhotoImage(data=ItemImageData[i])
        switchlabels.append(Label(SwitchWindow,image=tempImg,bg='black'))
        switchtextlabels.append(Label(SwitchWindow,text=Equip['skill']['buff']['equipment'][i]['itemName'],bg='black',fg='yellow'))
        switchlabels[i].configure(image=tempImg)
        switchlabels[i].image = tempImg
        switchlabels[i].place(x=0,y=i*30)
        switchtextlabels[i].place(x=40,y=5+i*30)
    SwitchWindow.mainloop()

def Iteminfo(Main):
    serverId = GetServerId(Main.TextBox['서버'].get())
    info = GetCharID(serverId, Main.TextBox['닉네임'].get())
    Equip = GetCharEquip(serverId, info['rows'][0]['characterId'])
    SubWindow = Toplevel(Main.Window)
    SubWindow.geometry("250x430+%d+%d"%(Main.w,Main.y+30+Main.h))
    SubWindow.configure(bg='black')
    SubWindow.title("아이템 상세 정보")
    #SubWindow.iconbitmap("icon.ico")
    labels = list()
    for i in range(len(Equip['equipment'])):
        labels.append(Label(SubWindow,text=Equip['equipment'][i]['slotName'] + " : " + Equip['equipment'][i]['itemName']+" 강화 : " + str(Equip['equipment'][i]['reinforce']),bg='black'))
        labels[i].configure(fg='yellow')
        labels[i].place(x=0,y=i*32)
    SubWindow.mainloop()


def execute():
    #Set Main Window
    Main = TkController()
    Main.SetWindowTitle("DnfApi")
    Main.SetWindowSize(100,100,400,300)
    #Main.SetIcon('icon.ico')
    Main.AddLabel("서버",20,200)
    Main.AddTextBox("서버",60,200)
    Main.AddLabel("주의사항",250,200)
    Main.AddButton("장비정보",300, 70)
    Main.AddLabel("닉네임",10,240)
    Main.AddTextBox("닉네임",60,240)
    Main.AddButton("정보입력",300,30)
    Main.AddButton("버프장비",300,110)
    Main.AddButton("데미지계산",300,150)
    Main.ConfigureLabelText("닉네임", "닉네임 : ")
    Main.ConfigureLabelText("서버", "서버 : ")
    Main.ConfigureLabelText("주의사항","계산기 사용시 \n 적용하지 않는 부분의 \n 입력값은 0으로 \n채워 넣어 주어야합니다.")
    #Set
    Main.AddImageData("캐릭터",DownLoadURLImage("https://img-api.neople.co.kr/df/servers/cain/characters/"+"893312ac0f02c869cabcaaeafc5062be"+"?zoom=1"))
    Main.AddImageData("기본아이템칸",DownLoadURLImage('https://img-api.neople.co.kr/df/items/9e5af255255135e2493aa286e3c0a7f5'))

    Main.AddLabel("Character",45,-40)
    Main.AddLabel("머리어깨",20,30)
    Main.AddLabel("상의",50,30)
    Main.AddLabel("하의",20,60)
    Main.AddLabel("허리",50,60)
    Main.AddLabel("신발",20,90)
    Main.AddLabel("무기",200,30)
    Main.AddLabel("칭호",230,30)
    Main.AddLabel("팔찌",200,60)
    Main.AddLabel("목걸이",230,60)
    Main.AddLabel("보조장비",200,90)
    Main.AddLabel("반지",230,90)
    Main.AddLabel("마법석",200,120)
    Main.AddLabel("귀걸이",230,120)
    Main.AddLabel("머리어깨강화", 10, 30)
    Main.AddLabel("상의강화", 40, 30)
    Main.AddLabel("하의강화", 10, 60)
    Main.AddLabel("허리강화", 40, 60)
    Main.AddLabel("신발강화", 10, 90)
    Main.AddLabel("무기강화", 190, 30)
    Main.AddLabel("칭호강화", 220, 30)
    Main.AddLabel("팔찌강화", 190, 60)
    Main.AddLabel("목걸이강화", 220, 60)
    Main.AddLabel("보조장비강화", 190, 90)
    Main.AddLabel("반지강화", 220, 90)
    Main.AddLabel("마법석강화", 190, 120)
    Main.AddLabel("귀걸이강화", 220, 120)
    #Main.AddImgLabel("Test",Main.ImageData['Test'],300,0)
    Main.Buttons['장비정보'].configure(command=lambda : Iteminfo(Main))
    Main.Buttons['정보입력'].configure(command=lambda : itemImageSet(Main))
    Main.Buttons['버프장비'].configure(command=lambda : Switcinginfo(Main))
    Main.Buttons['데미지계산'].configure(command=lambda: CalcDamageRate(Main))
    Main.Loop()
