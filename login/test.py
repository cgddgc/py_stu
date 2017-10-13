import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
}

auth_url='https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
html = session.get(auth_url, headers=header)
soup=BeautifulSoup(html.content,"html.parser")
lt = soup.find('input',{'name':'lt'})['value']
execution = soup.find('input',{'name':'execution'})['value']
'''
print html.content
for input in soup.form.find_all("input"):
    if input.get("name")=="lt":
        lt=input.get("value")
    if input.get("name")=="execution":
        execution=input.get("value")
'''

def userpwdLogin():
    payload = {'username': 'cgddgc@foxmail.com',
               'password': 'cgd626723',
               'lt': lt,
               'execution': execution,
               '_eventId':'submit'}
    r = session.post(auth_url, data=payload, headers=header)
    s=session.get("http://my.csdn.net/my/score")
    print s.content

userpwdLogin()