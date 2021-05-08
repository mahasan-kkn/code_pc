from classloto import Calculate
''' module
    1.Calculate(number) # argument = str(number)
    2.lotto2() ==>return value (list)
    3.lotto3() ==>return value (list)
    4.ranlotto(numlist)  # argument = type list ==>return value (list)
    5.sendlotto(x,y,sendlist) argument point = พิกัดตำแหน่งหน้าจอ x , y  filetype=int
                                argument sendlist = ข้อมูลที่ต้องการส่ง filetype=list
                                การใช้งาน function ที่ 5 ให้แบ่งการทำงานเป็น 2 จอ
'''


#box = Calculate(Calculate.randNumber(7))
#huay = box.lotto3()
#randhuay = Calculate.ranlotto(huay)
#print(randhuay)
#Calculate.sendlotto(200,300,randhuay)
#Calculate.sendlottoVIP(480,615,randhuay)
#Calculate.selectVIP()
#a,b,c,d = Calculate.selectVIP()
#print(a)
#print(b)
#print(c)
#print(d)
#Calculate.loopVIP(a,b,c,d)
#tem = Calculate.randNumber(7)
#print(tem)
#m = "569"
#Cut = Calculate.cutnumber(m)
#print(Cut)
post = Calculate.formula_st(7)
box = Calculate(post)
huay = box.lotto3()
randhuay = Calculate.ranlotto(huay)
print(randhuay)
Calculate.sendlottoVIP(417,585,randhuay)
print("complete")