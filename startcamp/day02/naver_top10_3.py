import requests
import bs4

response = requests.get('https://naver.com').text
soup = bs4.BeautifulSoup(response, 'html.parser')#
result = soup.select('.ah_l > .ah_item',limit = 20)

for item in result :
    st = item.text.strip().split('\n')
    print(f'{st[0]}위는 {st[1]}입니다')
 