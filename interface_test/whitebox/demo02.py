#!/usr/bin/env python
#-*- coding:utf-8 -*-

class MyList:

    def __init__(self,list):
        self.list = list
    def mySplice(self,index,count):
        for i in range(index,len(self.list)-count):
            self.list[i] = self.list[i+count]
        for i in range(count):
            list.pop()

        return self.list

if __name__ == '__main__':

    list = []
    print(MyList(list).mySplice(0,len(list)))