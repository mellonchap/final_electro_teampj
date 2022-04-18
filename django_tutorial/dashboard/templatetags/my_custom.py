import requests
from bs4 import BeautifulSoup as BS
from django import template

url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
params ={'serviceKey' : 'xA349UTzw+UCTf9dZmcCmiOViDD/q9G5iEADL9sgSQGWfaKmHkfHZ6M2l3bjrTvI4Y7a7wgl8LOtmTC4rSyWMQ==', 'pageNo' : '1', 'numOfRows' : '1', 'addr' : '강원도' }

response = requests.get(url, params=params)
soup = BS(response.text, 'html.parser')
# print(response.text)

items = soup.find_all('item')
for i in items:
    a = float(i.find('lat').text)
    b = float(i.find('longi').text)

    # print(i.find('lat').text, ', ', i.find('longi').text)
print(a)
register = template.Library()
    
@register.simple_tag
def my_tag():
    return a

@register.simple_tag
def my_tag2():
    return b