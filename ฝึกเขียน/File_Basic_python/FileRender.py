
fo = open("foo.txt", "w") #สร้างไฟล์ foo
print ("Name of the file: ", fo.name)#เเสดงชื่อไฟล์
print ("Closed or not : ", fo.closed) #เช็คว่าปิดไฟล์
print ("Opening mode : ", fo.mode)#แสดง mode ที่เปิด
fo.write( "Python is a great language.\nYeah its great!!\n") #เขียนข้อมูลลงไปใน fo
fo.close() #ปิดไฟล์
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)
# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
print ("Again read String is : ", str)

# Close opened file
fo.close() #ปิดไฟล์
