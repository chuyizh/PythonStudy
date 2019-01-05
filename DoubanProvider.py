import urllib.request
import re
import pandas as pd
url='https://read.douban.com/provider/all'
data=urllib.request.urlopen(url).read().decode('utf8')
redata='<div class=\"name\">(.*?)</div><div class=\"works-num\">(.*?)</div>'
rst=re.compile(redata).findall(data)
for i in range(0,len(rst)):
    print(rst[i])
