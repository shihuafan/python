import requests
from bs4 import BeautifulSoup
import bs4

def getHtml(url):
    kv={'User-Agent':'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
       
    except:
        print("网页html获取失败")
        return ""
        
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[4].string])
   
def printList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}\t"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    
def main():
    uinfo = []
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html=getHtml(url)
    fillUnivList(uinfo,html)
    printList(uinfo,20)
    
main()
