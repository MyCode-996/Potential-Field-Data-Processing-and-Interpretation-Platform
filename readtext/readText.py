#打开文件
test_data = open("d:/test.txt", 'r')
#关闭文件
test_data.close()
#3种常见的文件读取的方法：read() readline()  readlines

'''
read()  可以从指定文件中读取指定数据  test_data.read([size])
'''
test_data = open("d:/test.txt", mode='r', encoding='utf-8')
print("读取两个字节")
print(test_data.read(2))
test_data.close()

test_data = open("d:/test.txt", mode='r', encoding='utf-8')
print("读取全部数据")
print(test_data.read())
test_data.close()
'''
readline()  可以从指定文件中读头行数据  test_data.readline()
readline()方法每执行一次只会读取文件中的一行数据
'''
test_data = open("d:/test.txt", mode='r', encoding='utf-8')
print(test_data.readline())
test_data.close()
'''
readlines()  可以一次读取文件中的所有数据  test_data.readlines()
readline()方法每执行一次只会读取文件中的一行数据
'''
test_data = open("d:/test.txt", mode='r', encoding='utf-8')
print(test_data.readlines())
test_data.close()

'''
通常用read（）方法
'''