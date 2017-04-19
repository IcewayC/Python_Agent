# -*- coding: utf-8 -*-
import requests
import re
import random
import time


#代理
# proxy = {'http':'ip:port'} #字典
# html = requests.get('https://www.baidu.com', proxies=proxy)


class DownLoad(object):

    def __init__(self):
        self.ip_list = []
        # 拿到代理IP www.haoip.com
        html = requests.get('http://www.haoip.cc/tiqu.htm')
        ip_content = re.findall(r'r/>(.*?)<b', html.text, re.S)  # 正则表达式, html源码

        for ip in ip_content:
            i = re.sub('\n', '', ip).strip()
            self.ip_list.append(i)
        self.user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0']

    def get(self, url, proxy=None, timeout=20, num=5):
        print '正在请求：', url
        UA = random.choice(self.user_agent_list)
        headers = {'User-Agent':UA}

        if proxy == None:
            num -= 4
            try:
                return requests.get(url, headers=headers, timeout=timeout)
            except:
                if num > 0:
                    time.sleep(10)
                    return self.get(url, num=num-1)
                else:
                    time.sleep(10)
                    IP = ''.join(random.choice(self.ip_list).strip())
                    proxy = {'http': IP}
                    return self.get(url, proxy=proxy, timeout=timeout)
        else:
            try:
                IP = ''.join(random.choice(self.ip_list).strip())
                proxy = {'http': IP}
                return requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
            except:
                if num > 0:
                    time.sleep(10)
                    IP = ''.join(random.choice(self.ip_list).strip())
                    proxy = {'http': IP}
                    print '正在更换代理'
                    print '当前代理：', proxy

                    return self.get(url, proxy=proxy, num=num-1)


# if __name__ == '__main__':
#     DownLoad().get('baidu.com')