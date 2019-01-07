import urllib.request
import re
import random
keys = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
]
#随机User-Agent
def usersagent(Useragent):
    user=random.choice(Useragent)
    headers=('User-Agent',user)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
#抓取代理ip
usersagent(keys)
url='https://www.xicidaili.com/wt/'
redata=open('XicidailiHttpRe.txt','r',encoding='utf8').read()
urldata=urllib.request.urlopen(url,timeout=5).read().decode('utf8')
rst=re.compile(redata).findall(urldata)
with open('XcdlHttp.txt','w') as f:
    f.write('\n'.join('%s:%s' % x for x in rst))
f.close()
#随机ip
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
f=open('xiushibaike.txt', 'w',encoding='utf-8')
for i in range(1, 13):
    try:
        usersagent(keys)
        #proxyip('XcdlHttp.txt')
        url='https://www.qiushibaike.com/text/page/'+str(i)+'/'
        data=urllib.request.urlopen(url,timeout=15).read().decode('utf8','ignore')
        redata=open('xiushibaikeRe.txt','r',encoding='utf8').read()
        rst=re.compile(redata).findall(data)
        f.write('\n--------\n'.join('%s' % x for x in rst))
    except Exception as err:
        print(err)
