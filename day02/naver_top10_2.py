import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response,'html.parser')

rank = soup.select('.ah_l > .ah_item > .ah_a > .ah_r')
name = soup.select('.ah_l > .ah_item > .ah_a > .ah_k')

for i in range(20):
    r = rank[i]
    n = name[i]
    print(f'{r.text}위는 {n.text}입니다')