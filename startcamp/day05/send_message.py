import os
import requests
token = os.getenv('TELEGRAM_BOT_TOKEN') #=> os.getenv를 통해 저장해놨던 값이 나옴
chat_id = os.getenv('CHAT_ID')          #=> 해서 미리 저장해놓고 암호화 하고난 뒤 os.getenv()를 넣어야함
# 하고싶은 것들

text = '반갑습니다'
print(chat_id)
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
