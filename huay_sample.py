import random
while(True):
    num = input("กรอกตัวเลข 0 - 9 จำนวน 4 - 9 ตัว ไม่ซ้ำตัวเดิม : ")
    if num.isdigit() == True : # ตรวจสอบข้อมูลเฉพาะตัวเลข
        if 4 <= len(num) <= 9 : # ตรวจสอบจำนวนตัวเลขที่กรอก
            if len(set(num)) == len(num) : # ตรวจสอบการกรอกตัวเลขซ้ำ
                break
    else:
        continue
#print(num)
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
while(True):
    message = input("สุ่มคัดเลือกตัวเลขหรือไม่ พิมพ์ y = ตกลง พิมพ์ n = ไม่ตกลง :").lower()
    if message == "y" :
        while(True):
            select = input(f"เลขมีอยู่ {len(total)} ตัว ต้องการเลือกกี่ตัว : ")
            if select.isdigit() == True :
                if 1 <= int(select) <= len(total):
                    print(random.sample(total,k=int(select)))
                    break
            else:
                continue
    elif message == "n" :
        break
    else:
        continue


            