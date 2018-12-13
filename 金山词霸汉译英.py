import urllib.request
import urllib.parse
import json
fanyi='http://fy.iciba.com/ajax.php?a=fy'
inputs=input('请输入需要翻译的中文：')
postdata={'f':'auto','t':'auto','w':inputs}
postdata=urllib.parse.urlencode(postdata)
postdata=bytes(postdata,encoding='utf8')
request=urllib.request.Request(fanyi)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
response=urllib.request.urlopen(request,data=postdata)
data=response.read().decode('utf8')
result=json.loads(data)
dest=result['content']['out']
print('翻译的结果为：'+ dest)
