#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


# Send E-Mail
def _format_addr(s):
    name, addr = parseaddr(s)
    # print(name, addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendPlainText():
    from_addr = input('From Email: ')
    password = input('Password: ')
    to_addr = input('To Email: ')
    smtp_server = input('SMTP Server: ')

    # __init__(self, _text, _subtype='plain', _charset=None)
    msg = MIMEText('Hello, World!', 'plain', 'utf-8')

    # send html email
    # html = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
    # msg = MIMEText(html, 'html', 'utf-8')

    msg['Subject'] = Header('Hello, My friends.', charset='utf-8').encode()
    msg['From'] = _format_addr('Nate_River <%s>' % from_addr)
    msg['To'] = _format_addr('Near <%s>' % to_addr)
    # print(msg)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)    # Print out all the information during the SMTP server interaction process
    server.login(user=from_addr, password=password)
    server.sendmail(from_addr=from_addr, to_addrs=[to_addr], msg=msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendPlainText()
