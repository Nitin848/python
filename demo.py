# f=open("test.txt",'w')
# f=open("test.txt",'r')
# for i in range(11):
#     a=str(i)
#     f.write(a)
#     f.read(a)
import win32file

with open("test.txt", 'w', encoding='utf-8')as f:

     f.write("my frist line")
     f.write("this file")
     f.write("contains threee lines")

with open("test.txt", 'r', encoding='utf-8')as f:
         print(f.read())
         print(f.tell())
         print(f.seek(10))



