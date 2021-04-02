import random
import pyautogui
import time

class Calculate:

    def __init__(self,number):
        self.number = number

    def lotto2(self):
        fill = []
        num = self.number
        for m in num : # แยกสายสตริงออกเป็นตัวๆเก็บไว้ในตัวแปร fill
            fill.append(m)
            #print(fill)
            total = [] # เรียงเลข 2 ตัวเก็บไว้ในตัวแปร total
            len_fill = len(fill)
        for i in range(len_fill):
            for j in range(len_fill):
                a = fill[i]+fill[j]
                total.append(a)
        total_sum = set(total) # ตัดตัวซ้ำเก็บค่าไว้ในตัวแปร total_sum
        total_repeat = []
        for m in total_sum:
            if m[0] == m[1]:
                total_repeat.append(m)
                #print(total_sum) # เลข 2 ตัวทั้งหมดที่ได้
                #print(total_repeat) # แยกเลขเบิ้ลออก
        t_r = set(total_repeat) # แปลงประเภทข้อมูลเป็น set เพื่อสะดวกในการลบเลขออก
        t_sr = list(total_sum - t_r) # เลขที่คัดกรองแล้วไม่มีเลขเบิ้ลและเลขซ้ำ
        return t_sr

    def lotto3(self):
        num = self.number
        fill = []
        for m in num : # แยกสายสตริงออกเป็นตัวๆเก็บไว้ในตัวแปร fill
            fill.append(m)
            #print(fill)
        total = [] # เรียงเลข 3 ตัวไม่ซ้ำกันเก็บไว้ในตัวแปร total
        len_fill = len(fill)
        for i in range(len_fill-2):
            a = fill[i]
            for j in range((i+1),(len_fill-1)):
                b = fill[j]
                for k in range(j+1,len_fill):
                    c = fill[k]
                    total.append(a+b+c)
        return total

    @staticmethod
    def ranlotto(numlist):
        num = numlist
        lennum = len(num)
        while(True):
            select = input(f"เลขมีอยู่ {lennum} ตัว ต้องการเลือกกี่ตัว : ")
            rander = []
            if select.isdigit() == True :
                if 1 <= int(select) <= lennum:
                    rander = random.sample(num,k=int(select))
                    break
            else:
                print("กรอกข้อมูลให้ถูกต้อง")
        return rander
        
    @staticmethod
    def sendlotto(x,y,sendlist):
        pool = sendlist
        pyautogui.moveTo(x,y,2)
        pyautogui.click()
        for i in pool :
            pyautogui.typewrite(i)
            time.sleep(1)
            pyautogui.typewrite(['enter'])

    @staticmethod
    def sendlottoVIP(x,y,sendlist): # ค่า x และ y หาด้วยโปรแกรม "MPos.exe"
        pool = ""
        for i in sendlist:
            for j in i :
                pool += j
        pyautogui.moveTo(x,y,2)
        pyautogui.click()
        for k in pool:
            pyautogui.typewrite(k)
            time.sleep(0.5)

    @staticmethod
    def selectVIP():
        sort3 = []
        switch3 = []
        top2 = []
        bottom2 = []
        while True:
            twoORtree = input("3 ตัวบน พิมพ์ : aaa    เลข 3 ตัวโต๊ด พิมพ์ : bbb \n 2 ตัวบน พิมพ์ : aa 2 ตัวล่าง พิมพ์ : cc \n หรือออกจากโปรแกรม พิมพ์ : q \n")
            if twoORtree == "aaa" :
                while True:
                    data = ""
                    data = input("พิมพ์ตัวเลข 3 ตัว : ")
                    sort3.append(data)
                    out = input("พิมพ์ต่อเลือก : พิมพ์อะไรก็ได้  ไม่พิมพ์ต่อเลือก : n ==> ")
                    if out == "n" :
                        print(sort3)
                        break
                    else:
                        continue
            elif twoORtree == "bbb" :
                while True:
                    data = ""
                    data = input("พิมพ์ตัวเลข 3 ตัว : ")
                    switch3.append(data)
                    out = input("พิมพ์ต่อเลือก : พิมพ์อะไรก็ได้  ไม่พิมพ์ต่อเลือก : n  ==> ")
                    if out == "n" :
                        print(switch3)
                        break
                    else:
                        continue
            elif twoORtree == "aa" :
                while True:
                    data = ""
                    data = input("พิมพ์ตัวเลข 2 ตัว : ")
                    top2.append(data)
                    out = input("พิมพ์ต่อเลือก : พิมพ์อะไรก็ได้  ไม่พิมพ์ต่อเลือก : n  ==> ")
                    if out == "n" :
                        print(top2)
                        break
                    else:
                        continue
            elif twoORtree == "cc" :
                while True:
                    data = ""
                    data = input("พิมพ์ตัวเลข 2 ตัว : ")
                    bottom2.append(data)
                    out = input("พิมพ์ต่อเลือก : พิมพ์อะไรก็ได้  ไม่พิมพ์ต่อเลือก : n  ==> ")
                    if out == "n" :
                        print(bottom2)
                        break
                    else: 
                        continue
            elif twoORtree == "q" :
                print(f"สามตัวบน = {sort3} \n สามตัวโต๊ด = {switch3} \n สองตัวบน = {top2} \n สองตัวล่าง {bottom2}")
                break
            else :
                print("พิมพ์ใหม่")
                continue
        return sort3,switch3,top2,bottom2

    @staticmethod
    def loopVIP(s1,s2,s3,s4): # s1,s2,s3,s4 = สามตัวตรง,สามตัวโต๊ด,สองตัวบน,สองตัวล่าง ==> typelist
        while True:
            lotto = input("เลือก 3 ตัวตรง พิมพ์ : t1 เลือก 3 ตัวโต๊ด พิมพ์ : t2 \n เลือก 2 ตัวบน พิมพ์ : t3 เลือก 2 ตัวล่าง พิมพ์ : t4 \n ออกจากโปรแกรม พิมพ์ q ==> ")
            if lotto == "q" :
                break
            elif lotto == "t1" :
                sendlist = s1
                x = int(input("พิกัดแกน x ==> "))
                y = int(input("พิกัดแกน y ==> "))
                Calculate.sendlottoVIP(x,y,sendlist)
            elif lotto == "t2" :
                sendlist = s2
                x = int(input("พิกัดแกน x ==> "))
                y = int(input("พิกัดแกน y ==> "))
                Calculate.sendlottoVIP(x,y,sendlist)
            elif lotto == "t3" :
                sendlist = s3
                x = int(input("พิกัดแกน x ==> "))
                y = int(input("พิกัดแกน y ==> "))
                Calculate.sendlottoVIP(x,y,sendlist)
            elif lotto == "t4" :
                sendlist = s4
                x = int(input("พิกัดแกน x ==> "))
                y = int(input("พิกัดแกน y ==> "))
                Calculate.sendlottoVIP(x,y,sendlist)
            else :
                continue

    @staticmethod
    def randNumber(r_num): # r_num = เลข 0 - 9 จำนวนกี่ตัว type = int
        dunk = ['0','1','2','3','4','5','6','7','8','9']
        rander = random.sample(dunk,k=r_num)
        randoor = ""
        for i in rander:
            randoor += i
        return randoor





