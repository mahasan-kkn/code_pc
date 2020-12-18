import random
print("เลือกเลขมา 6 ตัวที่ไม่ซ้ำ")
b = []
for i in range(6): # วนเก็บข้อมูล 6 ครั้งเก็บไว้ในตัวแปร b
    print(f"เลขตัวที่ {i+1} : ")
    while True:
        a = input()
        if len(a) > 1 or a.isdigit() != True or a in b : # ตรวจสอบให้กรอกทีละตัว,เป็นตัวเลข และไม่ซ้ำตัวที่เคยกรอกมาแล้ว
            print("ไม่ถูกต้องพิมพ์ใหม่")
            continue
        else:
            b.append(a) # ตรงตามเงื่อนไขก็เพิ่มข้อมูลเก็บไว้ในตัวแปร b
            break
print(b)

