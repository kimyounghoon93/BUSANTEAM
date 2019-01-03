# print('Hello World!')
#import requests
#btc = requests.get('https://api.bithumb.com/public/ticker/btc').json()['data']

#op = int(btc['opening_price'])
#cl = int(btc['closing_price'])
#mi = int(btc['min_price'])
#ma = int(btc['max_price'])
#if ma-mi+op > ma:
#    print("상승장")
#else:
#    print("하락장")

currency = requests.get('https://api.bithumb.com/public/ticker/all').json()['data']
for n in currency:
    op = float(currency[n]['opening_price'])
    cl = float(currency[n]['closing_price'])
    mi = float(currency[n]['min_price'])
    ma = float(currency[n]['max_price'])
    if ma-mi+op > ma:
        print(f"{n} 상승장")
    else:
       print(f"{n} 하락장")