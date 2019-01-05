import urllib.request
import re
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
f=open('xiushibaike.txt', 'w',encoding='utf-8')
for i in range(1,50):
    url='https://www.qiushibaike.com/text/page/'+str(i)+'/'
    data=urllib.request.urlopen(url).read().decode('utf8')
    redata=open('xiushibaikeRe.txt','r',encoding='utf8').read()
    rst=re.compile(redata).findall(data)
    f.write('\n--------\n'.join('%s' % x for x in rst))
f.close()
