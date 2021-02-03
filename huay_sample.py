fill = ['1','2','3','4','5','6','7']
len_fill = len(fill)
for i in range(len_fill-2):
    a = fill[i]
    for j in range((len_fill+i),(len_fill-1)):
        b = fill[j]
        for k in range(len_fill+i+1):
            c = fill[k]
            print(a+b+c)