
# coding: utf-8

import io  
import sys
import time
import random
import itchat
from itchat.content import *
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')




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
