import requests
from lxml import etree
import re
import time
heards = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
#############################################################################################################################################
def seach (url,text):
    allurl=[]
    newurl=url+'/index.php?m=vod-search'
    data={
        'wd': text,
        'submit': 'search',
    }
    seachdata=requests.post(newurl,data=data,headers=heards)
    xpmid=etree.HTML(seachdata.text)
    link1=xpmid.xpath('//td[@class="l"]/a/@href')
    link2=xpmid.xpath('//span[@class="xing_vb4"]//@href')
    if (len(link1)==0):
        link=link2
    else:
        link=link1
    for i in link:
        aclink=url+i
        allurl.append(aclink)
    print(allurl)
    return allurl
###############################################################################################
def everyurl(url,num):
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
            file = open('.\\搜索资源\\' + i+'    第'+str(num)+'个资源'+'.txt', 'w')
            file.write(now + '\n')
            for i in range(0, len(news)):
                file.write(news[i] + '\n')
            file.close()
            print(name[j] + '    采集成功')
        except Exception as err:
            #print('资源目录错误')
            print(err)
#############################################################################################
if __name__ == '__main__':
    url = ['http://www.okzy.co', 'http://www.1977zy.com', 'http://www.172zy.net/', 'http://www.605zy.com/',
           'http://zuidazy.net/', 'http://131zy.net', 'http://api.172zy.xyz/', 'http://yongjiuzy.cc/',
           'http://jingpinzy.com/', 'http://www.jingpinzy.net/']
    txt=input('请输入要采集的内容：')
    num=0
    for url in url:
        print(url)
        allurl=seach(url,txt)
        print(allurl)
        for url in allurl:
            num=num+1
            everyurl(url,num)
