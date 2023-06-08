import requests


def keyword(message, uid, gid=None):
    if gid is None:  # 判断是否传入gid，区别群聊和私聊
        if uid == :  #  QQ号
            if message == '我爱你':
                requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id=%s&message=%s' % (uid, '我也爱你'))
            elif message == '你是谁':
                requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id=%s&message=%s' % (uid, '我是QQ机器人'))
                # 私聊回复requests网址，参数自行修改

    elif gid == :  # 群号，你想要自动回复的群
        if uid == :  # 谁发的消息要回复
            if '我爱你' in message:
                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=%s' % (
                    gid, '[CQ:at,qq=%s]我也爱你' % uid))
                # 群聊回复requests网址，参数自行修改

