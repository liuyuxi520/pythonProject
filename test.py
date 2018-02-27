# python3 最新语法

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


input('\n\n按下 enter 键后退出。')
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
#str[0]='m'会导致错误

# 5.函数，杨辉三角
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
print('yhsj',yhFn(7,3),yhFn(7,4),yhFn(7,5),yhFn(8,4))

