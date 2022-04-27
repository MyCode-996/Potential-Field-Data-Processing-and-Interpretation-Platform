#读取整个文件
with open("d:/test.txt") as file_object:
    contents = file_object.read()
    # print(contents.rstrip())
'''
此时contents是一个长长的字符串  输出时在末尾会多出一个空行，因为read（）到达文件尾部时会返回一个空的字符串，而这个空的字符串显示出来就就是一个空行
若想去掉这个空行，加rstrip即可
'''

#逐行读取
# with open("d:/test.txt") as file_object:
#     for line in file_object:
#         print(contents.rstrip())

with open("d:/test.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
        
#可以使用strip（）删除换行符

with open("d:/test.txt") as file_object:
    lines = file_object.readlines()
    string = ''
    for line in lines:
        string += line.rstrip()
    print(string)
    print(len(string))