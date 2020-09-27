import requests 
from bs4 import BeautifulSoup


url = "https://www.javacodegeeks.com/" # url ของเว็บที่ต้องการดูข้อมูล
data = requests.get(url)
# print(data.status_code)
# print(data.text)

soup = BeautifulSoup(data.text,'html.parser')

x = soup.find_all("p") # <- ค่าที่ใช้ในการค้นหา

for i in x:
    print(i.text)