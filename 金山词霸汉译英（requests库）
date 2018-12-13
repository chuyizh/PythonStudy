import requests
import json
inputs=input('请输入需要翻译的中文：')
fanyi='http://fy.iciba.com/ajax.php?a=fy'
postdata={'f':'auto','t':'auto','w':inputs}
response=requests.post(fanyi,data=postdata)
result=json.loads(response.text,encoding='utf8')
dest=result['content']['out']
print('翻译的结果为：'+ dest)
