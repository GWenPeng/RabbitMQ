#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika
import random
username = 'xpms'  # 指定远程rabbitmq的用户名密码
pwd = 'xpms'
ip_addr = '10.1.249.250'
port_num = 5672
# 新建连接，rabbitmq安装在本地则hostname为'localhost'

credentials = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip_addr, port=port_num, virtual_host='XPMS',credentials=credentials))



# 消息队列服务的连接和队列的创建


# 创建通道
channel = connection.channel()
# 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
channel.queue_declare(queue='XPMS_DEVELOPER_MEMBER',passive=True)
body = '{"CrsResvNo":"2011018190829150321007006X02SS5O","ResNo":"2011018190829150321007006X02SS5O","MemberId":"031106173","MemberLevel":"I","Date":"2019/8/29 15:03:37","HotelId":"2011018"}'
for i in range(1,100):
    # 交换机; 队列名,写明将消息发往哪个队列; 消息内容
    # routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列
    channel.basic_publish(exchange='', routing_key='XPMS_DEVELOPER_MEMBER', body=body)

print ("%s" % body)
connection.close()