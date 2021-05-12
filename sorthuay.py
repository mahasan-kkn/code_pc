import os
import numpy as np
filename = 'Hresult.txt'
f = open(filename,encoding='utf-8')
text = f.read()
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
arr = np.array(dm) # นำลิสต์ dm ไปสร้างเป็น array 2 มิติ ชื่อ arr
print(arr)
f.close()