import urllib.request
import re
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
url='https://blog.csdn.net/'
data=urllib.request.urlopen(url,timeout=15).read().decode('utf8')
redata='<a href="(.*?)" target="_blank"'
rst=re.compile(redata).findall(data)
for i in range(0,len(rst)):
    otherurl=rst[i]
    rstdata=urllib.request.urlopen(otherurl,timeout=15).read().decode('utf8')
    with open(str(i)+'.html','w',encoding='utf8') as f:
        f.write(rstdata)
