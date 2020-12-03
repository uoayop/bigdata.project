from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
import time
import urllib.parse
import datetime as dt

keyword="배민 시켰"
article_keyword="배민"
keyword_url= urllib.parse.quote_plus(keyword)          #키워드 설정
cols=['date','time','text']                     #수집할 데이터 목록

#def getURL(keyword,start,end):
#    return 'https://twitter.com/search?q='+str(keyword)+'%20since%3A'+str(start)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=ko'

def findTweet(soup):
    return (soup.find_all("div", {"class": "css-1dbjc4n r-18u37iz"}))

#def findName(soup):
#    return (soup.find_all("div", {"class": "css-901oao css-bfa6kz r-1re7ezh r-18u37iz r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}))

def findDate(soup):
    return (soup.find_all("a",{"class":"r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao"}))

def getSplit(datetime):
    time = datetime.split(' · ')[0]
    date = datetime.split(' · ')[1]
    return date,time



driver = webdriver.Chrome('/Users/doyeon/Downloads/chromedriver')
driver.implicitly_wait(2)

#driver.get('http://www.twitter.com')
#driver.get(url)

#driver.find_element_by_name('session[username_or_email]').send_keys('BigdataCrapper') # id 입력
#driver.find_element_by_name('session[password]').send_keys('1234qwer!') # pwd 입력

#로그인 버튼
#driver.find_element_by_css_selector("#react-root > div > div > div > main > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-1d2f490.r-7v430y.r-1j3t67a.r-u8s1d.r-1s7wq8y.r-13qz1uu > div > form > div > div.css-1dbjc4n.r-eqz5dr.r-1777fci > div > div > span > span").click()


#time.sleep(2)
#driver.implicitly_wait(2)

#검색창 클릭
#elem=driver.find_elements_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1jocfgc > div > div.css-1dbjc4n.r-gtdqiz.r-1jocfgc > div > div > div > div.css-1dbjc4n.r-1awozwy.r-aqfbo4.r-14lw9ot.r-18u37iz.r-1h3ijdo.r-15d164r.r-1vsu8ta.r-1xcajam.r-ipm5af.r-1jocfgc.r-136ojw6 > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div.css-901oao.r-hkyrab.r-6koalj.r-16y2uox.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > input").click()
#data = driver.find_elements_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div > div > div > section > div > div > div > div > div > div > article > div > div > div > div > div > div:nth-child(2) > div > div > span')


# for item in data:
#     print ('배고파', '\n')
# print (driver.current_url)
# print (driver.title)

#검색창 입력
#elem.send_keys('Wordbe')
#elem.submit()

totalfreq=[]
result_tweet=[]



# savestartdate=dt.date(year=2020,month=temp,day=1)
# startdate=dt.date(year=2020,month=temp,day=1)      #검색 기간 설정
# untildate=dt.date(year=2020,month=temp,day=2)      #시작날짜 +1
# enddate=dt.date(year=2020,month=temp,day=15)



# savestartdate=dt.date(year=2020,month=temp,day=16)
# startdate=dt.date(year=2020,month=temp,day=16)      #검색 기간 설정
# untildate=dt.date(year=2020,month=temp,day=17)      #시작날짜 +1
# enddate=dt.date(year=2020,month=temp,day=31)
#


# savestartdate=dt.date(year=2020,month=9,day=1)
# startdate=dt.date(year=2020,month=9,day=1)      #검색 기간 설정
# untildate=dt.date(year=2020,month=9,day=2)      #시작날짜 +1
# enddate=dt.date(year=2020,month=9,day=15)

def scrap(startdate,untildate,enddate,savestartdate):
    while not enddate==startdate:

        #url=getURL(keyword,startdate,untildate)


        url = 'https://twitter.com/search?q=' + keyword + '%20since%3A' + str(startdate) + '%20until%3A' + str(untildate) + '&amp;amp;amp;amp;amp;amp;lang=ko'
        driver.get(url)
        html = driver.page_source
        soup=BeautifulSoup(html,'html.parser')

        lastHeight = driver.execute_script("return document.body.scrollHeight")

        while True:
            dailyfreq={'Date':startdate}
            wordfreq=0
            after_word_cnt=0

            tweets=findTweet(soup)
            wordfreq+=len(tweets)

            pre_cnt=wordfreq

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            newHeight = driver.execute_script("return document.body.scrollHeight")
            print(newHeight)

            if newHeight != lastHeight:
                html = driver.page_source
                soup=BeautifulSoup(html,'html.parser')

                tweets = findTweet(soup)
                #name = findName(soup)

            #date = (soup.find_all("a",{"class":"r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao"}))
                date = (soup.find_all("a", {"class": "css-4rbku5 css-18t94o4 css-901oao r-m0bqgq r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"}))

                pre_cnt = len(tweets)
                wordfreq = len (tweets)

                for i in range(pre_cnt-1):
                    user_tweet = tweets[i].text

                    if user_tweet.find(article_keyword)==-1:  #광고 거르기
                        date.insert(i, "0000 · 0000")
                        user_date_and_time=date[i]
                        user_tweet="키워드 없음"
                        #print("=================", i, "/", pre_cnt, "=====================")
                        #print("[키워드 없음 : (%s)]"%user_tweet)


                    # if type(date[i])==str:  #검색어가 포함되어 있지 않으면
                    #     user_date_and_time= date[i]
                    #     user_tweet="키워드 없음"

                    else:
                        user_date_and_time = (date[i]).get("title")

                    user_date, user_time = getSplit(user_date_and_time)


                    result_tweet.append([user_date,user_time,user_tweet])
                    #print("[%s/%s]%s"%(user_date,user_time,user_tweet))



            else:
                dailyfreq['Frequency']=wordfreq
                wordfreq=0
                totalfreq.append(dailyfreq)
                startdate=untildate
                untildate+=dt.timedelta(days=1)
                print('=====untildate+1=======/',untildate.day)
                dailyfreq={}
                break

            lastHeight = newHeight

    df=(pd.DataFrame(result_tweet,columns=cols)).drop_duplicates('text',keep='first')
    display(df)
    df.to_csv('%s_%s_to_%s_scrap.csv'%(keyword,savestartdate,enddate),mode='w',encoding='utf-8-sig')

    driver.quit()

i=11

#1~10
savestartdate1=dt.date(year=2020,month=i,day=1)
startdate1=dt.date(year=2020,month=i,day=1)      #검색 기간 설정
untildate1=dt.date(year=2020,month=i,day=2)      #시작날짜 +1
enddate1=dt.date(year=2020,month=i,day=15)
scrap(startdate1,untildate1,enddate1,savestartdate1)

# #1,3,5,7,8,10
# savestartdate = dt.date(year=2020, month=i, day=16)
# startdate = dt.date(year=2020, month=i, day=16)  # 검색 기간 설정
# untildate = dt.date(year=2020, month=i, day=17)  # 시작날짜 +1
# enddate = dt.date(year=2020, month=i, day=31)
# scrap(startdate, untildate, enddate, savestartdate)

#4,6,9
# savestartdate = dt.date(year=2020, month=i, day=16)
# startdate = dt.date(year=2020, month=i, day=16)  # 검색 기간 설정
# untildate = dt.date(year=2020, month=i, day=17)  # 시작날짜 +1
# enddate = dt.date(year=2020, month=i, day=30)
# scrap(startdate, untildate, enddate, savestartdate)

#2
# savestartdate = dt.date(year=2020, month=i, day=16)
# startdate = dt.date(year=2020, month=i, day=16)  # 검색 기간 설정
# untildate = dt.date(year=2020, month=i, day=17)  # 시작날짜 +1
# enddate = dt.date(year=2020, month=i, day=28)
# scrap(startdate, untildate, enddate, savestartdate)