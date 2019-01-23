import urllib.request
from lxml import etree
import re
import time
def everyurl(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url,timeout=5).read().decode('utf8','ignore')
    mid=etree.HTML(data)
    news=mid.xpath('//div[@class="ibox playBox"]//div//div//ul/li/text()')
    #name=mid.xpath('//head/title/text()')
    remain='<h2>(.*?)</h2>'
    name=re.compile(remain).findall(data)
    time.localtime()
    now=time.strftime('%Y-%m-%d %X',time.localtime())
    for j in range(0,len(name)):
        print(name[j]+ '    爬取成功')
        file=open('.\\电影资源\\'+name[j]+'.txt','w')
        file.write(now+'\n')
        for i in range(0,len(news)):
            file.write(news[i]+'\n')
        file.close()
def oneurl(oneurl):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    newurl = []
    for i in range(1,60):
        allurl = oneurl+'?m=vod-index-pg-'+str(i)+'.html'
        data = urllib.request.urlopen(allurl, timeout=5).read().decode('utf8', 'ignore')
        mid = etree.HTML(data)
        link = mid.xpath('//ul//span[@class="xing_vb4"]/a/@href')
        for i in range(0, len(link)):
            newurl.append(oneurl + link[i])
    return newurl
urls=['http://okokzy.cc/','http://www.1977zy.com/','http://129zy.com/','http://131zy.vip/','http://www.605zy.com/','http://www.1977zy.com/','http://zuidazy.net/']
print('爬虫加载中，请耐心等待')
time.sleep(2)
for url in urls:
    try:
        allurl=oneurl(url)
        print('加载完毕，开始爬取资源')
        for url in allurl:
            try:
                everyurl(url)
            except Exception as err:
                print('资源爬取失败')
    except Exception as err:
        print('主链接失效')
print('资源爬取结束')
print('爬虫功能完善中，如有问题请及时反馈')
print('                                   -----by:将往')
time.sleep(15)
