#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 输入Email地址和口令:
from_addr = 'wuying@etherfast.com'
username = 'wuying'
password = 'asdf:LKJ'
# 输入SMTP服务器地址:
smtp_server = 'smtp.etherfast.com'
# 输入收件人地址:
to_addr = 'wuying@corp.the9.com'

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
print msg
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
print msg
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
print msg
msg['Subject'] = Header(u'来自SMTP的问候...', 'utf-8').encode()
print msg


server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(username, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
