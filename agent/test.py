# -*- coding: utf-8 -*-

import demo

url = 'http://www.baidu.com'

xz = demo.DownLoad()
html = xz.get(url)
print html.text