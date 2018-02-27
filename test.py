# python3 最新语法
# -*- coding: UTF-8 -*-
print('Hello, Python!')

# 1.Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
print('1.Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建')
x = 12
y = 55
print(x)
print(y)
print('--------')
print(x,y)
a = b = c =1
print('a,b,c',a,b,c)



# 2.python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束.
print('2.python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束.')
if False:
    print('True 是我')
elif True:
    print('False 是她')
else:
    print('false 是它')


# input('\n\n按下 enter 键后退出。')
import sys
print('argv:',sys.argv)
print('path:',sys.path)

# 3.数据类型 Number 支持 int,float,bool,complex(复数)
print('3.数据类型 Number 支持 int,float,bool,complex(复数)')
d,e,f,g = 1,2.5,True,4+3j
print(type(d),type(e),type(f),type(g))
print('是否',isinstance(d,int))

# 4.数据类型 String 不能被改变
print('4.数据类型 String 不能被改变')
print('Ru\noob')
print(r'Ru\noob') #反斜杠用来转义，使用r可以让反斜杠不发生转义

str = 'runoob'
print('str*2:',str*2) #输出两次
print(str[0:-1]) #输出第一个到倒数第二个所有字符
print(str[2:]) #输出从第三个开始后的所有
#str[0]='m' #会导致错误

# 5.数据类型 列表
print('5.数据类型 列表')
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = list1 + list2
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
print ('list3:',list3)
del list2[3]
print ('list2删除第四个元素',list2)
list1.append('baidu')
print ('append()向列表的末尾添加新元素，类似array的push',list1)
list2.extend([40,50,60])
print ('extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中',list2)

# 6.数据类型 元组
print('6.数据类型 元组')
tup1 = (); #创建新元组
tup1 = (50,) #当元组中有一个元素时，后面要加逗号，否则括号会被当作运算符
print ('tup1类型',type(tup1))
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2 #元组不能修改内部值，但可以对元组进行连接组合
print ('tup3:',tup3)
del tup2
# print ('删除后的tup2:',tup2) ＃NameError: name 'tup2' is not defined
for x in tup3:
    print ('every x :',x)
print('计算tup3的长度:',len(tup3))
# max(tuple)返回元组中元素最大值。min(tuple) 返回元组中元素最小值。
# 5.函数，杨辉三角
print('5.函数，杨辉三角')
def yhFn(n,m):
    if(m > n):
        return false
    if(m == 1 and n == 1):
        return 1
    if(m == 1 or m == n):
        return 1
    if(n > 2 and (m == 2 or m == n-1)):
        return n-1
    return yhFn(n-1,m-1) + yhFn(n-1,m)
print('yhsj',yhFn(7,3),yhFn(7,4),yhFn(7,5),yhFn(8,4),yhFn(10,3))

# 6.时间，日历
print('6.时间，日历')
import calendar
cal = calendar.month(2018, 2)
print("以下输出2018年2月份的日历:")
print(cal)