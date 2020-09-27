import _thread
import time
"""
คือการแบ่งการทำงานของโปรแกรม ให้สามารถทำงานควบคู่ไปด้วยกันได้ 
ยกอย่างข้างล่าง คือการแบ่งเป็นสองการทำงาน แล้วสั่งให้ทำงานจนกว่าโปรแกรมใดจะนับได้มากกว่าหรือ 
เท่ากับ 5 ถึงว่าเสร็จสินการทำงาน
"""

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s : %d" % ( threadName, time.ctime(time.time()) ,count))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")
   
while 1:
   pass