#import os

#os.chdir(r'C:\Users\student\yh\day02\dummy')
# print(os.getcwd()) 파일위치
#for filename in os.listdir('.'): #여기서 .은 현재폴더를 얘기함 현재폴더에 있는 모든파일을 가져와서 리스트화
 #   os.rename('filename', f'지원자_{filename}') #()안은 1.파일이름, 2.뭘로 바꿀껀지

# 합격자_0_누구누구.txt

import os

os.chdir(r'C:\Users\student\yh\day02\dummy')
# print(os.getcwd()) 파일위치
for filename in os.listdir('.'): #여기서 .은 현재폴더를 얘기함 현재폴더에 있는 모든파일을 가져와서 리스트화
    #1. replace 함수 이용, 새로운 파일이름 생성
    #new_filename = filename.replace('지원자_','합격자_')
    #2. os.rename 함수이용, 파일이름 변경
    #os.rename(filename,new_filename)
    filename2 = filename.replace('지원자_', '합격자_') #()안은 1.바꿀 문자열, 2.뭘로 바꿀껀지
    os.rename(filename,filename2)