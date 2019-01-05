import urllib.request
import re
import pandas as pd
url='https://read.douban.com/provider/all'
data=urllib.request.urlopen(url).read().decode('utf8')
redata='<div class=\"name\">(.*?)</div><div class=\"works-num\">(.*?)</div>'
rst=re.compile(redata).findall(data)
with open('c1c.txt','w') as f:
    f.write('\n'.join('{}{}'.format(x[0],x[1])for x in rst))
   #f.write('\n'.join('%s %s' % x for x in rst))
