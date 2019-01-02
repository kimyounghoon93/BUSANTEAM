import requests

response = requests.get('https://finance.naver.com/sise/')
print(response.text)
# ctrl + `
