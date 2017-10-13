#-*-coding:utf-8-*-
import urllib,urllib2,cookielib,os

url="http://go.cgddgc.cn/auth/login"
url1="http://go.cgddgc.cn/user/node"
valu={"email":"cgddgc@foxmail.com","passwd":"cgd1011","remember_me":"week"}
data=urllib.urlencode(valu)
ckjar=cookielib.MozillaCookieJar("cookie.txt")
ckproc=urllib2.HTTPCookieProcessor(ckjar)
opener=urllib2.build_opener(ckproc)
request=urllib2.Request(url,data)
respon=opener.open(request)
respon=opener.open(url1)
result=respon.read()
respon.close()
ckjar.save()
print result

