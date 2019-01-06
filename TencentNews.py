import urllib.request
import re
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
#url='http://xian.qq.com/'
url='https://pacaio.match.qq.com/irs/rcd?cid=108&ext=&token=349ee24cdf9327a050ddad8c166bd3e3&page=0&expIds=&callback=__jp1'
urldata=urllib.request.urlopen(url).read().decode('utf8','ignore')
redata=open('TencentNewIndexRe.txt','r',encoding='utf8').read()
rst=re.compile(redata,re.S).findall(urldata)
with open('Tencent.txt','w') as f:
    f.write('\n------\n'.join('%s，%s，%s' % x for x in rst))
reother='"url":"(.*?)"'
rstother=re.compile(reother,re.S).findall(urldata)
for i in range(0,len(rstother)):
    urlother=rstother[i]
    newother=urllib.request.urlopen(urlother,timeout=10).read().decode('utf-8','ignore')
    #urllib.request.urlretrieve(newother,'C:\\Users\\乙\\Desktop\\study\\newdata\\'+str(i)+'.html')
    with open(str(i)+'.html', 'w',encoding='utf-8') as f:
        f.write(newother)
