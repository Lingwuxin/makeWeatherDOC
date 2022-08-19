# getCity_Weather.py v1.2 for 天气预报1.2.2

from bs4 import BeautifulSoup
import requests


class Weather():

    def __init__(self, url='', wea='', temHigh='', temLow='', rays=''):
        self.wea = wea
        self.temHigh = temHigh
        self.temLow = temLow
        self.url = url
        self.rays = rays

    def getWeather(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        res = requests.get(self.url, headers=headers, timeout=20)
        res.encoding = 'utf-8'

        soup = BeautifulSoup(res.text, 'html.parser')

        tem_list = soup.find_all('p', class_='tem')  #温度
        # day = soup.find('ul',class_='t clearfix')  #日期
        wealist = soup.find_all('p', class_='wea')   #天气

        for i in range(1, 2):
            try:
                self.temHigh = tem_list[i].span.string  # 有时候没有最高温度，用第二天的代替
            except AttributeError as e:                 # 我管这叫作糊弄学
                self.temHigh = tem_list[i+1].span.string
            if self.temHigh[-1] != '℃':
                self.temHigh+='℃'
            self.temLow = tem_list[i].i.string
            if self.temLow[-1]!='℃':
                self.temLow+='℃'

        self.wea = wealist[1].string
        if len(self.wea) > 2:
            self.wea = self.wea[0:2]
            if self.wea[-1] == '转':
                self.wea = self.wea[0:1]

    def citys_weather(self):
        hrefList = {'郑州': 'http://www.weather.com.cn/weather/101180101.shtml',
                    '安阳': 'http://www.weather.com.cn/weather/101180201.shtml',
                    '新乡': 'http://www.weather.com.cn/weather/101180301.shtml',
                    '许昌': 'http://www.weather.com.cn/weather/101180401.shtml',
                    '平顶山': 'http://www.weather.com.cn/weather/101180501.shtml',
                    '信阳': 'http://www.weather.com.cn/weather/101180601.shtml',
                    '开封': 'http://www.weather.com.cn/weather/101180801.shtml',
                    '洛阳': 'http://www.weather.com.cn/weather/101180901.shtml',
                    '商丘': 'http://www.weather.com.cn/weather/101181001.shtml',
                    '焦作': 'http://www.weather.com.cn/weather/101181101.shtml',
                    '鹤壁': 'http://www.weather.com.cn/weather/101181201.shtml',
                    '濮阳': 'http://www.weather.com.cn/weather/101181301.shtml',
                    '周口': 'http://www.weather.com.cn/weather/101181401.shtml',
                    '漯河': 'http://www.weather.com.cn/weather/101181501.shtml',
                    '驻马店': 'http://www.weather.com.cn/weather/101181601.shtml',
                    '三门峡': 'http://www.weather.com.cn/weather/101181701.shtml',
                    '济源': 'http://www.weather.com.cn/weather/101181801.shtml', }

        # self.url="http://www.weather.com.cn/weather/101210701.shtml"
        # self.getWeather()
        weather_table = ''
        num = 0
        for i in hrefList.keys():
            self.url = hrefList[i]
            self.getWeather()
            weather_table = weather_table+i+'  \t'+self.wea + \
                ' \t'+self.temLow+' \t'+self.temHigh
            if num % 2 == 0:
                weather_table = weather_table+'\t\t'
            else:
                weather_table = weather_table+'\n'
            num = num+1
        return weather_table
