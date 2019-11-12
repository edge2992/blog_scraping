import lxml.html
from bson import ObjectId
from pymongo import MongoClient, response
from datetime import datetime
from extractcontent3 import ExtractContent


class TestMongo(object):
    def __init__(self):
        self.clint = MongoClient()
        self.db = self.clint['scraping-book']
        self.collection = self.db['hatena']

    def add_one(self):
        """データ挿入"""
        post = {
            'url': 'ハリネズミ',
            'title': 'ハリネズミ可愛い~',
            'html': datetime.now()
        }
        return self.collection.insert_one(post)

    def get_one(self):
        return self.collection.find_one()

    def get_from_oid(self, oid):
        return self.db.test.find_one({'_id': ObjectId(oid)})

    def update(self, title, content):
        rest = self.collection.update_one({"title": title}, {"$set": {"content": content}})
        return rest

    def delete(self):
        """マッチした最初のデータを削除"""
        rest = self.db.test.delete_one({"title": "ハムスター"})
        return rest

    def get_content(self, html):
        extractor = ExtractContent()
        extractor.analyse(html)
        text, title = extractor.as_text()
        return text

    def pad(self):
        find = self.collection.find(filter={'content': ''})
        for doc in find:
            content = self.get_content(doc['html'])
            self.update(doc['title'], content)

    def count_pad(self):
        find = self.collection.find(filter={'content': ''})
        print(find.count())


def main():
    TestMongo().pad()
    TestMongo().count_pad()


if __name__ == '__main__':
    main()