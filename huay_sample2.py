import random
while(True):
    num = input("คำนวณเลข 2 ตัวล่าง => กรอกตัวเลข 0 - 9 จำนวน 3 - 9 ตัว ไม่ซ้ำตัวเดิม : ")
    if num.isdigit() == True : # ตรวจสอบข้อมูลเฉพาะตัวเลข
        if 3 <= len(num) <= 9 : # ตรวจสอบจำนวนตัวเลขที่กรอก
            if len(set(num)) == len(num) : # ตรวจสอบการกรอกตัวเลขซ้ำ
                break
    else:
        continue
#print(num)
fill = []
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

while(True):
    message = input("สุ่มคัดเลือกตัวเลขหรือไม่ พิมพ์ y = ตกลง พิมพ์ n = ไม่ตกลงหรือออกโปรแกรม :").lower()
    if message == "y" :
        while(True):
            select = input(f"เลขมีอยู่ {len(t_sr)} ตัว ต้องการเลือกกี่ตัว : ")
            if select.isdigit() == True :
                if 1 <= int(select) <= len(t_sr):
                    print(random.sample(t_sr,k=int(select)))
                    break
            else:
                continue
    elif message == "n" :
        break
    else:
        continue