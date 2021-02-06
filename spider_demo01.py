#爬虫前奏
#明确目的
#找到数据对应的网页
#分析网页的结构找到数据所在的标签位置

#模拟Http请求，向服务器发送这个请求，获取到服务器返回给我们的HTML
#用正则表达式提取我们要的数据（名字，人气）

#获取HTTP

from urllib import request
import re
class Spider():
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class="avatar fl">([\s\S]*?)</span>'
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    num_pattern = '<i class="js-num">([\s\S]*?)</i>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        print(root_html[0])
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)
    



spider = Spider()
spider.go()