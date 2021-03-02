#!/usr/bin/python
# -*- coding: utf-8 -*-
p=""
print("Simple tool for reversing string by William Wei")
txt=str(input("Please input a string:"))
for j in range(len(txt)-1,-1,-1):
    p=p+txt[j]
print(p)
input("Press Enter to exit...")
