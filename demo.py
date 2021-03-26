import requests
from bs4 import BeautifulSoup

req = requests.get("http://dns2.asia.edu.tw/~jdwang/PaperList.htm")
req.encoding="uft8"
if req.status_code==200 :
    #print(req.text)
    Soup = BeautifulSoup(req.text,"lxml")
    #print(Soup)
    result1 = Soup.find_all("li")
    fp=open("out3.txt","w",encoding="utf8")
    for val in result1:
        text2=val.text.replace('\n','')
        text3=text2.replace('  ','')
        print(text3)
        fp.write(text3 +"\n")
    fp.close()
else:
    print("no page")