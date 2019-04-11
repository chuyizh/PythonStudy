import requests
import time
from lxml import etree
import UsersAgent as UA
##################################################################################################################################################################
#西刺HTTP代理IP
def Xc_Ip(number):
    headers=UA.PcUA()
    item=[]
    for i in range(0,number):
        url='https://www.xicidaili.com/wt/'+str(i)
        try:
            urldata=requests.get(url,headers=headers).text
            html = etree.HTML(urldata)
            list = html.xpath("//tr[@class='odd']")
            list2=html.xpath("//tr[@class='']")
            for ip in list:
                ip_num = ip.xpath('./td[2]/text()')[0]
                port_num = ip.xpath('./td[3]/text()')[0]
                http = ip_num + ':' + port_num
                item.append(http)
            for ip in list2:
                ip_num = ip.xpath('./td[2]/text()')[0]
                port_num = ip.xpath('./td[3]/text()')[0]
                http = ip_num + ':' + port_num
                item.append(http)
        except:
            print('抓取错误')
    return item
##################################################################################################################################################################
#西刺HTTPS代理IP
def Xc_Ips(number):
    headers=UA.PcUA()
    item=[]
    for i in range(0,number):
        url='https://www.xicidaili.com/wn/'+str(i)
        try:
            urldata=requests.get(url,headers=headers).text
            html = etree.HTML(urldata)
            list = html.xpath("//tr[@class='odd']")
            list2=html.xpath("//tr[@class='']")
            for ip in list:
                ip_num = ip.xpath('./td[2]/text()')[0]
                port_num = ip.xpath('./td[3]/text()')[0]
                https = ip_num + ':' + port_num
                item.append(https)
            for ip in list2:
                ip_num = ip.xpath('./td[2]/text()')[0]
                port_num = ip.xpath('./td[3]/text()')[0]
                https = ip_num + ':' + port_num
                item.append(https)
        except:
            print('抓取错误')
    return item
##################################################################################################################################################################
#判断https的IP存活
def HttpsTure(ip):
    headers=UA.PcUA()
    url = 'https://www.baidu.com/'
    proxies = {'https': 'https://'+ip}
    try:
        j = requests.get(url, proxies=proxies, headers=headers, timeout=2)
        code=j.status_code
        if code==200:
            return ip
    except:
        pass
##################################################################################################################################################################
#判断http的IP存活
def HttpTure(ip):
    headers=UA.PcUA()
    url = 'https://www.baidu.com/'
    proxies = {'http': 'http://'+ip}
    try:
        j = requests.get(url, proxies=proxies, headers=headers, timeout=2)
        code=j.status_code
        if code==200:
            return ip
    except:
        pass
##################################################################################################################################################################
if __name__ == '__main__':
    while True:
        file=open('http.txt','a+')
        files=open('https.txt','a+')
        x=3
        https=Xc_Ips(x)
        http=Xc_Ip(x)
        for ip in http:
            try:
                s = HttpTure(ip)
                print(s)
                file.write(s + '\n')
            except:
                pass
        file.close()
        for ips in https:
            try:
                ss = HttpsTure(ips)
                files.write(ss + '\n')
            except:
                pass
        files.close()
        print('今日ip采集结束')
        time.sleep(86000)
