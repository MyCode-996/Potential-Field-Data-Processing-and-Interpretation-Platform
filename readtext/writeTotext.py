'''
向文件中写入文件使用  write()和writelines()
write()方法： test_data.write(str)    向文件中写入数据
writelines()方法： test_data.write([str])   向文件中写入字符串序列
'''
#追加，文件不为空
test_data = open("d:/test11.txt", mode='a+', encoding='utf-8')       #a+追加
print(test_data.write("hello"))

test_data = open("d:/test12.txt", mode='a+', encoding='utf-8')       #a+追加
print(test_data.writelines("\n" + "hello" + "\n" + "world"))

#写入空文件
with open("d:/test11.txt", mode='w', encoding='utf-8') as file_object:       #w   写入  这种模式下如果原来文件中有内容将被清空
    file_object.write("jjjj jjjj\n")
    file_object.write("jjjj jjjj")
#使用write函数写入时，不会在末尾添加换行符，所以需要手动添加换行符

