def tamnai():
    import random
    print("select 0 - 9 ==> 7 times : ")
    b = []
    for i in range(7): # วนเก็บข้อมูล 7 ครั้งเก็บไว้ในตัวแปร b
        print(f"number  {i+1} : ")
        while True:
            a = input()
            if len(a) > 1 or a.isdigit() != True or a in b : # ตรวจสอบให้กรอกทีละตัว,เป็นตัวเลข และไม่ซ้ำตัวที่เคยกรอกมาแล้ว
                print("try again")
                continue
            else:
                b.append(a) # ตรงตามเงื่อนไขก็เพิ่มข้อมูลเก็บไว้ในตัวแปร b
                break
    print(b)
    print(" bingo.. !!! ")
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15 = b[0]+b[1]+b[2],b[0]+b[1]+b[3],b[0]+b[1]+b[4],b[0]+b[1]+b[5],b[0]+b[1]+b[6],b[0]+b[2]+b[3],b[0]+b[2]+b[4],b[0]+b[2]+b[5],b[0]+b[2]+b[6],b[0]+b[3]+b[4],b[0]+b[3]+b[5],b[0]+b[3]+b[6],b[0]+b[4]+b[5],b[0]+b[4]+b[6],b[0]+b[5]+b[6]
    d1,d2,d3,d4,d5,d6,d7,d8,d9,d10 = b[1]+b[2]+b[3],b[1]+b[2]+b[4],b[1]+b[2]+b[5],b[1]+b[2]+b[6],b[1]+b[3]+b[4],b[1]+b[3]+b[5],b[1]+b[3]+b[6],b[1]+b[4]+b[5],b[1]+b[4]+b[6],b[1]+b[5]+b[6]
    f1,f2,f3,f4,f5,f6 = b[2]+b[3]+b[4],b[2]+b[3]+b[5],b[2]+b[3]+b[6],b[2]+b[4]+b[5],b[2]+b[4]+b[6],b[2]+b[5]+b[6]
    g1,g2,g3 = b[3]+b[4]+b[5],b[3]+b[4]+b[6],b[3]+b[5]+b[6]
    h1 = b[4]+b[5]+b[6]
    lot = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,f1,f2,f3,f4,f5,f6,g1,g2,g3,h1]
    print(random.sample(lot,k=30))
if __name__ == '__main__':
    while (True):
        tamnai()
        x = input(" q = 'quit' or ....... : ")
        if x == "q":
            break
        else:
            continue