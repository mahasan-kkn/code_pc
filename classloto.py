import random
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
        t_sr = total_sum - t_r # เลขที่คัดกรองแล้วไม่มีเลขเบิ้ลและเลขซ้ำ
        print(t_sr)
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
        print(total)

