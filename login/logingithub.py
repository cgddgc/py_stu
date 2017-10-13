#-*-coding=utf-8-*-
import urllib,urllib2,re,requests,cookielib
from bs4 import BeautifulSoup

login_url="https://github.com/login"
'''
session=requests.session()
html=session.get(login_url,headers=header)
'''
html=urllib.urlopen(login_url)
soup=BeautifulSoup(html.read(),"lxml")
for input in soup.form.find_all("input"):
    if input.get("name")=="authenticity_token":
        token=input.get("value")
#print token
values={'login':'cgddgc@foxmail.com','password':'cgd1011','commit':'Sign+in','authenticity_token':token,'utf8':'%E2%9C%93'}
data=urllib.urlencode(values)
ckjar=cookielib.MozillaCookieJar('gitcookie.txt')
handler=urllib2.HTTPCookieProcessor(ckjar)
opener=urllib2.build_opener(handler)
opener.addheaders=[('Host','https://github.com'),('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'),('Referer','https://github.com')]
auth_url="https://github.com/session"
respon=opener.open(auth_url,data)
ckjar.save(ignore_discard=True,ignore_expires=True)
#respon=opener.open("https://github.com/")
print respon.read()