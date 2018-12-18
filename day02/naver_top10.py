import requests
import bs4

response = requests.get('https://naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('.ah_l > .ah_item > .ah_a')

#print(result)

for item in result :
    print(item.text.strip().split('\n'))