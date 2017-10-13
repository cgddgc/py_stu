#-*-coding:utf-8-*-
import urllib,urllib2,cookielib,os
from bs4 import BeautifulSoup

req_url="https://passport.csdn.net/account/login"
login_url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

def getcookie():
    ckjar=cookielib.MozillaCookieJar("cookiecsdn.txt")
    ckproc=urllib2.HTTPCookieProcessor(ckjar)
    opener=urllib2.build_opener(ckproc)
    #request=urllib2.Request(login_url)
    respon=opener.open(login_url)
    soup=BeautifulSoup(respon.read(),"lxml")
    for input in  soup.form.find_all("input"):
        if input.get("name") == "lt":
            lt = input.get("value")
        if input.get("name") == "execution":
            execution = input.get("value")
        if input.get("name") == "_eventId":
            id = input.get("value")
    values={"username":"cgddgc@foxmail.com","password":"cgd626723",
"lt":lt,"execution":execution,"_eventId":id}
    req_data=urllib.urlencode(values)
    #request=urllib2.Request(login_url,req_data)
    opener.addheaders=[('Origin','https://passport.csdn.net'),('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'),('Referer','https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')]
    respon1=opener.open(login_url,req_data)
    #respon=opener.open(url1)
    result=respon1.read()
    mycsdn="http://my.csdn.net/my/score"
    #respon.close()
    ckjar.save(ignore_discard=True,ignore_expires=True)
    #result=opener.open(mycsdn)
    result1=opener.open("http://my.csdn.net/my/score")
    #print id
    print result1.read()
#getcookie()

def gethtml(url):
    ckjar=cookielib.MozillaCookieJar()
    ckjar.load("cookiecsdn.txt",ignore_discard=True,ignore_expires=True)
    handler=urllib2.HTTPCookieProcessor(ckjar)
    opener=urllib2.build_opener(handler)
    opener.addheaders=[('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    respon=opener.open(url)
    print respon.read()
gethtml("http://msg.csdn.net/")