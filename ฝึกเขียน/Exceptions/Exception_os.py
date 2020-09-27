#สร้าง Exception ของ การเปิดไฟล์
import sys

try:
    f = open('foo.txt')
    s = f.readline()
    print(s)

except OSError as err:
    print("OS error: ", err)

except:
    print("Unexpected error occured")

else:
    print("File closed successfully")
    f.close()