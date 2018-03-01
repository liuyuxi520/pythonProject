# -*- coding: UTF-8 -*-
def yhFn(n):
    Li = [1]
    while True:
        if(n<len(Li)):
            return
        yield Li
        Li = [1] + [Li[i]+Li[i+1] for i in range(len(Li)-1)] + [1]
f2 = yhFn(5)

print ('杨辉三角111')   
for i in f2:
    print (i) 

def insertSort(list):
    lang = len(list)
    if lang <= 0:
        return '请输入有值列表'
    if lang == 1:
        return lists
    for i in range(1,lang):
        key = list[i]
        j = i - 1 
        while j>=0:
            if list[j] > key:
                list[j+1]=list[j]
                list[j] = key
            j-=1
    return list        
print('插入排序：',insertSort([6,2,8,3,1]))   