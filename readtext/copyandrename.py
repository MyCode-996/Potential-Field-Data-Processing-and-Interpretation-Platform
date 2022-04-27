'''
文件复制逻辑
1.打开文件
2.读取文件内容、
3.创建新文件，将数据写入新文件
4.关闭文件保存数据
'''
file_name = "d:/test.txt"
source_file = open("d:/test.txt", mode='r', encoding='utf-8')
all_data = source_file.read(4096)
flag = file_name.split('.')
new_file = open(flag[0]+"备份"+".txt",'w', encoding='utf-8')
new_file.write(all_data)
source_file.close()
new_file.close()
