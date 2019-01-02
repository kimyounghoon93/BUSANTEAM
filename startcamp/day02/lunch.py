lunch = {
    '웅성돌솥밥':'054-484-5124',
    '삼성샌드위치':'으으으으',
    '아몰라맛나':'개졸립'
}

import csv

with open('lunch.csv','w',encoding='utf8',newline='') as f:
    csvwriter = csv.writer(f)
    for item in lunch.items(): # 리스트 [(key,value), ...]
        csvwriter.writerow(item)
        #f.write(f'{item[0]},{item[1]}\n')