#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Nate River'

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack(): 把Widget加入到父容器中
        self.pack()
        self.nameEntry = Entry(self)
        # self.exitButton = Button(self, text='Exit', command=self.quit)
        self.triggerButton = Button(self, text='Click', command=self.sayHello)

        self.createWidgets()

    def createWidgets(self):
        self.nameEntry.pack()
        self.triggerButton.pack()

    def sayHello(self):
        name = self.nameEntry.get() or 'anonymous'
        messagebox.showinfo(title='Message', message='hello, %s' % name)


if __name__ == '__main__':
    app = Application()
    # 设置窗口标题
    app.master.title = 'App'
    # 主消息循环
    app.mainloop()
