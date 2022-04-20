from pyrogram import Client
import time
import sys

print(
    """


    Coded by Llattes

    Contact with Telegram : @llattes

"""
)
time.sleep(5)

print(
    """\n\n
 Do you need to add members from your specific group ENTER 1
 Or
 Add with your destination usernames list ENTER 2
"""
)

orginally = int(input("Type number 1 or 2: "))

alf = open("Sessions.txt", "r").read()
alf1 = alf.split()
lena = len(alf1)
threads = int(lena / 4)

app0 = Client(
    "Sessions/" + str(alf1[0]), int(alf1[1]), str(alf1[2]), phone_number=str(alf1[3])
)
app1 = Client(
    "Sessions/" + str(alf1[4]), int(alf1[5]), str(alf1[6]), phone_number=str(alf1[7])
)
app2 = Client(
    "Sessions/" + str(alf1[8]), int(alf1[9]), str(alf1[10]), phone_number=str(alf1[11])
)
app3 = Client(
    "Sessions/" + str(alf1[12]),
    int(alf1[13]),
    str(alf1[14]),
    phone_number=str(alf1[15]),
)
# app4 = Client("Sessions/"+str(alf1[16]),int(alf1[17]),str(alf1[18]),phone_number=str(alf1[19]))
# app5 = Client("Sessions/"+str(alf1[20]),int(alf1[21]),str(alf1[22]),phone_number=str(alf1[23]))
# app6 = Client("Sessions/"+str(alf1[24]),int(alf1[25]),str(alf1[26]),phone_number=str(alf1[27]))
# app7 = Client("Sessions/"+str(alf1[28]),int(alf1[29]),str(alf1[30]),phone_number=str(alf1[31]))
# app8 = Client("Sessions/"+str(alf1[32]),int(alf1[33]),str(alf1[34]),phone_number=str(alf1[35]))
# app9 = Client("Sessions/"+str(alf1[36]),int(alf1[37]),str(alf1[38]),phone_number=str(alf1[39]))
# app10 = Client("Sessions/"+str(alf1[40]),int(alf1[41]),str(alf1[42]),phone_number=str(alf1[43]))
# app11 = Client("Sessions/"+str(alf1[44]),int(alf1[45]),str(alf1[46]),phone_number=str(alf1[47]))
# app12 = Client("Sessions/"+str(alf1[48]),int(alf1[49]),str(alf1[50]),phone_number=str(alf1[51]))
# app13 = Client("Sessions/"+str(alf1[52]),int(alf1[53]),str(alf1[54]),phone_number=str(alf1[55]))
# app14 = Client("Sessions/"+str(alf1[56]),int(alf1[57]),str(alf1[58]),phone_number=str(alf1[59]))
# app15 = Client("Sessions/"+str(alf1[60]),int(alf1[61]),str(alf1[62]),phone_number=str(alf1[63]))
# app16 = Client("Sessions/"+str(alf1[64]),int(alf1[65]),str(alf1[66]),phone_number=str(alf1[67]))
# app17 = Client("Sessions/"+str(alf1[68]),int(alf1[69]),str(alf1[70]),phone_number=str(alf1[71]))
# app18 = Client("Sessions/"+str(alf1[72]),int(alf1[73]),str(alf1[74]),phone_number=str(alf1[75]))
# app19 = Client("Sessions/"+str(alf1[76]),int(alf1[77]),str(alf1[78]),phone_number=str(alf1[79]))
# app20 = Client("Sessions/"+str(alf1[80]),int(alf1[81]),str(alf1[82]),phone_number=str(alf1[83]))
# app21 = Client("Sessions/"+str(alf1[84]),int(alf1[85]),str(alf1[86]),phone_number=str(alf1[87]))
# app22 = Client("Sessions/"+str(alf1[88]),int(alf1[89]),str(alf1[90]),phone_number=str(alf1[91]))
# app23 = Client("Sessions/"+str(alf1[92]),int(alf1[93]),str(alf1[94]),phone_number=str(alf1[95]))
# app24 = Client("Sessions/"+str(alf1[96]),int(alf1[97]),str(alf1[98]),phone_number=str(alf1[99]))
# app25 = Client("Sessions/"+str(alf1[100]),int(alf1[101]),str(alf1[102]),phone_number=str(alf1[103]))
# app26 = Client("Sessions/"+str(alf1[104]),int(alf1[105]),str(alf1[106]),phone_number=str(alf1[107]))
# app27 = Client("Sessions/"+str(alf1[108]),int(alf1[109]),str(alf1[110]),phone_number=str(alf1[111]))
# app28 = Client("Sessions/"+str(alf1[112]),int(alf1[113]),str(alf1[114]),phone_number=str(alf1[115]))
# app29 = Client("Sessions/"+str(alf1[116]),int(alf1[117]),str(alf1[118]),phone_number=str(alf1[119]))
# app30 = Client("Sessions/"+str(alf1[120]),int(alf1[121]),str(alf1[122]),phone_number=str(alf1[123]))
# app31 = Client("Sessions/"+str(alf1[124]),int(alf1[125]),str(alf1[126]),phone_number=str(alf1[127]))
# app32 = Client("Sessions/"+str(alf1[128]),int(alf1[129]),str(alf1[130]),phone_number=str(alf1[131]))


apps = [app0, app1, app2, app3]

for app in apps:
    app.start()
aaaaaa = len(apps)


class GroupToGroup_AddMember:
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1, Link2):
        global a, b
        self.Group_ChatID = app0.get_chat(Link1)
        a = self.Group_ChatID.id
        self.Group_ChatID = app0.get_chat(Link2)
        b = self.Group_ChatID.id

    def Add_To_Group(self, Source, Destination):
        members = app0.iter_chat_members(Source)
        counter = 1
        ccc = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            try:
                user_id = member.user.username
                app.add_chat_members(Destination, user_id)
            except:
                pass
            else:
                print("Added " + str(counter) + " " + str(user_id) + "\t" + str(ccc))
                counter = counter + 1
            if ccc == aaaaaa:
                ccc = 1


class GroupToGroup_AddMember1:
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
        global a
        self.Group_ChatID = app0.get_chat(Link1)
        a = self.Group_ChatID.id

    def Add_To_Group(self, Destination):
        counter = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            ccc = 1
            try:
                app.add_chat_members(Destination, member)
            except:
                pass
            else:
                print("Added " + str(counter) + " " + str(member) + "\t" + str(ccc))
                counter = counter + 1
            if ccc == aaaaaa:
                ccc = 1


if int(orginally) == 1:
    one = input("Source group: ")
    two = input("Destination group: ")

    if "@" in str(one):
        onee = one.replace("@", "")
    else:
        onee = one
    if "@" in str(two):
        twoo = two.replace("@", "")
    else:
        twoo = two
    try:
        for app in apps:
            app.join_chat(str(onee))
            app.join_chat(str(twoo))
    except:
        pass

    App_Start = GroupToGroup_AddMember()
    ab = App_Start.Get_group_chat_id(one, two)
    App_Start.Add_To_Group(a, b)

elif int(orginally) == 2:
    one = input("Destination group: ")
    members1 = str(input("Enter your file of members: "))

    if "@" in str(one):
        onee = one.replace("@", "")
    else:
        onee = one
    try:
        for app in apps:
            app.join_chat(str(onee))
    except:
        pass

    members = open(members1, "r").read()
    members = members.split()
    App_Start = GroupToGroup_AddMember1()
    ab = App_Start.Get_group_chat_id(one)
    App_Start.Add_To_Group(a)
else:
    for app in apps:
        app.stop()
    sys.exit("Enter 1 or 2")

print(
    """


    Coded by Llattes

    Contact with Telegram : @llattes

    Happy Hacking ;))))

"""
)

time.sleep(5)
for app in apps:
    app.stop()
sys.exit()
