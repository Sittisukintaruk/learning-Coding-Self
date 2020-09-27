import requests 
from bs4 import BeautifulSoup
import pandas as pd




products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product


url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2" # url ของเว็บที่ต้องการดูข้อมูล
data = requests.get(url)


soup = BeautifulSoup(data.text ,'html.parser')
for a in soup.findAll('a', attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 



# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')