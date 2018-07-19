
# coding: utf-8

import io  
import sys
import time
import random
import itchat
from itchat.content import *
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')




@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO, FRIENDS], isGroupChat=False)
def general_reply(msg): 
    friend_from = itchat.search_friends(userName=msg.fromUserName)
    friend_to = itchat.search_friends(userName=msg.toUserName)
    if friend_from["RemarkName"] == nameAdmin: # 从admin处发来的消息，解析，并转发给指定用户
        return
    else:
        #[TEXT, MAP, CARD, NOTE, SHARING],[PICTURE, RECORDING, ATTACHMENT, VIDEO], FRIENDS        
        # 根据消息类型转发
        if msg['Type'] == TEXT or msg['Type'] == NOTE:
            admin.send(u'%s->%s\n%s: %s\n<<'%(friend_from["NickName"],friend_to["NickName"],friend_from["RemarkName"], msg['Text']))
        elif msg['Type'] == CARD:
            admin.send_raw_msg(msg.msgType, msg.content)
            admin.send(u'%s->%s\n%s<<'%(friend_from["NickName"],friend_to["NickName"],friend_from["RemarkName"]))
            return
        elif msg['Type'] == SHARING or msg['Type'] == MAP:
            admin.send(u'%s->%s\n%s: %s\n%s\n<<'%(friend_from["NickName"],friend_to["NickName"],friend_from["RemarkName"], msg['Text'], msg['Url']))
            return
        elif msg['Type'] == PICTURE or msg['Type'] == RECORDING or msg['Type'] == ATTACHMENT or msg['Type'] == VIDEO:
            # 下载图片等文件
            msg['Text'](msg['FileName'])
            # 转发
            admin.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']))
            admin.send(u'%s->%s\n%s<<'%(friend_from["NickName"],friend_to["NickName"],friend_from["RemarkName"]))
            return
        admin.send_raw_msg(msg.msgType, msg.content)
        admin.send(u'%s->%s\n%s<<'%(friend_from["NickName"],friend_to["NickName"],friend_from["RemarkName"]))
        return




itchat.auto_login(enableCmdQR=2,hotReload=True)    # 部分linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2

# 消息转发给指定用户
nameAdmin = u'江枫'
admin = itchat.search_friends(name=nameAdmin) # RemarkName
if admin:
    admin = admin[0]
else:
    print('No friend name %s' % nameAdmin) 


nameAdminGroup = u'江枫'
adminG = itchat.search_friends(name=nameAdminGroup) # RemarkName
if adminG:
    adminG = adminG[0]
else:
    print('No friend named %s' % nameAdminGroup) 


# chatrooms
#chatrooms_Supervised = itchat.get_chatrooms(update=True)
#chatroom_ids = [c['NickName'] for c in chatrooms_Supervised]
#print('%d chatrooms under surveillance:' % len(chatrooms_Supervised))
#for item in chatrooms_Supervised:
#	print(u'%s' % item['NickName'])
groupSupervised=u'愁眠'
chatrooms_Supervised = itchat.search_chatrooms(name=groupSupervised)
chatroom_ids = [c['NickName'] for c in chatrooms_Supervised]
if chatrooms_Supervised:
    chatrooms_Supervised = chatrooms_Supervised[0]
else:
    print('No chatroom named %s' % chatrooms_Supervised)



# send renew info
en_sended_renew = []
        
itchat.run()
