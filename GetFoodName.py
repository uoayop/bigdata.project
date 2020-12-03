import pymysql
import csv
import json
import os
import nltk
from nltk.corpus import stopwords
from konlpy.tag import Komoran
from pprint import pprint
import re
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc


keywords=['먹고싶다','배고파 먹고싶다','배고파 배달','배고파 시켰','배고파 포장','배달 시켰','배민 시켰']
for keyword in keywords:
    path_dir="/Users/doyeon/PycharmProjects/selenium_scrap/"+keyword
    file_list=os.listdir(path_dir)
    file_list.sort()

    kmr=Komoran()


    # jan:0,1 -> 0,2   feb:2,3 -> 2,4    mar:4,5 -> 4,6   apr:6,7 -> 6,8   may:8,9 -> 8,10
    #jun: 10,11 -> 10,12    july:12,13 -> 12,14  aug: 14,15-> 14,16    sep: 16,17-> 16,18 oct: 18,19-> 18,20
    # for file in file_list:
    for  i in range(18,20,1):

        f = open(path_dir + "/" + file_list[i], 'r')

        csvReader = csv.reader(f)
        print(f.name)

        for row in csvReader:
            #user_date = (row[1])
            #user_time = (row[2])
            user_text = (row[3])
            user_text.replace('\n',' ')

            try:
                nouns=kmr.nouns(user_text)
                with open('october.json', 'a', encoding="utf-8") as make_file:
                    json.dump(nouns, make_file, ensure_ascii=False, indent=",")
            except:
                print('error ', row)
    f.close()


test=open('october.json','r')
# filter1=['배달\n','음식\n','주문\n','전화\n','배달원\n','시간\n','포장\n','오늘\n',
#         '이랑\n','생각\n','사람\n','점심\n','아침\n','내일\n','엄마\n','진짜\n']
#
# filter2=['배달\n','음식\n','저녁\n','아아\n','요즘\n','국물\n','소스\n','지금\n','혼자\n',
#          '친구\n','보고싶다\n','야식\n','때문\n','정도\n','소리\n','새벽\n']
#
# filter3=['시간\n','사실\n','완전\n','얘기\n','배달\n','추가\n','기분\n','요리\n',
#         '시발\n','질문\n','식욕\n','비티\n','인분\n','이번\n','엄마\n','진짜\n']
#
# filter4=['오늘\n','하루\n','취소\n','카페\n','처음\n','사진\n','메뉴\n','탐라\n',
#          '사랑\n','헤테로\n','엑스\n','이름\n','그룹\n','냄새\n','배제\n','오덕\n']
#
# filter5=['인생\n','한입\n','동생\n','인가\n','퇴근\n','알바\n','유닛\n','다이어트\n',
#          '동네\n','오랜만\n','다음\n','코로나\n','생일\n','언니\n','축하\n','배제\n']
#
# filter6=['진심\n','마음\n','행복\n','원래\n','제가\n','점심\n','동안\n','시작\n',
#          '저번\n','와서\n','택배\n','백현\n','아저씨\n','머리\n','가게\n','기사\n']
#
# filter7=['학교\n','라고\n','근처\n','안와\n','짜증\n','음식\n','마트\n','주문\n',
#          '보기\n','포함\n','아니\n','세상\n','고추\n','설정\n','주소\n','청년\n']
#
# filter8=['거리\n','느낌\n','거지\n','고민\n','기억\n','10월\n','10월 28일\n','10월 20일\n',
#          '콘텐츠\n','10월 27일\n','10월 24일\n','10월 23일\n','포함\n',
#          '10월 17일\n','설정\n','10월 22일\n','도착\n']
#
# filter9=['10월 26일\n','10월 30일\n','10월 16일\n','10월 25일\n','10월 31일\n','10월 18일\n',
#          '보기\n','설정\n','포함\n','콘텐츠\n','미디어\n','변경\n','10월 29일\n',
#          '트윗\n','10월 21일\n','10월 19일\n']
#
# tokens=[]
# pattern='[^\w\s]'
# repl=''
#
# for word in test:
#     filter_word=re.sub(pattern=pattern,repl=repl,string=word)
#     if (len(filter_word)>2):
#         tokens.append(filter_word)
#
# for i in tokens:
#     i.replace('\n','')
#     if (i in filter1):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n','')
#     if (i in filter2):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n','')
#     if (i in filter3):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n', '')
#     if (i in filter4):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n', '')
#     if (i in filter5):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n', '')
#     if (i in filter6):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n', '')
#     if (i in filter7):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n', '')
#     if (i in filter8):
#         tokens.remove(i)
#
# for i in tokens:
#     i.replace('\n', '')
#     if (i in filter9):
#         tokens.remove(i)
#
# text=nltk.Text(tokens, name='NMSC')
#
# # print(len(text.tokens))
# # print(len(set(text.tokens)))
# pprint(text.vocab().most_common(50))
#
#
#
# font_fname= '/Users/doyeon/Library/Fonts/NanumGothicCoding.ttf'
# font_name=font_manager.FontProperties(fname=font_fname).get_name()
# rc('font',family=font_name)
#
#
# plt.figure(figsize=(20,10))
# plt.xlabel('음식')
# plt.ylabel('선호도')
# plt.title('2020년도 10월 음식 선호도')
# text.plot(50)
#
test.close()
#

# python GetFoodName.py > output.txt



