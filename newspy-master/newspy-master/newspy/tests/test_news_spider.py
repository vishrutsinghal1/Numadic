import unittest

from newspy.spiders import news_spider
from . import fake_response_from_file


class NewsSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = news_spider.NewsSpider()

    def test_parse_ok(self):
        item = self.spider.parse_item(fake_response_from_file('samples/1.html'))
        self.assertIsNotNone(item)

    def test_item_url_ok(self):
        item = self.spider.parse_item(fake_response_from_file('samples/1.html'))
        self.assertIsNotNone(item['url'])

    def test_item_text_ok(self):
        item = self.spider.parse_item(fake_response_from_file('samples/1.html'))
        self.assertIsNotNone(item['text'])

    def test_item_text_null(self):
        item = self.spider.parse_item(fake_response_from_file('samples/2.html'))
        self.assertIsNone(item['text'])
