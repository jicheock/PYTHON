#standard modules
# random: 랜덤 역할을 하는 도구 모음
# math: 수학 관련된 역할을 하는 도구 모음
# datetime: 시간 관련된 도구 모음
# os: 운영 체제 파일
import datetime


#from math import *
#qrt(100)
#import  datetime
#now=datetime.datetime.now()
#print(now)
import os
p=os.path.join(os.environ['USERPROFILE'], 'DESKTOP')
folder_name="ghghgh"
new_p=os.path.join(p,folder_name)
os.makedirs(new_p)
