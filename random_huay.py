huay = ['79157','98977','50105','93790','17488','15673','89268','97101','72463','29845']
point = 0
num = input("เลขที่ต้องการตรวจ : ")
for i in range (len(huay)):
    if num in huay[i] :
        point += 1
    else:
        continue
print("จำนวนที่พบ",point)
    