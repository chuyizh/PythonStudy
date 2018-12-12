```python
import urllib.request
import urllib.parse
import json
fanyi='http://fy.iciba.com/ajax.php?a=fy'
inputs=input('请输入需要翻译的中文：')
postdata={'f':'auto','t':'auto','w':inputs}
postdata=urllib.parse.urlencode(postdata)
postdata=bytes(postdata,encoding='utf8')
response=urllib.request.urlopen(fanyi,data=postdata)
data=response.read().decode('utf8')
result=json.loads(data)
dest=result['content']['out']
print('翻译的结果为：'+ dest)
```
