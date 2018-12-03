import requests
from bs4 import BeautifulSoup
from threading import Thread

def down_pic(link,pic_num):
    retire = 0
    while retire < 3:
        try:
            if link.get('data-lazy') != None:
                pic_url = requests.get(link.get('data-lazy'),timeout=15)
                with open(str(pic_num)+'.jpg',"wb") as f:
                    f.write(pic_url.content)
            else:
                pic_url = requests.get(link.get('src'),timeout=15)
                with open(str(pic_num)+'.jpg',"wb") as f:
                    f.write(pic_url.content)
        except requests.exceptions.RequestException as e:
            retire+=1
            print(e)
            print(str(pic_num)+'.jpg','failed')
        else:
            print(str(pic_num)+'.jpg','saved')
            break


pixabay_url = 'https://pixabay.com/'
text = requests.get(pixabay_url)
soup = BeautifulSoup(text.content,'lxml')
# print(soup)

pic_html = soup.find_all('div',class_='item')
pic_num = 0
for each in pic_html:
    link = each.find('img')
    t = Thread(target=down_pic,args=(link,pic_num,))
    t.start()
    pic_num+=1