with open('ssafy.txt','r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip()) #.strip() 을 포함하면 한줄 띄우기를 해제하게된다
        