'''
Created on 2016-4-15

@author: hys mac
'''
#coding：utf8

import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutputer()

    def craw(self, root_urls):
        count = 1

        self.urls.add_new_url(root_urls)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' %(count, new_url))
                html_cout = self.downloader.downloader(new_url)

                new_urls, new_data = self.parser.parse(new_url, html_cout)

                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)

                if count == 100:
                    break
                count += 1
            except Exception as e:
                print('craw fails--', e)

        self.output.output()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

