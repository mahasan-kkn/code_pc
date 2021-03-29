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
    def sendlottoVIP(x,y,sendlist):
        pool = ""
        for i in sendlist:
            for j in i :
                pool += j
        pyautogui.moveTo(x,y,2)
        pyautogui.click()
        for k in pool:
            pyautogui.typewrite(k)
            time.sleep(0.5)
        


