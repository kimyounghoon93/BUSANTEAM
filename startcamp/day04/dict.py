# 1. 딕셔너리 만들기
lunch = {
    '중국집':'02-123-123',
    '양식집':'054-123-123',
    '한식집':'031-123-123'
}

dinner = dict(중국집='02-123-123')

# 2. 만들어놓은 딕셔너리에 내용 추가하기
lunch['분식집'] = '053-123-123'

# 3. 딕셔너리 내용 가져오기
print(lunch['중국집']) # 출력값 => '02-123-123' lunch 안에 키값(중국집)의 : 벨류값이 나옴

print(lunch)


# 4. 딕셔너리 반복문 활용하기
# 기본활용
for key in lunch:
    print(key) #=> key
    print(lunch[key]) #=> value

# key만 가져오기 : .keys()
for key in lunch.keys():
    print(key)

# value만 가져오기 : .values()
for value in lunch.values():
    print(value)

# item (key, value) 가져오기 : .items()
# lunch.items() #=> [('중식','02'), ... ]
for item in lunch.items():
    print(item[0], item[1])

# 2개 = 자료형(list, tuple ...) 길이 2
a, b, c = 1, 2, 3
print(a)
print(b)

# 문제 1
# 수학점수는 80 국어는 90 음악은 100인데 반복을 통하여 벨류값을 가져와 평균을 출력하기
score = {
    '수학':80,
    '국어':90,
    '영어':100,

}

total_score = 0 #270
for subject_score in score.values():
    total_score = total_score + subject_score

avg_score = total_score / len(score) #> 270/3

total_score = sum(score.values()) # sum([80, 90, 100]) => 270
avg_score = total_score / len(score) #=> 270 / 3
print(avg_score)

# 문제 2
# 반평균 구하기

scores = {
    'a': {
        '수학':80,
        '국어':90,
        '영어':100,
    },
    'b': {
        '수학':80,
        '국어':90,
        '영어':100,
    }
}

scoreslist = list(scores.values())
s = 0 #0은 int (정수형태라는 뜻)
a = 0
for i in range(len(scoreslist)):
    s += sum(scoreslist[i].values())
    a += len(scoreslist[i])
avg = s / a
print(avg)

# 문제 2 풀이(반평균)
# total_score = 0
count = 0

# 1 ----  scores.values() #=> [{'수학:80, '국어:90, ... }]
# 2 ---- *for person_score in scores.values() #=> [{'수학:80', '국어:90', ... }]
# 3 ----  person_score #=> {'수학:80, '국어:90, ... }
# 4 ----  person_score.values() #=> {80, 90, 70, ... }
# 5 ---- *for subject_score in person_score.values():
# 6 ----                 #1번째 시행    #3번쨰
# 7 ----  #subject_score #=> 80        #70
# 8 ---- *total_score =+ subject_score
# 9 ---- *count += 1
#10 ---- *avg_score = total_score / count
#11 ---- *print(avg_score)

# 문제 3 도시별 최근 3일의 온도입니다.
city = {
    '서을': [-6, -10, 6],
    '대전': [-3, -6, 2],
    '광주': [-0, -2, 10],
    '구미': [2, -2, 9],
}
# 도시별 최근 3일의 온도 평균은
'''출력예시)
서울 : 값
대전 : 값
광주 : 값
구미 : 값
'''

for name, temp in city.items():
    sum_temp = sum(temp)
    avg_temp = sum_temp / 3 # 3대신 len(temp) 를 넣어도 된다!
    print(f'{name} : {round(avg_temp,1)}')

# 1 for 네임, 템프라고 정하겠다 씨티 아이템즈안에 있는 값들을
# 2 템프안의 값을 더한것을 썸템프 상자에 넣겠다
# 3 ''
# 4 프린트 하겠다 (f'{변수 혹은 회차별 문자} : {''}') f는 회차마다 값이 변하는 것을 프린트 할 때 쓰는 것
# 5 round(avg_temp,n) 소수점 n번째에서 자릿값을 자르겠다

for name, temp in city.items():
    # name #=> 서울
    # temp #=> 온도
    # 1. 반복
    total_temp = 0 #=> -10
    for t in temp:
        #1번째 시행
        #t => -6
        total_temp += t # t값을 토탈템프에 저장
    avg_temp = total_temp / len(temp) #=> -10 / 3

    # 2. 내장 함수
    avg_temp = sum(temp) / len(temp) #=> -10 / 3
    print(f'{name} : {avg_temp}')