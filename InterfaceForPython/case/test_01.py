# coding:utf-8
import unittest
import requests
from Common.logger import Log
class Test(unittest.TestCase):
    log = Log()
    def test_01(self):
        self.log.info('------test------')
        url = 'http://www.baidu.com'
        self.log.info('测试url:%s' %url)
        r = requests.get(url)
        print(r.content.decode('utf8'))
        self.assertEqual(r.status_code,200)
