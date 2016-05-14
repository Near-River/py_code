#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


# sending email with attachments
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendEmailWithAttachments():
    from_addr = input('From Email: ')
    password = input('Password: ')
    to_addr = input('To Email: ')
    smtp_server = input('SMTP Server: ')

    msg = MIMEMultipart()
    msg['Subject'] = Header('Hello, My friends.', charset='utf-8').encode()
    msg['From'] = _format_addr('Nate_River <%s>' % from_addr)
    msg['To'] = _format_addr('Near <%s>' % to_addr)
    html = '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'
    content = MIMEText(html, 'html', 'utf-8')
    msg.attach(content)
    # Add attachments to the Mail
    with open('../io/cat.jpg', 'rb') as f:
        mime = MIMEBase('image', 'jpg', filename='cat.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='cat.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    # Puts the connection to the SMTP server into TLS mode
    # server.starttls()
    server.set_debuglevel(1)    # Print out all the information during the SMTP server interaction process
    server.login(user=from_addr, password=password)
    server.sendmail(from_addr=from_addr, to_addrs=[to_addr], msg=msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendEmailWithAttachments()
