import requests
from bs4 import BeautifulSoup

web = 'https://www.melotto.com/login'
soup = requests.get(web)
melo = BeautifulSoup(soup.content,'lxml')
melo1 = melo.find_all('div',class_ = 'row')
print(melo1)