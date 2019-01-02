with open('ssafy.txt', 'r', encoding='utf8') as f:
    l = f.readlines()
l.reverse()
with open('ssafy_reversed.txt', 'w', encoding='utf8') as f:
    f.writelines(l)