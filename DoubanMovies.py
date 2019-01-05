import urllib.request
import re
url='https://movie.douban.com/chart'
data=urllib.request.urlopen(url).read().decode('utf8')
redata=open('cc.txt','r',encoding='utf8').read()
rst=re.compile(redata).findall(data)
with open('chart.csv','w') as f:
    f.write('\n'.join('%s %s %s %s %s %s %s %s %s %s %s' % x for x in rst))
