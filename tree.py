
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

t1,t2,t3,t4,t5,t6,t7,t8,t9,t10 = b[0]+b[1]+b[2],b[0]+b[1]+b[3],b[0]+b[1]+b[4],b[0]+b[1]+b[5],b[0]+b[2]+b[3],b[0]+b[2]+b[4],b[0]+b[2]+b[5],b[0]+b[3]+b[4],b[0]+b[3]+b[5],b[0]+b[4]+b[5]
print(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10)
r1,r2,r3,r4,r5,r6 = b[1]+b[2]+b[3],b[1]+b[2]+b[4],b[1]+b[2]+b[5],b[1]+b[3]+b[4],b[1]+b[3]+b[5],b[1]+b[4]+b[5]
print(r1,r2,r3,r4,r5,r6)
y1,y2,y3 = b[2]+b[3]+b[4],b[2]+b[3]+b[5],b[2]+b[4]+b[5]
print(y1,y2,y3)
m1 = b[3]+b[4]+b[5]
print(m1)

 
