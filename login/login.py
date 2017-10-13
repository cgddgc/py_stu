#-*-coding:utf-8-*-
import urllib,urllib2,cookielib,os

url="http://go.cgddgc.cn/auth/login"
url1="http://go.cgddgc.cn"
valu={"email":"cgddgc@foxmail.com","passwd":"cgd1011","remember_me":"week"}
data=urllib.urlencode(valu)

def getcookie(req_url,req_data):
    ckjar=cookielib.MozillaCookieJar("cookie.txt")
    ckproc=urllib2.HTTPCookieProcessor(ckjar)
    opener=urllib2.build_opener(ckproc)
    request=urllib2.Request(req_url,req_data)
    respon=opener.open(request)
    #respon=opener.open(url1)
    result=respon.read()
    respon.close()
    ckjar.save(ignore_discard=True,ignore_expires=True)
#getcookie(url,data)

def gethtml(url):
    ckjar=cookielib.MozillaCookieJar()
    ckjar.load("cookie.txt")
    request=urllib2.Request(url)
    request.add_header('User-Agent', \
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
    result=opener.open(request)
    html=result.read()
    #result.close()
    file_html=open("1.html","w+")
    #file_html.write(result.info())
    file_html.write(html)
    file_html.close()
    #print result.info()
    #print html
gethtml("http://go.cgddgc.cn/user/")