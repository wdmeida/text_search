# -*- coding: utf-8 -*-
import urllib3

http = urllib3.PoolManager()
page = http.request('GET', 'https://www.iaexpert.com.br')
page.status
page.data