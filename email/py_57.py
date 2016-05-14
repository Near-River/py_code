#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
some terminology:
    MUA：Mail User Agent
    MTA：Mail Transfer Agent
    MDA：Mail Delivery Agent

    sender -> MUA -> MTA -> ... -> MTA -> MDA <- MUA <- receiver
"""
from email.mime.text import MIMEText
import smtplib


def sendPlainText():
    # __init__(self, _text, _subtype='plain', _charset=None)
    msg = MIMEText('Hello, World!', 'plain', 'utf-8')
    from_addr = input('From Email: ')
    password = input('Password: ')
    to_addr = input('To Email: ')
    smtp_server = input('SMTP Server: ')

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)    # Print out all the information during the SMTP server interaction process
    server.login(user=from_addr, password=password)
    server.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendPlainText()
