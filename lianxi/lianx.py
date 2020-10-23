#coding=utf-8
import re,requests,json,os
url='https://passport.cnblogs.com/user/signin'
headrer={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}
s=requests.session()
r=s.get(url,headers=headrer)
print(s.cookies)
c = requests.cookies.RequestsCookieJar()
c.set('.Cnblogs.Account.Antiforgery','CfDJ8AHUmC2ZwXVKl7whpe9_latO6276r1yw3jrKbKRgsUBl0u-VuPHi-TqVxD9SGGzpoN-d0oG8rTSlQto3NYV3GTasjbv6hnjQW4nL4E8iRQc6FzF5t-Vj3yOU3amEUgOKcL_6vL95UhRZuUD-fGTCitA')
c.set('.Cnblogs.Account.Session','CfDJ8AHUmC2ZwXVKl7whpe9%2Flas9zpaBjLHwxyFEhP5bIDVR8611%2Fm3YUJBAflKzmGJH15tMSlPL70ibrdhlyqexVhvTNxdV8%2B5xCisNwxc%2FJaJW3LoDa9Bk0bYpC8MD04VoaNRLuvMIPGgwqvwIXdiij0Xm%2FnvT8pypBRLENamTb0Xu')
s.cookies.update(c)
print(s.cookies)
requests.packages.urllib3.disable_warnings()
#跳过ssl验证会有两行warning警告，此方法可以消除

url2='https://i.cnblogs.com/EditPosts.aspx?opt=1'
body = {"__VIEWSTATE": "",
         "__VIEWSTATEGENERATOR":"FE27D343",
         "Editor$Edit$txbTitle":"这是绕过登录的标题：北京-宏哥",
         "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/duhong/</p>",
         "Editor$Edit$Advanced$ckbPublished":"on",
         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
         "Editor$Edit$Advanced$chkComments":"on",
         "Editor$Edit$Advanced$chkMainSyndication":"on",
         "Editor$Edit$lkbDraft":"存为草稿",
          }
r2=s.post(url2,data=body,verify=False)
print(r2.content.decode('utf-8'))
