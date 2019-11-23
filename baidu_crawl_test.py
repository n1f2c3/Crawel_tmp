

import requests
import re
class baidudork():
    def __init__(self,dork_world):
        self.url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="
        self.baidu='https://www.baidu.com'
        self.world=dork_world
        self.headers={  # 发送HTTP请求时的HEAD信息，用于伪装为浏览器
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
        self.o_urls=[]
        self.end_flag=True
        self.html=""
        self.cr_url=""
        self.result=set()


    def request_content(self):
        try:
            r=requests.get(url=self.cr_url, headers=self.headers,)
            if r.status_code == 200:

                htmltext = r.text
                r.close()
                return htmltext
        except:
            return 0

    def get_baiduurls(self):
        self.html = self.request_content()
        if self.html!=0:
            # 获取当前页面中百度得链接
            o_urls=re.findall('href\=\"(http\:\/\/www\.baidu\.com\/link\?url\=.*?)\" class\=\"c\-showurl\"',self.html)
            # 去重
            o_urls=list(set(o_urls))
            self.o_urls=o_urls
            next = re.findall(' href\=\"(\/s\?wd\=[\w\d\%\&\=\_\-]*?)\" class\=\"n\"', self.html)
            # end = re.findall(u'>下一页&gt;</a>'.decode('utf-8'), self.html.decode('utf-8'))
            # if end.__len__()==0:
            #     return 0
            a='>下一页&gt;</a>'
            # print a
            # print type(a)
            # print type(self.html)
            a1=u'>下一页&gt;</a>';
            # print type(a1)
            end = re.findall(u'>下一页&gt;</a>', self.html)
            # print end
            # print self.html
            # print end.__len__()
            if end.__len__() == 0:
                self.end_flag =False
            else:
                self.end_flag=True

            if len(next) > 0:
                self.next_page_url=self.baidu+next[-1]
    def get_Realurl(self):
        for i in self.o_urls:
            r = requests.get(i, timeout=40, allow_redirects=False)
            result=r.headers['location']
            print (result)
            self.result.add(result)


    def switch_url(self):
        if self.end_flag is False:
            return 0
        else:
            self.set_current_url(self.next_page_url)
    def set_current_url(self, url):
        '''设置当前url'''
        self.cr_url = url
    def crawler(self):
        self.cr_url = self.url+self.world
        while True:
            self.get_baiduurls()
            self.get_Realurl()
            if self.switch_url()==0:
                break

a=baidudork("test")
a.crawler()
# for i in a.result:
#     print (i)
