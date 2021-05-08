import requests
from bs4 import BeautifulSoup

web = 'https://www.melotto.com/login'
soup = requests.get(web)
melo = BeautifulSoup(soup.content,'lxml')
#print(melo.prettify)
melo1 = melo.find_all('div', class_="col-12 px-1 mb-2")
print(melo1)