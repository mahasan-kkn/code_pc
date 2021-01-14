import requests
import time
from bs4 import BeautifulSoup
from parinya import LINE
line = LINE("d3dVYwoTtmtGtLrDGXz491ZZlzogquSTAgVAa0bF7bI")
web = "https://www.huay.com/login"
def send():
    page = requests.get(web)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.content,'lxml')
    soup1 = soup.find('div',class_= 'card-body p-2')
    header = soup1.find(class_="text-danger").text
    header1 = header[:25] # จับยี่กี่รอบที่ ....
    soup2 = soup1.find_all('p',class_="number text-center m-0")
    soup3 = [] # สามตัวบนกับสองตัวล่าง
    for i in soup2:
        soup3.append(i.text)
    post = header1+'สามตัวบน  '+str(soup3[0])+'  สองตัวล่าง   '+str(soup3[1])
    print(post)
    line.sendtext(post)

def check():
    page = requests.get(web)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.content,'lxml')
    soup1 = soup.find('div',class_= 'card-body p-2')
    header = soup1.find(class_="text-danger").text
    header1 = header[:25] # จับยี่กี่รอบที่ ....
    return header1

if __name__ == '__main__':
    pretest = 'wellcom'
    while(True):
        audit = check()
        if pretest != audit :
            send()
            pretest = audit
            continue
        else:
            time.sleep(20)
            continue
