import requests
import time
import re
from lxml import etree
heards = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
urls=['http://www.okzy.co','http://www.1977zy.com','http://www.172zy.net/','http://www.605zy.com/','http://zuidazy.net/','http://131zy.net','http://api.172zy.xyz/','http://yongjiuzy.cc/','http://jingpinzy.com/','http://www.jingpinzy.net/']
###########################################################################################
def starturl(url,i):
    newurl = []
    #print(url)
    try:
        for i in range(1,i):
            starturl = url+'?m=vod-index-pg-'+str(i)+'.html'
            #print(starturl)
            data = requests.get(starturl,timeout=1,headers=heards)
            #print(data.text)
            mid = etree.HTML(data.text)
            linktry = mid.xpath('//ul//span[@class="xing_vb4"]/a/@href')
            linktry1=mid.xpath('//td[@class="l"]/a/@href')
            if len(linktry)==0:
                link=linktry1
            else:
                link=linktry
            #print(link)
            for i in range(0, len(link)):
                newurl.append(url + link[i])
    except Exception as err:
        #print(err)
        print('主资源错误')
    return newurl
###########################################################################################
def everyurl(url):
    data = requests.get(url,headers=heards)
    mid= etree.HTML(data.text)
    newstry = mid.xpath('//div[@class="ibox playBox"]//div//div//ul/li/text()')
    newstry1=mid.xpath('//div[@class="contentURL"]/div//li/text()')
    if len(newstry)==0:
        news=newstry1
    else:
        news=newstry
    #print(news)
    remain='<h2>(.*?)</h2>'
    remain1='<!--片名开始-->(.*?)<!--片名结束-->'
    remain2='<li class="sa">.*?<!--.*?-->(.*?)<!--.*?--></li>'
    remain3='<a href=".*?">(.*?)</a></dd>'
    nametry = re.compile(remain,re.S).findall(data.text)
    name1try = re.compile(remain1, re.S).findall(data.text)
    name2try= re.compile(remain2, re.S).findall(data.text)
    name3try= re.compile(remain3, re.S).findall(data.text)
    #print(nametry)
    #print(name1try)
    #print(name2try)
    if len(nametry)==0:
        if len(name1try)==0:
            if len(name2try)==0:
                name=name3try
            else:
                name=name2try
        else:
            name=name1try
    else:
        name=nametry
    now = time.strftime('%Y-%m-%d %X', time.localtime())
    for j in range(0, len(name)):
        try:
            sub1=name[j]
            new=re.sub('<!--片名开始-->|<!--片名结束-->','',sub1,2)
            if len(new)==0:
                i=sub1
            else:
                i=new
            file = open('.\\电影1资源\\' + i + '.txt', 'w')
            file.write(now + '\n')
            for i in range(0, len(news)):
                file.write(news[i] + '\n')
            file.close()
            print(name[j] + '    采集成功')
        except Exception as err:
            #print('资源目录错误')
            print(err)
##################################################################################
def updata():
    url='https://raw.githubusercontent.com/chuyizh/demo/master/remand.txt'
    data=requests.get(url,headers=heards)
    x=int(data.text)
    if (x==1):
        print('软件为最新版本!')
    elif (x==2):
        #print('有新版本发布，请前往QQ群下载')
        print('有新版本发布')
    else:
        print('检查更新出错')
##################################################################################
print('检查更新中......')
time.sleep(2)
#updata()
while True:
    #print('-------- by:将往\n QQ群:733127451')
    print('-------- \n by:将往\n ')
    print('采集模块加载中，请稍后')
    time.sleep(1)
    print('请选择采集方式\n1.全部采集  2.选择采集  3.搜索采集')
    x=int(input('请输入数字:'))
    if (x==1):
        print('开始采集，资源较多，请耐心等待！')
        i=100
        for url in urls:
            try:
                newurl=starturl(url,i)
                for nurl in newurl:
                    try:
                        everyurl(nurl)
                    except Exception as err:
                        print('资源采集失败')
                        #print(err)
            except Exception as err:
                print('主资源错误')
                #print(err)
        print('资源采集结束')
        print('采集功能完善中，如有问题请及时反馈')
        print('                                   -----by:将往')
        time.sleep(2)
    elif x==2:
        print('请输入采集资源数：最大采集量为50000，每轮采集资源200，输入数字为2-400之间')
        i=int(input('请输入数字：'))
        for url in urls:
            try:
                newurl=starturl(url,i)
                print(newurl)
                for nurl in newurl:
                    try:
                        print(nurl)
                        everyurl(nurl)
                    except Exception as err:
                        print('资源采集失败')
                        #print(err)
            except Exception as err:
                print('主资源错误')
                #print(err)
        print('资源采集结束')
        print('采集功能完善中，如有问题请及时反馈')
        print('                                   -----by:将往')
        time.sleep(2)
    elif (x==3):
        #print('本模块开发中,请使用其他功能。最新版本请加群下载QQ群:733127451')
        print('本模块开发中,请使用其他功能。')
        print('功能完善中，如有问题请及时反馈')
        print('                                   -----by:将往')
        time.sleep(2)
    else:
        print('输入错误')


