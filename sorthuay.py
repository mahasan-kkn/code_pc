import os
import numpy as np
filename = 'huayresult.txt'
f = open(filename,encoding='utf-8')
text = f.read()
f.close() # เก็บข้อมูลไว้ในตัวแปร text แล้วก็ใช้คำสั่งปิดไฟล์ได้เลย
#print(type(text))
text1 = ""
for i in text:
    if i == ' ' or i == '\n': # ตัดเว้นวรรคและคำสั่งขึ้นบรรทัดใหม่ออกนำมาต่อกันเก็บไว้ในตัวแปร text1(ตัวแปรสตริง)
        continue
    else:
        text1 += i
#print(text1)
text2 = text1.split('รอบที่') # ตัวคำเอาคำว่า 'รอบที่' ออก ข้อมูลสตริงสายยาวๆจะถูกแบ่งเป็นข้อมูลสตริงที่เก็บไว้ใน list ชื่อตัวแปร text2
#print(text2)
lotto = []
for i in text2:
    for j in range(len(i)): # วนลูปคัดเอาเฉพาะเลข 3 ตัวและ 2 ตัวออกมาเก็บไว้ใน list ชื่อตัวแปร lotto
        note = ''
        if j <= 1:
            continue
        else:
            if i[j].isdigit():
                note += i[j]
            else:
                continue
        lotto.append(note)
#print(lotto) 
dm = []
k = 0
m = []
for i in range(len(lotto)): # สร้างลิสต์ซ้อนลิสต์โดยเก็บตัวแปรเลข 3 ตัวและ 2 ตัวที่ออกรอบเดียวกันเก็บไว้ในลิสต์เดียวกัน และลิสต์แต่ละรอบจะส่งไปเก็บในลิสต์ชื่อ dm
    k += 1
    if k <= 5 :
        m.append(lotto[i])
    else:
        dm.append(m)
        k = 1
        m = []
        m.append(lotto[i])
#print(dm)

#----------------------------------------------------
t = '0123456789'
a = []
b = []
c = []
for i in t:
    a.append(i)
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        r1 = a[i]
        r2 = a[j]
        b.append(r1)
        b.append(r2)
        c.append(b)
        b = []
#print(c)
art = 0
df = len(dm)
for i in c:
    for j in dm:
        if i[0] in j:
            if i[1] in j:
                art += 1
    #print("{} = {:.2f} %".format(i,(art/df)*100))
    art = 0

tek = 0
bt = [str(i) for i in range(10)]
for i in bt:
    for j in range(len(dm)):
        if i in dm[j]:
            tek += 1
    print("เลข :{} ==> {:.2f} %".format(i,(tek/len(dm))*100))
    tek = 0
