import os                                   #开始
def NewCaesar(m,n,t):                       #定义新函数NewCaeser
    z='';i=0                                #定义空字符串z，作为密文/明文输出，定义循环变量i=0
    while i<len(t):                         #在给出的明文/密文长度内循环
        tmp=t[i].upper()                    #取给出明文的第i个字符转换为大写进行加密/解密
        if tmp in m:                        #检测字符是否在密码表里
            if ord(t[i])<=90:               #检测字母是否为大写
                z+=n[m.find(tmp)]           #大写字母加密/解密
            else:
                z+=n[m.find(tmp)].lower()   #否则将密码表转换为小写，小写字母加密/解密
        else:
            z+=t[i]                         #不是字母，输出原字符
        i+=1                                #进行下个循环
    return z                                #输出
m='ABCDEFGHIJKLMNOPQRSTUVWXYZ'              #定义明文表
n='QWERTYUIOPASDFGHJKLZXCVBNM'              #定义密文表
a=input('请输入<明文>a=')
b=NewCaesar(m,n,a)                          #加密
print('对应的密文为：',b)
c=NewCaesar(n,m,b)                          #解密
print('解密后明文为：',c)
if a==c:                                    #判断加密解密后是否与原文一致
    print('加密解密成功！')
else:
    print('加密解密失败！')
input('运行完毕，请按回车键退出...')
os._exit(0)                                 #结束
#str.find(str,beg=0,end=len(string)):检测字符串内是否含有字符串str，并返回其位置，否则返回-1。
#str.lower():返回字符串内英文的小写。
