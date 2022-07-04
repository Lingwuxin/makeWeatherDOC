#v1.0
import requests
from bs4 import BeautifulSoup

def get_airs():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        res = requests.get('https://tianqi.2345.com/air-57178.htm', headers=headers,timeout=20)
        res.encoding = 'utf-8'
        #print(res.status_code)
        soup = BeautifulSoup(res.text,'html.parser')
        airs_spuer=soup.find_all('div',class_='aqi-map-con')

        airs=airs_spuer[0].em.string
        return airs
def get_rays():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        res = requests.get('http://www.weather.com.cn/weather1d/101180701.shtml#input', headers=headers,timeout=20)
        res.encoding = 'utf-8'
        #print(res.status_code)
        soup = BeautifulSoup(res.text,'html.parser')
        rays_spuer=soup.find_all('li',class_='li1 hot')
        rays=rays_spuer[0].span.string
        return rays