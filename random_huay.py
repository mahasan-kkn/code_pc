huay = ['79157','98977','50105','93790','17488','15673','89268','97101','72463','29845','13234','16277','78304','96379','42678','29062','27336','90214','43958']
'''point = 0
num = input("เลขที่ต้องการตรวจ : ") # หาเลขที่ต้องการตรวจมาบ่อยไหม
for i in range (len(huay)):
    if num in huay[i] :
        point += 1
    else:
        continue
print("จำนวนที่พบ",point)
# ----------------------------------------------------------------------
len_huay = len(huay) # หาเลข 3 ตัวโอกาสกลับมาซ้ำบ่อยไหม
print("จำนวนรอบ = ",len_huay)
num = 0
for i in range(len_huay-1):
    if huay[i+1][0] in huay[i] or huay[i+1][1] in huay[i] or huay[i+1][2] in huay[i] :
        num += 1
    else:
        continue
print("เลข 3 ตัวเก่าไม่มา = ",(len_huay-num))
# ----------------------------------------------------------------------
len_huay = len(huay) # หาเลข 2 ตัวกลับมาซ้ำไหม
print("จำนวนรอบ = ",len_huay)
num = 0
for i in range(len_huay-1):
    tree = huay[i+1][0]+huay[i+1][1]+huay[i+1][2]
    if huay[i][3] in tree or huay[i][4] in tree :
        num += 1
    else:
        continue
print("เลข 2 ตัวเก่าไม่มา = ",(len_huay-num))
#------------------------------------------------------------------------------
len_huay = len(huay) # หาเลข 3 ตัวกลับมาซ้ำไหม
print("จำนวนรอบ = ",len_huay)
num = 0
for i in range(len_huay-1):
    tree = huay[i+1][0]+huay[i+1][1]+huay[i+1][2]
    if huay[i][0] in tree or huay[i][1] in tree or huay[i][2] in tree:
        num += 1
    else:
        continue
print("เลข 3 ตัวเก่าไม่มา = ",(len_huay-num))'''
#---------------------------------------------------------------------------------
len_huay = len(huay) # หาเลข 3 ตัวกลับมาซ้ำไหม
print("จำนวนรอบ = ",len_huay)
num = 0
for i in range(len_huay-1):
    temp = 0
    tree = huay[i+1][0]+huay[i+1][1]+huay[i+1][2]
    if huay[i][0] in tree :
        temp += 1
    if huay[i][1] in tree :
        temp += 1
    if huay[i][1] in tree :
        temp += 1
    if 0 < temp < 2 :
        num += 1
print("เลข 3 ตัวเก่ามา = ",(num))
    