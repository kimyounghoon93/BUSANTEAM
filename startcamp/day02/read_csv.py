import csv
with open('lunch.csv','r',encoding='utf8') as f:
    #lines = f.readlines()
    items = csv.reader(f)
    for item in items:
        print(item)

# with open('lunch.csv','r',encoding='utf8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip().split(','))
#         #.strip() 은 \n 삭제하는 명령