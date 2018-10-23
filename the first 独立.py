
import time
import requests
from bs4 import BeautifulSoup
user_agent = ""
'''
import requests
from bs4 import BeautifulSoup
import time
url = "https://www.tripadvisor.cn/Hotel_Review-g294212-d1414087-Reviews-Beijing_Qianmen_Guanqi_Hotel-Beijing.html#apg=029157d74b54476d9f763e7821ad1423&ss=472FE5670259B7973E544AC1E6DB6BEF"
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

'''
url = ['https://www.tripadvisor.cn/Hotels-g294212-oa{}-Beijing-Hotels.html'.format(str(i)) for i in range(30, 900, 30)]


def main():
    for i in url:
        a(i)


def a(a):
    time.sleep(2)
    wb_data = requests.get(a)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text, 'html-paser')
    titles = soup.select('div.listing_title > a')
    prices = soup.select('div.price-wrap > div')
    imgs = soup.select('div.inner')
    for title, price, img in zip(titles, prices, imgs):
        data = {
            'title': title.get_text(),
            'price': list(price.stripped_strings),
            'img': img.get('data-lazyurl')
        }
        print(data)
        with open('a.txt','a') as f:
                for key in data:
                    f.write(str(data[key])+"\n")
        f.close()


if __name__ == '__main__':
    main()

