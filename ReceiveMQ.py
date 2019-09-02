import pika
import sys
import time

# 远程rabbitmq服务的配置信息
username = 'xpms'  # 指定远程rabbitmq的用户名密码
pwd = 'xpms'
ip_addr = '10.1.249.250'
port_num = 5672

credentials = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(ip_addr, port_num, 'XPMS', credentials))
channel = connection.channel()


# 消费成功的回调函数
def callback(ch, method, properties, body):
    print(" [%s] Received %r" % (time.time(), body))
    # time.sleep(0.2)


# 开始依次消费XPMS_DEVELOPER_MEMBER队列中的消息
channel.basic_consume(queue='XPMS_DEVELOPER_MEMBER', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages')
channel.start_consuming()  # 启动消费