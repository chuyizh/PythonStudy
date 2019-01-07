import urllib.request
import re
import random
keys=[
    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
    'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'
]
def usersagent(Useragent):
    user=random.choice(Useragent)
    headers=('User-Agent',user)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
def proxyip(httpip):
    f = open(httpip, 'r')
    ip=[]
    for i in f:
        row = i.strip('\n')
        ip.append(row)
    userip=random.choice(ip)
    print(userip)
    proxy=urllib.request.ProxyHandler({'http':userip})
    opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
    urllib.request.install_opener(opener)
print('请输入要搜索的商品名:')
namenum=input()
print('请输入要下载的页面总数:')
pagenum=input()
pageint=int(pagenum)
page=2*int(pagenum)-1
print('爬虫模块加载中')
'''代理IP获取
print('开始加载代理IP')
usersagent(keys)
url='https://www.xicidaili.com/wt/'
redata=open('XicidailiHttpRe.txt','r',encoding='utf8').read()
urldata=urllib.request.urlopen(url,timeout=5).read().decode('utf8')
rst=re.compile(redata).findall(urldata)
with open('XcdlHttp.txt','w') as f:
    f.write('\n'.join('%s:%s' % x for x in rst))
f.close()
print('IP加载完毕')
'''
print('开始爬取图片')
for i in range(0,pageint):
    try:
        usersagent(keys)
        #proxyip('XicidailiHttpRe.txt')
        name = urllib.request.quote(namenum)
        pagestr=str(pageint)
        urljd='https://search.jd.com/Search?keyword='+name+'&enc=utf-8&page='+pagestr+'&click=0'
        print(urljd)
        data=urllib.request.urlopen(urljd,timeout=10).read().decode('utf-8','ignore')
        rejd= 'source-data-lazy-img="(.*?)" />'
        rstjd= re.compile(rejd,re.S).findall(data)
        for j in range(0,len(rstjd)):
            img=rstjd[j]
            imgurl='http:'+img
            file='C:\\Users\\乙\\Desktop\\JD\\'+str(i)+str(j)+'.jpg'
            urllib.request.urlretrieve(imgurl,filename=file)
        print('爬取结束，爬取了'+len(rstjd)+'个图片')
    except Exception as err:
        print(err)
        #print('抓取失败，请更换代理')
