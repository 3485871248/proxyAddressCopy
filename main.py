import json
import imaplib
import email
from os import system
from os.path import isfile
from time import sleep
from email.header import decode_header

SLOGAN = ['欢迎使用PAC(代理地址自动复制)程序 我们将辅助您的使用体验', '广告: s-y.lol 低价NFA 1+ 0.6/张', 'made by: shuye#1337/n']

print(r"""██████╗  █████╗  ██████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██║     
██╔═══╝ ██╔══██║██║     
██║     ██║  ██║╚██████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝
""")

for i in SLOGAN:
    print('[欢迎]' + i)

configs = {
    'imap_server': 'imap.qq.com',
    'account': 'QQmail_account',
    'password': 'QQmail_authorization_code',
    'route': 'proxy_route_serial_number (number!!)'
}

# 配置读取/创建
if isfile('config.json'):
    configFile = open('config.json', 'r')
    try:
        configs = json.load(configFile)
    except json.JSONDecodeError:
        input("[错误]配置文件解析错误 请检查配置文件或删除它")
        exit(1)
    configFile.close()
    print("[日志]配置文件解析成功")
else:
    configFile = open('config.json', 'w')
    json.dump(configs, configFile)
    configFile.close()
    input("[提示]未检测到配置文件 已生成模板 请关闭程序并填写配置")
    exit(0)

try:  # 连接到IMAP服务器 并登录账号
    mail = imaplib.IMAP4_SSL(configs['imap_server'])
    mail.login(configs['account'], configs['password'])
except imaplib.IMAP4.IMAP4Exception:
    input("[错误]连接到IMAP服务器失败 请检测网络或配置")
    exit(1)
# 选择一个邮件文件夹，默认为inbox
mail.select('inbox')

system('title PAC-持续运行中-开源程序请勿滥用')


def get_mail():
    # 搜索未读邮件
    status, data = mail.search(None, 'UNSEEN')
    if status != 'OK':
        input("[错误]搜索未读邮件失败 检查你的账号/授权码与你的网络")
        mail.logout()
        return error

    # 获取未读邮件ID列表
    mail_ids = data[0].decode()  # 将二进制数据解码为字符串
    id_list = mail_ids.split()

    # 如果没有未读邮件 返回0代表未获取到需要的邮件
    if not id_list:
        return '0'

    latest_unseen_email_id = int(id_list[-1])  # 获取最新的未读邮件ID
    status, data = mail.fetch(str(latest_unseen_email_id), '(RFC822)')  # 获取邮件数据
    if status != 'OK':
        input("[错误]获取邮件数据失败 检查你的网络")
        mail.logout()
        return error

    # 解析邮件数据
    msg = email.message_from_bytes(data[0][1])

    # 检查邮件主题
    subject = decode_header(msg['subject'])[0][0]
    if isinstance(subject, bytes):
        subject = subject.decode()

    # 检查邮件是否未读且标题是否为 "QiuProxy NG"
    if subject == 'QiuProxy NG':
        # 将邮件标记为已读
        mail.store(str(latest_unseen_email_id), '+FLAGS', '\\Seen')
        print("[日志]已找到您的proxy邮件 邮件已标记为已读")
        # 解析邮件内容
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                return body
    else:
        return '0'


def copy_link(body):  # 解析、复制部分
    lines = body.splitlines()
    if len(lines) <= int(configs['route']) + 5:
        input("[错误]线路选择错误")
        return
    lines = lines[int(configs['route']) + 2]
    lines = lines.split(': ')[1]
    if ' ' in lines:
        lines = lines.split(' ')[0]
    system(f"echo {lines} | clip")
    print("[日志]邮件解析成功 线路地址已复制")


while True:
    mailContent = get_mail()
    if mailContent != '0':
        copy_link(mailContent)
    if mailContent == 'error':
        exit(1)

    sleep(3)
