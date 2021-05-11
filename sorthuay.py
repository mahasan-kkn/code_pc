import os
filename = 'Hresult.txt'
f = open(filename,encoding='utf-8')
text = f.read()
print(type(text))
text1 = ""
for i in text:
    if i == ' ' or i == '\n':
        continue
    else:
        text1 += i
#print(text1)
text2 = text1.split('รอบที่')
print(text2)
lotto = []
for i in text2:
    for j in range(len(i)):
        note = ''
        if j <= 1:
            continue
        else:
            if i[j].isdigit():
                note += i[j]
            else:
                continue
        lotto.append(note)
print(lotto)  
f.close()