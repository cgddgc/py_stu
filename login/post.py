#coding=utf-8
import urllib
import urllib2
content="sing a song"
#content=urllib.urlencode(content)
requrl="http://www.tuling123.com/openapi/api"
post_data="key=b8bb8bf591af8b522652fc2aa1e4a03a&info="+content+"&userid=cgddgc"
#post_data=urllib.urlencode(post_data)
req=urllib2.Request(url=requrl,data=post_data)
#print req
result=urllib2.urlopen(req)
res=result.read()
print res