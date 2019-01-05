import urllib.request
import re
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,100):
    url='https://www.qiushibaike.com/text/page/'+str(i)+'/'
    data=urllib.request.urlopen(url).read().decode('utf8')
    redata=open('qiushibaikeRe.txt','r',encoding='utf8').read()
    rst=re.compile(redata).findall(data)
    with open('qiushibaike.txt', 'w',encoding='utf-8') as  f:
        f.write('\n--------\n'.join('%s' % x for x in rst))
