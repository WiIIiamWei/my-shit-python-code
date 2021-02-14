#!/usr/bin/python
# -*- coding: utf-8 -*-
a=[]
p=""
print("Simple tool for reversing string by William Wei")
txt=str(input("Please input a string:"))
for i in txt:
    a.append(i)
for j in range(len(a)-1,-1,-1):
    p=p+a[j]
print(p)
input("Press Enter to exit...")
