# -*- coding:utf-8 -*-
# developTime: 2025/12/1 16:34
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def test(self,name):
        print("%s在考试"%self.name)
