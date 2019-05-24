import requests
from bs4 import BeautifulSoup
url="https://cubingchina.com"
kv={'User-Agent':'Mozilla/5.0'}
try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    demo=r.text
    soup=BeautifulSoup(demo,"html.parser")
    print(soup.text)
 #   print(r.text)
except:
    print("失败")
print("shihuafan")
