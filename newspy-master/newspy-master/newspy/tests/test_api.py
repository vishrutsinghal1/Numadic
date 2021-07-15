import json
import random
import ssl
import string
import unittest

import requests
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings


class TestApi(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000/getnews/'
        settings = get_project_settings()
        connection = MongoClient(settings['MONGODB_HOST'],
                                 port=settings['MONGODB_PORT'],
                                 username=settings['MONGODB_USER'],
                                 password=settings['MONGODB_PASS'],
                                 ssl=True,
                                 ssl_cert_reqs=ssl.CERT_NONE)
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

        self.item = {
            'url': 'http://www.example.com/',
            'title': 'Unittest Test Article',
            'description': None,
            'section': None,
            'text': None,
            'author': None,
            'keywords': None
        }

    def test_no_keyword_returns_404(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 404)

    def test_no_results_found(self):
        keyword = ''.join(random.choices(string.ascii_letters, k=10))
        response = requests.get(self.base_url + keyword)
        self.assertEqual(len(json.loads(response.text)), 0)

    def test_result_found(self):
        self.item['url'] += str(random.random())
        self.item['text'] = ''.join(random.choices(string.ascii_letters + ' ', k=10))
        self.collection.insert_one(self.item)

        response = requests.get(self.base_url + self.item['text'])
        self.assertEqual(len(json.loads(response.text)), 1)

    def test_result_text_matches(self):
        self.item['url'] += str(random.random())
        self.item['text'] = ''.join(random.choices(string.ascii_letters + ' ', k=10))
        self.collection.insert_one(self.item)

        response = requests.get(self.base_url + self.item['text'])
        result = json.loads(response.text)
        self.assertEqual(result[0]['text'], self.item['text'])


if __name__ == "__main__":
    unittest.main()
