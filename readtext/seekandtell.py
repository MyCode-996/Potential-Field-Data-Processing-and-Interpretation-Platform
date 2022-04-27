'''
使用tell（）和seek（）获取文件读写位置及修饰文件读写位置信息的方法
tell（）方法 获取当前文件读写的位置   test_data.tell()
seek（）方法 设置当前文件读写的位置   test_data.seek(offset， from)
offset表示偏移量 即读写位置需要移动的字节数  from用于指定文件的读写位置 参数的取值为0 1 2
0 表示在开始位置读写
1 表示在当前位置读写
2 表示在末尾位置读写
'''
file = open("d:/test.txt", mode='r', encoding='utf-8')
file.read(7)       #读取7个字节
print(file.tell())     #7

file = open("d:/test11.txt", mode='r', encoding='utf-8')
print(file.seek(15,0))   #将文件读取位置移动至开始位置偏移15个字节处，并使用read方法读取
print(file.read())
file.close()