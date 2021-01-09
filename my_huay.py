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

def r_time():
    tm = time.localtime()
    hour = tm.tm_hour
    min = tm.tm_min
    sec = tm.tm_sec
    return hour,min,sec

if __name__ == '__main__':
    t_h = [0,1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    t_m = [15,30,45,0]
    while(True):
        h,m,s = r_time()
        if h in t_h :
            if m in t_m :
                line.sendtext('หมดเวลารอผลอีก 3 นาที')
                time.sleep(210)
                send()
        else:
            time.sleep(20)
            continue
