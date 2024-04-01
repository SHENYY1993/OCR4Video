# print function
print("====print====")
print("Hello Python")
print("I'm killer")
print('I\'m killer')
print(int('1') + 2)

# 数学
print("\n====数学====")
print(1 + 1)
print(1 - 1)
print(1 * 2)
print(1 / 2)
print(2 ** 10)  # 幂
print(1 % 2)

# 自变量
print("\n====自变量====")
apple = 1
print(apple)
a, b, c = 1, 2, 3
print(a, b, c)  # 输出：1 2 3

# while & for loop
print("\n====while====")
condition = 0;
while condition < 10:
    print(condition)
    condition = condition + 1

example_list = [1, 2, 3, 4, 5, 6, 3, 53, 6, 45]
for i in example_list:
    print(i)

for i in range(1, 10):  # output 1 to 9
    print(i)

# continue & break
condition = 0
while True:
    condition = condition + 1
    if condition == 10:
        break
    if condition < 8:
        continue
    print("condition is:", condition)

print('Loop is ended')

# if
print("\n====if & else & elif====")
if a > b:
    print("a is larger than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is smaller than b")

# def
print("\n====def函数====")


def foo():
    print("foo in invoked")
    res = a + b
    print(res)
    return (res)


def foo(*arg):
    print("foo in invoked")
    a = arg[0]
    b = arg[1]
    res = a + b
    print(res)
    return (res)


foo(4, 2)

# global & local variable
print("\n====global & local variable====")

# import module
import numpy

print(numpy.abs(-1.0))

# read & write
print("\n====read & write====")
text = "This is my first text."
my_file = open("my_file.txt", "w")
my_file.write(text)
my_file.close()

append_text = "\nThis is appended file."

my_file = open('my_file.txt', 'a')
my_file.write(append_text)
my_file.close()

file = open('my_file.txt', 'r')
content = file.readlines()  # output:['This is my first text.\n', 'This is appended file.']
print(content)

# class
print("\n====class====")
import calculator

cal = calculator.Calculator("Stupid Calculator")
cal.add(3, 5)
cal.minus(8, 3)

# input
print("\n====input====")
# a_input = input("Please enter a number\n")
# print("This input number is:", a_input)

# tuple(元组) & list
print("\n====tuple(元组) & list====")
a_tuple = (1, 2, 3, 4, 5, 6)
a_list = [4, 3, 2, 1, 5, 6]
for i in a_tuple:
    print(i)

print(a_list)
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)
a_list.reverse()
print(a_list)

# multiple dimension list
print("\n====multiple dimension list====")
multi_dim_a = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
print(multi_dim_a[2][2])

# dictionary(字典)
print("\n====dictionary(字典)====")
a_dic = {'Benz': 30, 'BMW': 25, "Audi": 24}
print(a_dic['BMW'])
a_dic['BYD'] = 15
print(a_dic)
del a_dic['Benz']
print(a_dic)

# import module
import time

print(time.localtime().tm_year)

import time as t

print(t.localtime().tm_year)

from time import localtime

print(localtime().tm_year)

# try
print("\n====try & except====")
try:
    file = open('abc', 'r')
except Exception as e:
    print(e)

# zip
a_zip = [1, 2, 3]
b_zip = [4, 5, 6]
zipped_list = list(zip(a_zip, b_zip))
print(zipped_list)  # output:[(1, 4), (2, 5), (3, 6)]

# lambda & map
print("\n====lambda & map====")


def foo2(x, y):
    return x + y


lambda_foo = lambda x, y: x * 2 + y * 3
print(lambda_foo(1, 2))
# print(list(map(foo2, 1, 2))) # TypeError: 'int' object is not iterable
print(list(map(foo2, [1, 4], [2, 6])))  # 输入的参数需要是list

# 深拷贝 & 浅拷贝
print("\n====深拷贝 & 浅拷贝====")
import copy

origin_list = [1, 2, 3]
copy_list = origin_list
deep_copy_list = copy.copy(origin_list)
print(id(origin_list))
print(id(copy_list))  # same object as original list
print(id(deep_copy_list))  # different object from original list

copy_list[0] = 5
print(origin_list)
print(deep_copy_list)
deep_copy_list[0] = 10
print(origin_list)

# pickle(存储数据)
print("\n====pickle(存储数据)====")
import pickle

a_dict = {'Benz': 30, 'BMW': 25, "Audi": 24}
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

next_day_file = open('pickle_example.pickle', 'rb')
b_dict = pickle.load(next_day_file)
file.close()
print(b_dict)

# set
char_list = ['a', 'b', 'b', 'c', 'd', 'c']
a_set = set(char_list)
print(a_set)  # {'a', 'b', 'c', 'd'}
print(type(a_set))
sentence = "Welcome to This  Tutorial"
print(set(sentence))  # {'h', 'e', ' ', 'a', 'r', 's', 't', 'W', 'u', 'o', 'i', 'T', 'l', 'c', 'm'}

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
